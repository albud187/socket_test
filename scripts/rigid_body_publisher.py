#!/usr/bin/env python
#_*_ coding: utf8 _*_
import socket
import rospy
import json
#message imports
from geometry_msgs.msg import Vector3

#subscribed topics

#published topics
TP_TGT_POS = "/rigid_body_pos"

#global variables
target_position = Vector3()

#constants
#HOST =  "10.0.0.37"
#HOST = "192.168.152.177"
HOST = "192.168.137.178"

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

def handle_data(key, data_dict):
    global target_position
    target_position.x = data_dict[key][0]
    target_position.y = data_dict[key][1]
    target_position.z = data_dict[key][2]

def print_position_data(key, data_dict):
    print("rigid body -- " + key)
    print("x: " + str(data_dict[key][0]))
    print("y: " + str(data_dict[key][1]))
    print("z: " + str(data_dict[key][2]))
    print(" ")

def multi_object_server():
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
    vect_pub = rospy.Publisher(TP_TGT_POS, Vector3, queue_size = 10)

    while not rospy.is_shutdown():
        #data is a json datastructure
        data = conn.recv(1024).decode()

        try:
            #data_dict is a dictionary converts it into a dictionary
            #keys are strings based on the streaming IDs of the objects
            #values in the updated_data dict are lists of floats
            data_dict = json.loads(data)
            #print(data_dict)
            key1 = "1"
            key2 = "2"
            print_position_data(key1, data_dict)
            print_position_data(key2, data_dict)
            handle_data(key2, data_dict)
            vect_pub.publish(target_position)
        except:
            print("data cannot be covnerted")

        # handle_data(data)
        # print(qc_position)
        # vect_pub.publish(qc_position)



if __name__ == '__main__':
    try:
        multi_object_server()
    except rospy.ROSInterruptException:
        pass

#main loop
