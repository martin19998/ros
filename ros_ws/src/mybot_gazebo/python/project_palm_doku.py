#Before starting Gazebo this command needs to be active:
gzserver


#Links to build a Robot
http://gazebosim.org/tutorials/?tut=ros_urdf
gazebosim.org/tutorials?tut=ros_gzplugins  #Plugins



#Reset Gazebo world to default
rosservice call /gazebo/reset_world "{}"

#Reset in python script (still needs to be tested):
#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty

rospy.init_node('reset_world')

rospy.wait_for_service('/gazebo/reset_world')
reset_world = rospy.ServiceProxy('/gazebo/reset_world', Empty)

reset_world()

#See more for reset here
https://answers.ros.org/question/266940/reset-model-poses-in-a-python-script/


#Start catvehicle_skidpan.launch
cd catvehicle_ws
source devel/setup.bash
roslaunch catvehicle catvehicle_skidpan.launch config:=front_laser

