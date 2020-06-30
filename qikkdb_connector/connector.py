import logging
import socket
import struct
import time
from enum import Enum
from threading import Lock, Timer
from datetime import datetime

from Types import QComplexPolygon
from Types import QPoint

from google.protobuf.any_pb2 import Any

from Message import (InfoMessage_pb2, QueryMessage_pb2,
                     QueryResponseMessage_pb2, SetDatabaseMessage_pb2, BulkImportMessage_pb2)
from Message.CSVImportMessage_pb2 import COLUMN_FLOAT, COLUMN_INT, COLUMN_LONG, COLUMN_DOUBLE, COLUMN_STRING, \
    COLUMN_POINT, COLUMN_POLYGON, COLUMN_INT8_T

lock = Lock()
KEEP_ALIVE_TIME = 25
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

class DataType(Enum):
    Bool = 1,
    Int = 2,
    Float = 3,
    Int64 = 4,
    Double = 5,
    Point = 6,
    Polygon = 7,
    String = 8
    Datetime = 9

# Class for timer thread, defined restart,start and cancel functions
class RepeatingTimer(object):
    def __init__(self, interval, function, _socket):
        self.interval = interval
        self.f = function
        self.socket = _socket
        self.daemon = True

        self.timer = None

    def callback(self):
        logging.debug("Calling keep_alive")
        self.f(self.socket)
        logging.debug("Calling start")
        self.start()
        logging.debug("Success keep_alive and start timer")

    def restart(self):
        self.cancel()
        self.start()

    def cancel(self):
        self.timer.cancel()

    def start(self):
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()

def keep_alive(_socket):
    """

    :param _socket:  created socket for communication with server
    :return:

    kepp alive funcion, which is sending heartbeat messages to server. Sends message every 25s
    """
    # Start only if is lock not acquired
    if lock.acquire(False):
        logging.debug("Keep alive lock acquired, execution of commands  ")
        start_msg = InfoMessage_pb2.InfoMessage(
            Message="", Code=InfoMessage_pb2.InfoMessage.StatusCode.Value("HEARTBEAT")
        )
        send_message(_socket, start_msg)
        logging.info("Heartbeat was sent")
        recv_bytes = read_message(_socket)

        recv_msg = unpack_type(
            recv_bytes,
            InfoMessage_pb2.InfoMessage.DESCRIPTOR,
            InfoMessage_pb2.InfoMessage(),
        )
        if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.OK:
            logging.info("Heartbeat acknowledgment, connection OK")
        else:
            print("error")
            logging.info(recv_msg)
            exit(-1)
    else:
        logging.debug("Lock is assigned, no needed for keep_alive")
        return
    if lock.locked():
        logging.debug("Lock released in keep_alive")
        lock.release()


def create_socket(host, port):
    """
    Function which create socket with server

    :return: nothing
    """

    try:
        tcp_ip = socket.gethostbyname(host)
        tcp_port = port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((tcp_ip, tcp_port))
        logging.info("Socket created successfully")
        return s
    except Exception as e:
        logging.error(f"Create_socket error: {e}")


def send_message(_socket, msg):
    """
    Function send input message to certain socket

    :param _socket: created socket for communication with server
    :param msg: message, which we will send to server
    :return: nothing
    """

    any = Any()
    any.Pack(msg)
    m = any.SerializeToString()
    #  format of byte array is big endian
    packed_len = struct.pack(">L", any.ByteSize())
    # We need send first length of message and then message
    _socket.send(packed_len)
    _socket.send(m)


