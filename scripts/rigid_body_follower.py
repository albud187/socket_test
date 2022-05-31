#!/usr/bin/env python

#package imports
import rospy
import numpy as np

#message imports
from geometry_msgs.msg import Twist, Vector3
from nav_msgs.msg import Odometry
#subscribed topics
TS_TGT_POS = "/rigid_body_pos"
TS_QC_STATE = "/ground_truth/state"


#published topics
TP_CMDVEL = "/cmd_vel"

#global variables
qc_position = Vector3()
target_position = Vector3()
cmd_vel = Twist()

#constants
HARD_DECK = 0.5
DELTA = 0.1
Kv = 1.2
#functions
def handle_position_state(msg):
    global qc_position
    qc_position.x = msg.pose.pose.position.x
    qc_position.y = msg.pose.pose.position.y
    qc_position.z = msg.pose.pose.position.z
    print("999")

def handle_target_position(msg):
    global target_position
    target_position = msg
    target_position.z = target_position.z + HARD_DECK

def velocity_control():
    global cmd_vel
    distance = np.sqrt((target_position.x- qc_position.x)**2 + (target_position.y - qc_position.y)**2 +(target_position.z- qc_position.z)**2 )
    if abs(distance) > DELTA:
        cmd_vel.linear.x = Kv*(target_position.x - qc_position.x)
        cmd_vel.linear.y = Kv*(target_position.y - qc_position.y)
        cmd_vel.linear.z = Kv*(target_position.z - qc_position.z)
    else:
        cmd_vel.linear.x = 0
        cmd_vel.linear.y = 0
        cmd_vel.linear.z = 0

#main loop
def rigid_body_follower():
    #globals
    global cmd_vel

    #init
    rospy.init_node("rigid_body_follower", anonymous = False)
    rate = rospy.Rate(120)
    #subscribers
    rospy.Subscriber(TS_QC_STATE , Odometry, handle_position_state)
    rospy.Subscriber(TS_TGT_POS, Vector3, handle_target_position)
    #publishers
    vel_pub = rospy.Publisher(TP_CMDVEL, Twist, queue_size = 10)

    while not rospy.is_shutdown():
        velocity_control()
        vel_pub.publish(cmd_vel)
        print(qc_position)
        print("")
        rate.sleep()

    rospy.spin()

if __name__ =='__main__':
    try:
        rigid_body_follower()
    except rospy.ROSInterruptException:
        pass
