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
sum=0
min_r=0
vel_msg = Twist()
def f1(msg,pub):
	global r,sum
	r[0]=msg.r1
	r[1]=msg.r2
	r[2]=msg.r3
	r[3]=msg.r4
	r[4]=msg.r5
	sum=-(2*msg.r1)-(1*msg.r2)+(0*msg.r3)+(1*msg.r4)+(2*msg.r5)
	min_r=min(r)
	ob_avoid(pub)

# def forward():
# 	vel_msg.linear.x = 0.7
# 	vel_msg.angular.z = 0
# def stop():
# 	vel_msg.linear.x = 0
# 	vel_msg.angular.z = 0
# def backward():
# 	vel_msg.linear.x = -0.7
# 	vel_msg.angular.z = 0
# def backward_right():
# 	vel_msg.linear.x = -0.2
# 	vel_msg.angular.z = -0.2
# def sharp_right_turn(): 
# 	vel_msg.linear.x = 0
# 	vel_msg.angular.z = -0.5
	
# def sharp_left_turn():
# 	vel_msg.linear.x = 0
# 	vel_msg.angular.z = 0.5

# def soft_right_turn(): 
# 	vel_msg.linear.x = 0.4
# 	vel_msg.angular.z = -0.4
	
# def soft_left_turn():
# 	vel_msg.linear.x = 0.4
# 	vel_msg.angular.z = 0.4

def ob_avoid(pub):
	global sum,r,min_r
	if min_r<1:
		sum=sum/15
	elif min_r>1 and min_r<2:
		sum=sum/20
	elif min_r>2 and min_r<3:
		sum=sum/15
	elif min_r>3 and min_r<4:
		sum=sum/30
	else:
		sum=sum/35
	vel_msg.linear.x = (1-abs(sum))/2
	vel_msg.angular.z = -sum
	
		
	# if abs(sum)==0:
	# 	# forward()
	# 	# message.flag=1
	# 	print("...going forward")			
	# elif sum>0 and sum <=7.5:
	# 	# soft_right_turn()
	# 	#message.flag=0
	# 	print("...soft right turn")
	# elif sum <0 and sum >=-7.5:
	# 	soft_left_turn()
	# 	#message.flag=0
	# 	print("...soft left turn")
	# elif sum>7.5:
	# 	sharp_right_turn()
	# 	#message.flag=0
	# 	print("...sharp right turn")
	# elif sum<-7.5:
	# 	sharp_left_turn()
	# 	#message.flag=0
	# 	print("...sharp left turn")
	# elif abs(sum)<3 and r[2]<1:
	# 	stop()
	# 	print("...stop:")
	# else:
	# 	pass	
	# 	print("pass")	
	pub.publish(vel_msg)
print("hii")
rospy.init_node('ob_avoid_using_pid1', anonymous=True)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=50)	
ultrasonic_msg_sub = rospy.Subscriber('/ultrasonic_msg_topic',ultrasonic_msg,f1,pub)
rospy.spin()


