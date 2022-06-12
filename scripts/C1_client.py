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

HOST = "10.0.0.221"
PORT = 1236

def C1_client():
    rospy.init_node("C1_client", anonymous = False)
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((HOST,PORT))

    message = input(" -> ")


    
    while not rospy.is_shutdown():

        mySocket.send(message.encode())

        message = input(" -> ")



if __name__ == '__main__':
    try:
        C1_client()
    except rospy.ROSInterruptException:
        pass

#main loop
