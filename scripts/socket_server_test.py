#!/usr/bin/env python
#_*_ coding: utf8 _*_
#server should be on linux machine to get info from optitrack
import socket

def Main():
    host = "127.0.0.1"
    port = 1236

    print(socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))

            data = str(data).upper() + " from server999"
            print ("sending: " + str(data))
            conn.send(data.encode())

    conn.close()

# if __name__ == '__main__':
#     Main()
Main()
