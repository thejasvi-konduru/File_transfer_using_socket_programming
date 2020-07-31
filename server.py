import socket
import threading
import os
import time

HEADER=1024
port=5050
FORMAT='utf-8'
host=socket.gethostbyname(socket.gethostname())
#The above statements returns the IP address
#socket.gethostname() returns the name of the host
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#creates a socket object
addr=(host,port)
server.bind(addr)
#bind() is used to associate the socket with a specific network interface and port number
def handle_client(conn, addr):
    print(f"NEW CONNECTION:- {addr} connected.")
    data=conn.recv(HEADER).decode(FORMAT)
    print(data)
    if not os.path.exists(data):
        conn.send("file-doesn't-exist".encode())
    else:
        conn.send("file-exists".encode())
        print("sending data..")
        with open(data, "rb") as f:
            data = f.read(1024)
            while data != b"":
                conn.send(data)
                data = f.read(1024)
    f.close()
    conn.close()
        
def start():
    server.listen()
    while True:
        conn,addr=server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()

print("server is starting....")
start()