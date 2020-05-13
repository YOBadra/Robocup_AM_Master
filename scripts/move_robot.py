#!/usr/bin/python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import <eposx_hardware/epos_hardware.h>
import sys

def pose_callback(pose):
    global robot_x
    robot_x = pose.x
    rospy.loginfo("Robot position = %f/n", pose.x)
    rospy.loginfo("Robot position = %f/n", pose.y)
    rospy.loginfo("Robot position = %f/n", pose.z)

def move_turtle(lin_vel,ang_vel,distance):
    global robot_x
    rospy.init_node('move_robot1', anonymous= False)
    pub = rospy.Publisher('/robot1/cmd_vel',Twist,queue_size=1)
    rospy.Subscriber('/robot1/pose',Pose, pose_callback) 

def move_robot1():
    rospy.init_node('move_robot1',anonymous=False)
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
    vel = Twist()
    vel.linear.x = 2.0

    tStart = rospy.Time.now
    rate =rospy.Rate(10)
    For the next 6 seconds publish vel move commands to Turtlesim
    while rospy.Time.now() < tStart + rospy.Duration(secs=6):
        pub.publish(vel)# publish velocity command to Turtlesim
        rate.sleep()

if __name__ == '__main__':
    try:
        move_robot1()
    except rospy.ROSInterruptException:
        pass