def read_message(_socket):
    """
    Function read message from certain socket

    :param _socket: created socket for communication with server
    :return: received byte array
    """

    total_read = 0
    now_reade = 0
    now_buf = bytearray(4)
    total_buf = bytearray(0)
    # time.sleep(1)
    # We need to read length of message coming from server
    while total_read != 4:
        now_reade = _socket.recv_into(now_buf, 4 - total_read)
        if now_reade == 4:
            total_buf += now_buf[:now_reade]
            break
        else:
            total_buf += now_buf[:now_reade]
            total_read += now_reade

    msg_len = struct.unpack(">L", total_buf)[0]
    total_read = 0
    data_rcv = bytearray(0)
    now_buf = bytearray(msg_len)
    while total_read != msg_len:
        # total_read += _socket.recv_into(data_rcv, msg_len - total_read)
        now_reade = _socket.recv_into(now_buf, msg_len - total_read)
        if now_reade == msg_len:
            data_rcv += now_buf[:now_reade]
            break
        else:
            data_rcv += now_buf[:now_reade]
            total_read += now_reade

    return data_rcv


def unpack_type(data, message_type, type):
    """
    Function unpack array of bytes to protobuf type

    :param data: received data from read_message() function
    :param message_type: descriptor of message to unpack
    :param type: type of message to unpack
    :return: unpacked protobuf message
    """

    any = Any()
    any.ParseFromString(data)
    if any.Is(message_type):
        any.Unpack(type)

    return type


def establish_connection(_socket):
    """
    After creating socket, we need to establish connection with server,
    which means to send "hello message"

    :param _socket: created socket for communication with server
    :return: nothing
    """

    heartbeat = None
    start_msg = InfoMessage_pb2.InfoMessage(
        Message="", Code=InfoMessage_pb2.InfoMessage.StatusCode.Value("CONN_ESTABLISH")
    )

    try:
        send_message(_socket, start_msg)
        recv_bytes = read_message(_socket)
        recv_msg = unpack_type(
            recv_bytes,
            InfoMessage_pb2.InfoMessage.DESCRIPTOR,
            InfoMessage_pb2.InfoMessage(),
        )
        if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.OK:
            logging.info("Connection established (StatusMessage = OK)...")
            # create object of keep_alive thread
            heartbeat = RepeatingTimer(KEEP_ALIVE_TIME, keep_alive, _socket)
            # Start keep_alive
            heartbeat.start()
            logging.info("Heartbeat started")
            logging.info("Connection established successfully")
        else:
            logging.error(recv_msg)
    except Exception as e:
        logging.error(f"Establish_connection error: {e}")
        exit(-1)

    return heartbeat


def use_database(_socket, database_name, heartbeat):
    """
    This function connect to input database

    :param heartbeat: keep_alive thread object
    :param _socket: created socket for communication with server
    :param database_name: name of database, which will be used
    :return: nothing
    """

    use_db_msg = SetDatabaseMessage_pb2.SetDatabaseMessage(DatabaseName=database_name)
    # acquire lock, execute comands and free lock after, if is lock acquired, will wait until its free
    with lock:
        logging.debug("Lock acquired in use_db")
        try:
            send_message(_socket, use_db_msg)
            recv_bytes = read_message(_socket)
        except Exception as e:
            logging.error(f"Use_db error: {e}")
            return

    heartbeat.restart()
    recv_msg = unpack_type(
        recv_bytes,
        InfoMessage_pb2.InfoMessage.DESCRIPTOR,
        InfoMessage_pb2.InfoMessage(),
    )
    if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.OK:
        logging.info(f"Successfully switched to database: {database_name}")
    else:
        logging.error(f"{recv_msg}")
        heartbeat.cancel()


