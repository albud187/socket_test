#!/usr/bin/env python
#_*_ coding: utf8 _*_

import rospy
import socket
import os
from _thread import *
#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics
TP1 = "TP1"
TP2 = "TP2"
#global variables
ServerSideSocket = socket.socket()
ThreadCount = 0

#constants
HOST = "10.0.0.37"
PORT = 1236

#functions
def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(1024)

        data2print = str(data).split("--")
        print(data2print)

    connection.close()
#data is in form
# "b'0--TOPIC_NAME--MSG"
def parse_data(data):
    data_list = str(data).split("--")
    TOPIC = data_list[1]
    msg = data_list[2]
    pub_dict[TOPIC].publish(msg)

    pass

def C1_server():
    global ThreadCount
    rospy.init_node("C1_server", anonymous = False)

    pub1 = rospy.Publisher(TP1, Vector3, queue_size = 10)
    pub2 = rospy.Publisher(TP2, Vector3, queue_size = 10)
    pub_dict = {TP1:pub1, TP2:pub2}

    try:
        ServerSideSocket.bind((HOST, PORT))
    except socket.error as e:
        print(str(e))
    print('Socket is listening..')
    ServerSideSocket.listen(5)

    while not rospy.is_shutdown():

        Client, address = ServerSideSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        print(Client)
        print(address)
        start_new_thread(multi_threaded_client, (Client, ))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))
    ServerSideSocket.close()

if __name__ == '__main__':
    try:
        C1_server()
    except rospy.ROSInterruptException:
        pass

#main loop
