#!/usr/bin/env python
#_*_ coding: utf8 _*_
import socket
import rospy

#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics

#global variables

#constants

HOST = "10.0.0.37"
PORT = 1236

def C1_server():

    print(socket.gethostname())
    mySocket = socket.socket()
    mySocket.bind((HOST,PORT))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    rospy.init_node("C1_server", anonymous = False)

    while not rospy.is_shutdown():

        data = conn.recv(1024).decode()
        print(data)
    conn.close()

if __name__ == '__main__':
    try:
        C1_server()
    except rospy.ROSInterruptException:
        pass

#main loop
