#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range
from custom_msg.msg import ultrasonic_msg
#from custom_msg.msg import obavoid_flag_x_z
# message = obavoid_flag_x_z()
# [r1,r2,r3]=[0.0,0.0,0.0]
r=[0,0,0,0,0]
sum_r=0
#min_r=0
vel_msg = Twist()
def f1(msg,pub):
	global r,sum_r
	# k=2.5
	r[0]=msg.r1
	# r[0]=-(2-(k-r[0]))*r[0]
	r[1]=msg.r2
	# r[1]=-(1-(k-r[1]))*r[1]
	r[2]=msg.r3
	# r[2]=-(0-(k-r[2]))*r[2]
	r[3]=msg.r4
	# r[3]=(1-(k-r[3]))*r[3]
	r[4]=msg.r5
	# r[4]=(2-(k-r[4]))*r[4]
	sum_abs_r=abs(sum(r))
	sum_1=-(2*msg.r1)-(1*msg.r2)+(0*msg.r3)+(1*msg.r4)+(2*msg.r5)
	g=sum_1/sum_abs_r
	print("sum_r",g)
	vel_msg.linear.x = (1-abs(g))/1.5
	vel_msg.angular.z = -g	
	pub.publish(vel_msg)



	


print("hii")
rospy.init_node('ob_avoid_using_pid1', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=50)	
ultrasonic_msg_sub = rospy.Subscriber('/ultrasonic_msg_topic',ultrasonic_msg,f1,pub)
rospy.spin()