def query(_socket, query_text, heartbeat):
    """
    Function send query to server and then send GetNextResult messages
    to server, to get data in bulks formatted in array of dictionaries

    :param heartbeat: keep_alive thread object
    :param _socket: created socket for communication with server
    :param query_text:  sql expression
    :return: table which is result of sql expression
    """

    query_msg = QueryMessage_pb2.QueryMessage(Query=query_text)

    try:
        # here we use lock.acquire because we need have locke for socket until we execute all comands here
        lock.acquire()
        logging.debug("Lock acquired in query()")
        heartbeat.cancel()

        send_message(_socket, query_msg)
        recv_bytes = read_message(_socket)

        recv_msg = unpack_type(
            recv_bytes,
            InfoMessage_pb2.InfoMessage.DESCRIPTOR,
            InfoMessage_pb2.InfoMessage(),
        )
        if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.WAIT:
            logging.info("Waiting for query (StatusMessage = Wait)...")
        else:
            logging.info(recv_msg)

        recv_bytes = read_message(_socket)
        recv_msg = unpack_type(
            recv_bytes,
            InfoMessage_pb2.InfoMessage.DESCRIPTOR,
            InfoMessage_pb2.InfoMessage(),
        )
        if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.GET_NEXT_RESULT:
            logging.info("Waiting for next result (StatusMessage = GetNextResult)...")
            array_dictionaries = []

            # Server is sending result of query in bulks, we need to call get_next_result until it returns None
            while 1:
                result = get_next_result(_socket, heartbeat)
                if result is None:
                    break
                else:
                    array_dictionaries = array_dictionaries + result
        else:
            logging.error(recv_msg)
            exit(-1)

        lock.release()
        logging.debug("Lock released in use_db")
        heartbeat.start()
        return array_dictionaries

    except Exception as e:
        logging.error(f"Query error: {e}")
        heartbeat.cancel()
        exit(-1)


def get_next_result(_socket, heartbeat):
    """
    This function sends GetNextResult messages and gets data in bulks from server
    until it gets some data, then return all data in array of dictionaries

    :param heartbeat: keep_alive thread object
    :param _socket: created socket for communication with server
    :return: part of sql expression, whole response is divided into bulks
    """

    next_message = InfoMessage_pb2.InfoMessage(
        Message="", Code=InfoMessage_pb2.InfoMessage.StatusCode.Value("GET_NEXT_RESULT")
    )
    try:
        send_message(_socket, next_message)
        # time.sleep(1)
        recv_bytes = read_message(_socket)

        recv_msg = unpack_type(
            recv_bytes,
            QueryResponseMessage_pb2.QueryResponseMessage.DESCRIPTOR,
            QueryResponseMessage_pb2.QueryResponseMessage(),
        )

        if recv_msg == 0:
            # If it's not query response message, we check another possible format of received message
            recv_msg = unpack_type(
                recv_bytes,
                InfoMessage_pb2.InfoMessage.DESCRIPTOR,
                InfoMessage_pb2.InfoMessage(),
            )
            if recv_msg != 0:
                if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.OK:
                    logging.info("StatusMessage = OK")
                else:
                    logging.info(recv_msg)
                    return None
            logging.error("Invalid response from server")
            exit(-1)

        result = convert_to_dictionaries(recv_msg)

    except Exception as e:
        logging.error(f"Reading bytes error: {e}")
        heartbeat.cancel()
        exit(-1)

    return result


def fill_table(column, data, result, dataType):
    """
    This function fill result table with certain column of values

    :param column: name of column, which we added to result table
    :param data: values in  column
    :param result: out table, which we are updating according to processed columns
    :param dataType: enumerated data type for conversion cases
    :return: updated table
    """

    size = len(data)
    # Initialization of array of dictionaries with bulk size
    if result is None:
        result = [{} for i in range(size)]
    for i in range(size):
        if dataType == DataType.Datetime:
            result[i][column] = datetime.utcfromtimestamp(data[i])
        else:
            result[i][column] = data[i]

    return result


def check_null_values(data, byte_array, result, column, dataType):
    """

    :param data: values in  column
    :param byte_array: nullBitMask array for checking null values in column
    :param result: out table, which we are updating according to processed columns
    :param column: name of column,  which we added to result table
    :param dataType: enumerated data type for conversion cases
    :return: updated table
    """

    if result is None:
        result = [{} for i in range(len(data))]

    for index in range(len(data)):
        shift_offset = index % 64
        byte_offset = index / 64
        if (byte_array[int(byte_offset)] >> int(shift_offset) & 1) == 0:
            # there is no null value in this cell and we add value to out table
            if dataType == DataType.Datetime:
                result[index][column] = datetime.utcfromtimestamp(data[index])
            else:
                result[index][column] = data[index]
        else:
            # there is null value in this cell, so we need add None to out table
            result[index][column] = None
    return result


