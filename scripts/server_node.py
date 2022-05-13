#!/usr/bin/env python
#_*_ coding: utf8 _*_
import socket
import rospy

#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics
TP_QC_PTN = "/cmd_vel"

#global variables
qc_position = Vector3()

def Main():
    host = "10.0.0.37"
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

Main()

#main loop
