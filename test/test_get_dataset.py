import socket
import unittest

from qikkdb_connector.connector import create_socket, use_database
from qikkdb_connector.get_dataset import (close_connection, establish_connect,
                                          get_dataset, use_db)


class TestGetDataset(unittest.TestCase):
    def test_dataset_size(self):
        soc, hb = establish_connect()
        use_db(soc, "test", hb)
        dataset = get_dataset(soc, "select * from trips limit 50;", hb)
        close_connection(soc, hb)
        self.assertEqual(len(dataset), 50)

    def test_dataset_keys(self):
        soc, hb = establish_connect()
        use_db(soc, "test", hb)
        dataset = get_dataset(soc, "select * from trips limit 50;", hb)
        close_connection(soc, hb)
        self.assertEqual(len(dataset[0].keys()), 7)

    def test_socket_creation(self):
        soc, hb = establish_connect()
        close_connection(soc, hb)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.assertEqual(soc.family, s.family)
        self.assertEqual(soc.type, s.type)

    # if inserted bad server IP
    def test_socket_error(self):
        self.assertRaises(socket.gaierror, create_socket())

    # testing use_database when calls use before establish
    def test_use_database(self):
        soc = 0
        hb = 0
        self.assertRaises(AttributeError, use_database(soc, "test", hb))


if __name__ == "__main__":
    unittest.main()
