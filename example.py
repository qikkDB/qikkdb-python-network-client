from qikkdb_client import qikkdb_client
from ast import literal_eval

from qikkdb_connector.connector import DataType

f = open('test_data_bulk_import/test_mixed.txt', 'r')
fileContent = f.read()
import_data = literal_eval(fileContent)

host = "127.0.0.1"
port = 12345

client = qikkdb_client(host, port)
client.Connect()

client.Use("default_db")
data = client.ExecuteQuery("SELECT * FROM T_default1 LIMIT 10;")
print(data)
#f = open('test_result.txt', 'w' )
#f.write(repr(data));
#f.close()

#client.BulkImport( "py_mixed", {'longitude': DataType.Float, 'latitude': DataType.Float, 'age':DataType.Int, 'eventDate':DataType.Int64, 'minutesDuration':DataType.Int, 'targetId':DataType.Int}, import_data)
#client.BulkImport( "py_float", {'longitude': DataType.Float, 'latitude': DataType.Float}, import_data)
#client.BulkImport( "py_string", {'eventType': DataType.String}, import_data)
#client.BulkImport( "py_point", {'dropoff_coord': DataType.Point}, import_data)
#client.BulkImport( "py_polygon", {'polygon': DataType.Polygon}, import_data)

#import_data = [{'longitude': 18.78696632385254, 'latitude': 49.1927375793457}, {'longitude': 18.078866958618164, 'latitude': None}, {'longitude': 18.735143661499023, 'latitude': 49.19744873046875}]
#import_columns = {'longitude': DataType.Float, 'latitude': DataType.Float}
#client.BulkImport( "py_import", import_columns, import_data)

client.Disconnect()


