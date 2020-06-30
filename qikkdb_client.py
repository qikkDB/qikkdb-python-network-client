from qikkdb_connector.connector import create_socket, establish_connection, use_database, query, bulk_import


class qikkdb_client:
    host = "127.0.0.1"
    port = 12345

    def __init__(self, host, port):
        """
        Constructor creating client with defined host and port
        :param host: ip address or host name on which qikkdb listens
        :param port: port on which qikkdb listens
        :return:
        """
        self.host = host
        self.port = port

    def Connect(self):
        """
        Creates connection between connector and databse and start keep_alive thread.
        :return:
        """
        self.socket = create_socket(self.host, self.port)
        self.heartbeat = establish_connection(self.socket)

    def Use(self, database_name):
        """
        Changes databse for executing queries
        :param db_name: name of database from which we will get data
        :return:
        """
        use_database(self.socket, database_name, self.heartbeat)

    def ExecuteQuery(self, query_string):
        """
        Executes query and returns all data
        :param query_string: sql string
        :return: data: list of dictionaries
        """
        data = query(self.socket, query_string, self.heartbeat)
        return data

    def Disconnect(self):
        """
        Closes connection to qikkdb server
        :param query_string: sql string
        :return: data: list of dictionaries
        """
        self.heartbeat.cancel()
        self.socket.close()

    def BulkImport(self, table_name, columns, data):
        """
        Imports native data into database
        :param table_name: name of the table to import data (does not need to exist)
        :param columns: name of columns with types as dictionary (e.g. {'column1': DataType.Int})
        :param data: data in form of list of dictionaries (same as result of ExecuteQuery()) (e.g. [{'column1': 123}])
        :return: data: list of dictionaries
        """
        bulk_import(self.socket, table_name, columns, data)