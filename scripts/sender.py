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
IP_INFO_FILE = "IP_DATA_SENDER.txt"

def get_IP_info(filename):
    with open(filename) as f:
        lines = f.readlines()

    result_dict ={"HOST":lines[0].strip(), "PORT":int(lines[1].strip())}

    return result_dict

IP_INFO = get_IP_info(IP_INFO_FILE)
HOST = IP_INFO["HOST"]
PORT = IP_INFO["PORT"]

def sender_node():
    print(socket.gethostname())
    mySocket = socket.socket()
    mySocket.connect((HOST,PORT))
    mySocket.listen(100)
    conn, addr = mySocket.accept()
    print("connection from: " + str(addr))

    rospy.init_node("server_node", anonymous = False)

    message = input(" -> ")
    while not rospy.is_shutdown():

        mySocket.send(message.encode())
        message = input(" -> ")



if __name__ == '__main__':
    try:
        sender_node()
    except rospy.ROSInterruptException:
        pass

#main loop
