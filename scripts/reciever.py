#!/usr/bin/env python
#_*_ coding: utf8 _*_
import socket
import rospy

#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics

#global variables
qc_position = Vector3()

#constants
IP_INFO_FILE = "IP_DATA_RECIEVER.txt"

def get_IP_info(filename):
    with open(filename) as f:
        lines = f.readlines()

    result_dict ={"HOST":lines[0].strip(), "PORT":int(lines[1].strip())}

    return result_dict

IP_INFO = get_IP_info(IP_INFO_FILE)
HOST = IP_INFO["HOST"]
PORT = IP_INFO["PORT"]

def reciever_node():

    print(socket.gethostname())
    mySocket = socket.socket()
    mySocket.bind((HOST,PORT))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("connection from: " + str(addr))

    rospy.init_node("server_node", anonymous = False)

    #subscribers

    #publishers

    while not rospy.is_shutdown():
        data = conn.recv(1024).decode()
        print(data)
        print(" ")

if __name__ == '__main__':
    try:
        reciever_node()
    except rospy.ROSInterruptException:
        pass

#main loop
