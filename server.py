import socket
from _thread import *

serever = "192.168.122.1"
port = 2012

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((serever, port))
except socket.error as e:
    str(e)

s.listen(2)
print("wating fo a conection, server started")

def threaded_cilent(conn):
    conn.send(str.encode("conected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("recived:",reply)
                print("sending:",reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("lost conection!")
    conn.close()

while True:
        conn, addr = s.accept()
        print("connected to:", addr)

        start_new_thread(threaded_cilent, (conn,))
