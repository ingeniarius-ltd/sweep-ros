#!/usr/bin/env python
#

import rospy
import serial
import time

time.sleep(6)  #wait for ROS sweep node to start and then do this...

rospy.init_node('test_sweep');

sweep = serial.Serial("/dev/sweep",
                      baudrate = 115200, 
                      parity=serial.PARITY_NONE,  
                      bytesize = serial.EIGHTBITS,
                      stopbits = serial.STOPBITS_ONE,
                      xonxoff = False,
                      rtscts = False,
                      dsrdtr = False)

rospy.loginfo("Scanse Sweep open")
sweep.write("ID\n")
rospy.loginfo("Version requested")

try:
	resp = sweep.readline()
	rospy.loginfo("Response: " + resp)
except:
	rospy.logerr("Could not get version from Sweep. Try again or unplug/plug the USB adapter")



