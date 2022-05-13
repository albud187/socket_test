#!/usr/bin/env python
#_*_ coding: utf8 _*_

import socket
def Main():
        host = "127.0.0.1"
        port = 5000

        mySocket = socket.socket()
        mySocket.connect((host,port))

        message = input(" -> ")

        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()

                print ('Received from server: ' + data)

                message = input(" -> ")

        mySocket.close()

Main()