def convert_to_dictionaries(data):
    """
    Function convert input data bulk into array of dictionaries

    :param data: received data
    :return: table
    """

    ordered_column_names = []
    result = None

    # From received data we get column order
    for column in data.columnOrder:
        ordered_column_names.append(column)

    # According to column order we take column by column and save values of columns in out table
    # Every column has to be treated according by type of values in it, because of access to values in data payload
    for column in ordered_column_names:
        x = data.payloads[column]

        if len(x.intPayload.intData) != 0:
            # checks if actual column is in nullbitmasks
            if column in data.nullBitMasks:
                # column is in nullBitMasks so we need to check null values in column
                result = check_null_values(
                    x.intPayload.intData, data.nullBitMasks[column].nullMask, result, column, DataType.Int
                )
            else:
                # column is not in nullBitMasks so we just fill our result dictonary with values from this column
                result = fill_table(column, x.intPayload.intData, result)

        elif len(x.floatPayload.floatData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.floatPayload.floatData, data.nullBitMasks[column].nullMask, result, column, DataType.Float
                )
            else:
                result = fill_table(column, x.floatPayload.floatData, result)

        elif len(x.int64Payload.int64Data) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.int64Payload.int64Data, data.nullBitMasks[column].nullMask, result, column, DataType.Int64
                )
            else:
                result = fill_table(column, x.int64Payload.int64Data, result)

        elif len(x.dateTimePayload.dateTimeData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.dateTimePayload.dateTimeData, data.nullBitMasks[column].nullMask, result, column, DataType.Datetime
                )
            else:
                result = fill_table(column, x.dateTimePayload.dateTimeData, result)

        elif len(x.doublePayload.doubleData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.doublePayload.doubleData,
                    data.nullBitMasks[column].nullMask,
                    result,
                    column,
                    DataType.Double
                )
            else:
                result = fill_table(column, x.doublePayload.doubleData, result)

        elif len(x.pointPayload.pointData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.pointPayload.pointData, data.nullBitMasks[column].nullMask, result, column, DataType.Point
                )
            else:
                result = fill_table(column, x.pointPayload.pointData, result)

        elif len(x.polygonPayload.polygonData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.polygonPayload.polygonData,
                    data.nullBitMasks[column].nullMask,
                    result,
                    column,
                    DataType.Polygon
                )
            else:
                result = fill_table(column, x.polygonPayload.polygonData, result)

        elif len(x.stringPayload.stringData) != 0:
            if column in data.nullBitMasks:
                result = check_null_values(
                    x.stringPayload.stringData,
                    data.nullBitMasks[column].nullMask,
                    result,
                    column,
                    DataType.String
                )
            else:
                result = fill_table(column, x.stringPayload.stringData, result)

    return result

BULK_IMPORT_FRAGMENT_SIZE = 8192 * 1024


