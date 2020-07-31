import socket
import time
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
host=socket.gethostbyname(socket.gethostname())
ADDR = (host, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    client.send(msg.encode(FORMAT))
    with open('received_file','wb') as f:
        print('file opened')
        while True:
            print("receiving data...")
            data=client.recv(1024)
            print((data.decode(FORMAT)))
            if data == b"":
                break
            f.write(data)
    f.close()
    print("successfully get the file")
    client.close()
    print("connection closed")

send("hello.txt")