#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import time

# to be able to subcribe to laser scanner data
from sensor_msgs.msg import LaserScan


class SimpleListening():
    '''
    Class blablabla
    '''
    def __init__(self):
        '''
        Class constructor: will get executed at the moment
         of object creation
        '''
        # register node in ROS network
        rospy.init_node('stationary_sensor', anonymous=False)
        # print message in terminal
        rospy.loginfo('Stationary sensor is active!')
        # subscribe to pioneer laser scanner topic
        rospy.Subscriber("/front/scan", LaserScan, self.laserCallback)
        # setup publisher to later on move the pioneer base
        self.pub_stat_data = rospy.Publisher('/stat/detect_msg', String, queue_size=1)
	# initialize distance value
	self.distance = 10.0


    def laserCallback(self, msg):
        '''
        Processes the laserdata and sets smallerst distance value
        '''
        self.distance = min(msg.ranges)
	print(self.distance)


    def send_message(self):
        '''
        Processes the laserdata
        '''
        if self.distance < 2:
            # time.sleep(5)
            test = "Warning!"
            # print("Fehler: " + type(self.pub_state_data))
            rospy.loginfo(test)
            self.pub_stat_data.publish(test)
            rospy.sleep(0.1) 


    def run_sensor(self):
        '''
        The sensor is active and ready to publish data.
        '''
        while not rospy.is_shutdown():
            self.send_message()
            #test = "Warning!"
            #rospy.loginfo(test)
            #self.pub_stat_data.publish("HALLO")
            #rospy.sleep(0.1) 
 



if __name__ == '__main__':
    my_sensor = SimpleListening()
    try:
        my_sensor.run_sensor()
    except rospy.ROSInterruptException:
        pass
