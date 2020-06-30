import logging
import struct

from Message import BulkImportMessage_pb2, InfoMessage_pb2
from Message.CSVImportMessage_pb2 import CONST_FLOAT, CONST_DOUBLE, COLUMN_FLOAT
from qikkdb_connector.connector import (RepeatingTimer, create_socket,
                                        establish_connection, query,
                                        use_database, DataType, send_message, read_message, unpack_type, bulk_import)


"""
Main function which calls connector functions needed to get data from server
Python 3.7.x and higher is required! Tested on 3.7.3 and 3.7.4!

:param db_name: Name of database, from which you want to get data
:param query_text: sql expression, according to https://docs.qikk.ly/sql-data-manipulation
:return: returns array of dictionaries, one dictionary is one row in database
"""


def establish_connect(host, port):
    """
    This function create connection between connector and databse and start keep_alive thread.
    :param host: ip address or host name on which qikkdb listens
    :param port: port on which qikkdb listens
    :return: socket and keep_alive reference
    """
    _socket = create_socket(host, port)
    heartbeat = establish_connection(_socket)
    return _socket, heartbeat


def use_db(_socket, db_name, heartbeat):
    """
    This function change databse from which we will get data.
    :param _socket: reference from establish_connection
    :param db_name: name of database from which we will get data
    :param heartbeat: reference from establish_connection
    :return:
    """
    use_database(_socket, db_name, heartbeat)


def get_dataset(_socket, query_text, heartbeat):
    """
    Function for downloading data from database.
    :param _socket: reference from establish_connection
    :param query_text: sql string
    :param heartbeat: reference from establish_connection
    :return: downloaded data
    """
    dataset = query(_socket, query_text, heartbeat)

    return dataset


def close_connection(_socket, heartbeat):
    """
    Function which ends connection with database
    :param _socket: reference from establish_connection
    :param heartbeat: reference from establish_connection
    :return:
    """
    heartbeat.cancel()
    _socket.close()


# Internal testing:#
# q = "show tables;"

q = "select longitude, latitude from T_default1 limit 10;"
hb = 0
socket = 0
#while 1:
#     t = input("pre koniec stlac q, e = establish, u = use, g = getdataset\n")
#     if t is "q":
#         if socket:
#             close_connection(socket, hb)
#         if hb:
#             hb.cancel()
#         exit(0)
#     elif t is "e":
#         socket, hb = establish_connect("127.0.0.1", 12345)
#     elif t is "u":
#         use_db(socket, "test", hb)
#         u = True
#     elif t is "g":
#         result = get_dataset(socket, q, hb)
#         for i in result:
#             print(i)
#         print(result[0].keys())
