#!/usr/bin/env python
import time
import roslib; roslib.load_manifest('ur_driver')
import rospy
from trajectory_msgs.msg import *
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy
from std_msgs.msg import String
from math import pi

JOINT_NAMES = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint',
               'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
robot_state = None
pub = None

def joint_states_callback(data):
	#rospy.loginfo("position: %4.3f %4.3f", data.position[0], data.position[1])
    #rospy.loginfo(data.effort)
    robot_state = data
    pass

def handle_joy(data):
    #print(data)
    # A1  B2 X3 Y4
    if data.buttons[2] == 1:
        cmd = "speedl([0.2,0,0,0,0,0], 0.2, 5)"
    elif data.buttons[1] == 1:
        cmd = "speedl([-0.2,0,0,0,0,0], 0.2, 5)"
    elif data.buttons[0] == 1:
        cmd = "speedl([0,0,-0.2,0,0,0], 0.2, 5)"
    elif data.buttons[3] == 1:
        cmd = "speedl([0,0,0.2,0,0,0], 0.2, 5)"
    else:
        cmd = "stopj(2)"
    pub.publish(cmd)
    

def main():
    global robot_state
    global pub
    try:
        rospy.init_node("testJointSpeed", anonymous=True)

        rate = rospy.Rate(10)


        # subscribe joint state
        rospy.Subscriber("/joint_states", JointState, joint_states_callback)
        # setup joy topic subscription
        joy_subscriber = rospy.Subscriber("joy", Joy, handle_joy, queue_size=10)

        # publisher
		
        pub = rospy.Publisher('/ur_driver/URScript', String, queue_size=10)
        #cmd = "movej([0,-1.57,0,-1.57,0,0],a=2.1, v=1, t=0, r=0)"
        #cmd = "movej([-1.509,-1.695,-1.480,-0.849,1.509,0.170],a=2.1, v=1, t=0, r=0)"
        #cmd = "speedl([0.5,0,0,0,0,0], 0.2, 1)"

        while not rospy.is_shutdown():
            #print('loop')
            #pub.publish(cmd)
            rate.sleep()

    except KeyboardInterrupt:
        rospy.signal_shutdown("KeyboardInterrupt")
        raise


if __name__ == '__main__': main()
