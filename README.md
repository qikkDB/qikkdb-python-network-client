# Python connector to QikkDB database

**qikkdb_client.py:** class containing functions necessary to establish connection and get the data

**example.py:** sample usage of qikkdb_client.py

## Usage

### Creating connection
```
from qikkdb_client import qikkdb_client
client = qikkdb_client("127.0.0.1", 12345)
client.Connect()
```

### Switching database
```
client.Use("test")
```

### Querying
```
data = client.ExecuteQuery("SELECT longitude, latitude from T_default1;")
```

### Bulk import
```
import_data = [{'longitude': 18.78696632385254, 'latitude': 49.1927375793457}, {'longitude': 18.078866958618164, 'latitude': None}, {'longitude': 18.735143661499023, 'latitude': 49.19744873046875}]
import_columns = {'longitude': DataType.Float, 'latitude': DataType.Float}
client.BulkImport( "py_import", import_columns, import_data)
```

### Disconnecting
```
client.Disconnect()
```

## Generating Protobuf classes

```
protoc --proto_path=. --python_out=. Message/InfoMessage.proto Message/QueryMessage.proto Message/QueryResponseMessage.proto Message/SetDatabaseMessage.proto Message/BulkImportMessage.proto Message/CSVImportMessage.proto Types/ComplexPolygon.proto Types/Point.proto
```
