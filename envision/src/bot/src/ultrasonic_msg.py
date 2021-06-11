#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Range
from custom_msg.msg import ultrasonic_msg

message= ultrasonic_msg()

def s1(msg):
    message.r1=msg.range
def s2(msg):
    message.r2=msg.range
def s3(msg):
    message.r3=msg.range
def s4(msg):
    message.r4=msg.range    
def s5(msg,pub1):
    message.r5=msg.range
    pub1.publish(message)

rospy.init_node('ultrasonic_data', anonymous=True)
pub1 = rospy.Publisher('/ultrasonic_msg_topic', ultrasonic_msg, queue_size=10)	
sub1 = rospy.Subscriber('/bot/ir_front_left2',Range,s1)
sub2 = rospy.Subscriber('/bot/ir_front_left1',Range,s2)
sub3 = rospy.Subscriber('/bot/ir_front_middle',Range,s3)
sub4 = rospy.Subscriber('/bot/ir_front_right1',Range,s4)
sub5 = rospy.Subscriber('/bot/ir_front_right2',Range,s5,pub1)
rospy.spin()
