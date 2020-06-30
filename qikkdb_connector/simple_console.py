from qikkdb_connector.get_dataset import close_connection, establish_connect, use_db, get_dataset

host = "127.0.0.1"
port = 12345
q = "select longitude, latitude from T_default1 limit 10;"
hb = 0
socket = 0
while 1:
     t = input("pre koniec stlac q, e = establish, u = use, g = getdataset\n")
     if t == "q":
         if socket:
             close_connection(socket, hb)
         if hb:
             hb.cancel()
         exit(0)
     elif t == "e":
         socket, hb = establish_connect(host, port)
     elif t == "u":
         use_db(socket, "test", hb)
         u = True
     elif t == "g":
         result = get_dataset(socket, q, hb)
         for i in result:
             print(i)
         print(result[0].keys())