def bulk_import(_socket, tableName, columns, data):

    columnNames = columns.keys()
    columnTypes = columns.values()

    for columnName, columnType in columns.items():

        size = len(data)
        elementCount = size
        typeSize = 1
        nullMask = None
        dataBuffer = bytearray()
        serverColumnType = COLUMN_INT

        if columnType == DataType.Bool:
            typeSize = 1
            serverColumnType = COLUMN_INT8_T
            size = size * typeSize
            for i in range(elementCount):
                if data[i][columnName] == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for j in range(nullMaskSize):
                            nullMask[j] = 0
                    shiftIdx = i % 8
                    byteIdx = i / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elementBytes = bytearray(struct.pack("?", 0))
                else:
                    elementBytes = bytearray(struct.pack("?", data[i][columnName]))
                dataBuffer.extend(elementBytes)

        elif columnType == DataType.Int:
            typeSize = 4
            serverColumnType = COLUMN_INT
            size = size * typeSize
            for i in range(elementCount):
                if data[i][columnName] == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for j in range(nullMaskSize):
                            nullMask[j] = 0
                    shiftIdx = i % 8
                    byteIdx = i / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elementBytes = bytearray(struct.pack("i", 0))
                else:
                    elementBytes = bytearray(struct.pack("i", data[i][columnName]))
                dataBuffer.extend(elementBytes)

        elif columnType == DataType.Int64:
            typeSize = 8
            serverColumnType = COLUMN_LONG
            size = size * typeSize
            for i in range(elementCount):
                if data[i][columnName] == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for j in range(nullMaskSize):
                            nullMask[j] = 0
                    shiftIdx = i % 8
                    byteIdx = i / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elementBytes = bytearray(struct.pack("q", 0))
                else:
                    elementBytes = bytearray(struct.pack("q", data[i][columnName]))
                dataBuffer.extend(elementBytes)

        elif columnType == DataType.Float:
            typeSize = 4
            serverColumnType = COLUMN_FLOAT
            size = size * typeSize
            for i in range(elementCount):
                if data[i][columnName] == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for j in range(nullMaskSize):
                            nullMask[j] = 0
                    shiftIdx = i % 8
                    byteIdx = i / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elementBytes = bytearray(struct.pack("f", 0))
                else:
                    elementBytes = bytearray(struct.pack("f", data[i][columnName]))
                dataBuffer.extend(elementBytes)

        elif columnType == DataType.Double:
            typeSize = 8
            serverColumnType = COLUMN_DOUBLE
            size = size * typeSize
            for i in range(elementCount):
                if data[i][columnName] == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for j in range(nullMaskSize):
                            nullMask[j] = 0
                    shiftIdx = i % 8
                    byteIdx = i / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elementBytes = bytearray(struct.pack("d", 0))
                else:
                    elementBytes = bytearray(struct.pack("d", data[i][columnName]))
                dataBuffer.extend(elementBytes)

        elif columnType == DataType.String:
            serverColumnType = COLUMN_STRING
            size = 0
            defaultElem = ""
            for i in range(elementCount):
                if data[i][columnName] != None:
                    size = size + 4 + len(data[i][columnName])
                else:
                    size = size + 4 + len(defaultElem)
            dataBuffer = bytearray()
            i = 0
            for j in range(elementCount):
                elem = data[j][columnName]
                if elem == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for k in range(nullMaskSize):
                            nullMask[k] = 0
                    shiftIdx = j % 8
                    byteIdx = j / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elem = defaultElem
                lenBytes = bytearray(struct.pack("i", len(elem)))
                dataBuffer.extend(lenBytes)
                dataBuffer.extend(elem.encode('utf-8'))

        elif columnType == DataType.Point:
            serverColumnType = COLUMN_POINT
            size = 0
            defaultElem = QPoint(0, 0)
            points = []
            for i in range(elementCount):
                if data[i][columnName] != None:
                    p = QPoint.CreateFromWkt(data[i][columnName])
                    points.append(p)
                    size = size + 4 + p.point.ByteSize()
                else:
                    size = size + 4 + defaultElem.point.ByteSize()
            dataBuffer = bytearray()
            i = 0
            for elem in points:
                print(str(elem.point.geoPoint.longitude) + ", " + str(elem.point.geoPoint.latitude))
                if elem == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for k in range(nullMaskSize):
                            nullMask[k] = 0
                    shiftIdx = j % 8
                    byteIdx = j / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elem = defaultElem
                lenBytes = bytearray(struct.pack("i", elem.point.ByteSize()))
                dataBuffer.extend(lenBytes)
                dataBuffer.extend(elem.point.SerializeToString())

        elif columnType == DataType.Polygon:
            serverColumnType = COLUMN_POLYGON
            size = 0
            defaultElem = QComplexPolygon()
            polygons = []
            for i in range(elementCount):
                if data[i][columnName] != None:
                    p = QComplexPolygon.CreateFromWkt(data[i][columnName])
                    polygons.append(p)
                    size = size + 4 + p.complexPolygon.ByteSize()
                else:
                    size = size + 4 + defaultElem.complexPolygon.ByteSize()
            dataBuffer = bytearray()
            i = 0
            for elem in polygons:
                print(str(elem.complexPolygon))
                if elem == None:
                    if nullMask == None:
                        nullMaskSize = int((elementCount + 8 - 1) / 8)
                        nullMask = bytearray(int(nullMaskSize))
                        for k in range(nullMaskSize):
                            nullMask[k] = 0
                    shiftIdx = j % 8
                    byteIdx = j / 8
                    nullMask[int(byteIdx)] = nullMask[int(byteIdx)] | ((1 << int(shiftIdx)) & 255)
                    elem = defaultElem
                lenBytes = bytearray(struct.pack("i", elem.complexPolygon.ByteSize()))
                dataBuffer.extend(lenBytes)
                dataBuffer.extend(elem.complexPolygon.SerializeToString())

        fragmentSize = 0;
        lastNullBuffOffset = -1;
        i = 0
        while i < size:
            elemCount = 0

            if columnType == DataType.String or columnType == DataType.Point or columnType == DataType.Polygon:
                fragmentSize = 0
                while fragmentSize < BULK_IMPORT_FRAGMENT_SIZE and i + fragmentSize < size:
                    fragmentSize = fragmentSize + 4
                    lenBytes = dataBuffer[(i + fragmentSize - 4):(i + fragmentSize)]
                    strSize = (struct.unpack("i", lenBytes))[0]
                    if fragmentSize + strSize > BULK_IMPORT_FRAGMENT_SIZE:
                        fragmentSize = fragmentSize - 4
                        break
                    elemCount = elemCount + 1
                    fragmentSize = fragmentSize + strSize

            else:
                if size - 1 < BULK_IMPORT_FRAGMENT_SIZE:
                    fragmentSize = size - i
                else:
                    fragmentSize = BULK_IMPORT_FRAGMENT_SIZE;
                fragmentSize = int(fragmentSize / typeSize) * typeSize
                elemCount = int(fragmentSize / typeSize);

            smallBuffer = bytearray()
            smallBuffer = dataBuffer[i:(i+fragmentSize)]
            nullBuffSize = int((elemCount + 8 - 1) /  8)
            if (nullMask == None):
                nullBuffSize = 0

            bulk_import_message = BulkImportMessage_pb2.BulkImportMessage(
                TableName = tableName, ElemCount = elemCount, ColumnName = columnName, ColumnType = serverColumnType, nullMaskLen = nullBuffSize, dataLength = fragmentSize
            )

            send_message(_socket, bulk_import_message)
            _socket.send(smallBuffer)

            if nullBuffSize != 0:
                startOffset = int(i / 8);
                if startOffset == lastNullBuffOffset:
                    startOffset = startOffset + 1
                    nullBuffSize = nullBuffSize - 1
                smallNullBuffer = bytearray()
                smallNullBuffer = nullMask[startOffset:(startOffset + nullBuffSize)]
                _socket.send(smallNullBuffer)

            recv_bytes = read_message(_socket)

            recv_msg = unpack_type(
                recv_bytes,
                InfoMessage_pb2.InfoMessage.DESCRIPTOR,
                InfoMessage_pb2.InfoMessage(),
            )

            if recv_msg == 0:
                # If it's not query response message, we check another possible format of received message
                recv_msg = unpack_type(
                    recv_bytes,
                    InfoMessage_pb2.InfoMessage.DESCRIPTOR,
                    InfoMessage_pb2.InfoMessage(),
                )
                if recv_msg != 0:
                    if recv_msg.Code == InfoMessage_pb2.InfoMessage.StatusCode.OK:
                        logging.info("StatusMessage = OK")
                    else:
                        logging.info(recv_msg)
                        return None
                logging.error("Invalid response from server")
                exit(-1)

            i += fragmentSize

    return

