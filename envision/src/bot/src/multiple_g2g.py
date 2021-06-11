#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from custom_msg.msg import lat_long_msg
lat_long_msg_1=lat_long_msg()
flag=0
lat=[21.164217,21.164413,21.164551]
lon=[72.784355,72.784371,72.784552]
def flag_callback(msg):
    global flag
    flag=msg.data
    print("flag=",flag)
    for i in range(3):
        if flag==i:
            lat_long_msg_1.lat=lat[i]
            lat_long_msg_1.long=lon[i]
            print("-->current goal no:",flag+1)
        else:
            pass
    lat_long_pub.publish(lat_long_msg_1)    
rospy.init_node('multiple_goal_g2g_node', anonymous=True)
lat_long_pub = rospy.Publisher('/Multiple_goal_lat_long_topic', lat_long_msg, latch=True,queue_size=10)
flag_sub = rospy.Subscriber('/flag_topic_for_mutilple_goal', Int32,flag_callback)
rospy.spin()
