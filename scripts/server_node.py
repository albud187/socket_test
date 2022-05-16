#!/usr/bin/env python
#_*_ coding: utf8 _*_
import socket
import rospy

#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics
TP_QC_PTN = "/pos_vect"

#global variables
qc_position = Vector3()

#constants
#HOST =  "10.0.0.37"
HOST = "192.168.152.177"
PORT = 1236


def Main():
    global mySocket
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

def handle_data(input_data):
    global qc_position
    vector_data = input_data.split(",")
    qc_position.x = float(vector_data[0])
    qc_position.y = float(vector_data[1])
    qc_position.z = float(vector_data[2])

def server_node():
    global qc_position
    print(socket.gethostname())
    mySocket = socket.socket()
    mySocket.bind((HOST,PORT))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print("connection from: " + str(addr))

    rospy.init_node("server_node", anonymous = False)

    #subscribers

    #publishers
    vect_pub = rospy.Publisher(TP_QC_PTN, Vector3, queue_size = 10)

    while not rospy.is_shutdown():
        data = conn.recv(1024).decode()
        handle_data(data)
        print(qc_position)
        vect_pub.publish(qc_position)


if __name__ == '__main__':
    try:
        server_node()
    except rospy.ROSInterruptException:
        pass

#main loop
