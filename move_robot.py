#! /usr/bin/env/python

import rospy
from geometry_msgs import twist

import rospy
from geometry_msgs.msg import Twist # import twist message from geometry_msgs package

rospy.init_node('move_robot_node')  # initiate a node named 'move_robot_node'
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # Create a Publisher object, that will publish on the /cmd_vel topic

rate = rospy.Rate(2)    # Set a publish rate of 2 Hz
move = Twist()
move.linear.x = 0.5 #Move the robot with a linear velocity in the x axis
move.angular.z = 0.5 #Move the with an angular velocity in the z axis

while not rospy.is_shutdown():    # Create a loop that will go until someone stops the program execution
  pub.publish(move)         # Publish the message within the 'Move' var
  rate.sleep()              # Make sure the publish rate maintains at 2 Hz