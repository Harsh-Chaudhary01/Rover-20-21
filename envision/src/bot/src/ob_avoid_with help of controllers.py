#!/usr/bin/env python
import sys, select, termios, tty
import rospy
from std_msgs.msg import Float64

def getKey(key_timeout):
	settings = termios.tcgetattr(sys.stdin)
	tty.setraw(sys.stdin.fileno())
	rlist, _, _ = select.select([sys.stdin], [], [], key_timeout)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key
def forward() :
	global var1,var2,var3,var4,var5,var6
	[var1,var2,var3,var4,var5,var6]=[1000,1000,1000,1000,1000,1000]
def right_turn():
	global var1,var2,var3,var4,var5,var6
	[var1,var2,var3,var4,var5,var6]=[1000,0,1000,0,1000,0]
def left_turn():
	global var1,var2,var3,var4,var5,var6
	[var1,var2,var3,var4,var5,var6]=[0,1000,0,500,0,1000]
def stop():
	global var1,var2,var3,var4,var5,var6
	[var1,var2,var3,var4,var5,var6]=[0,0,0,0,0,0]
def key_pressing_logic():

	gk1 = getKey(10)
	if gk1 == "f" :
		print("f pressed")
		forward()
	if gk1 == "r" :
		print("r pressed")
		right_turn()
	if gk1 == "l" :
		print("l pressed")
		left_turn()
	if gk1 == "s" :
		print("s pressed")
		stop()

rospy.init_node('node1')
pub1 = rospy.Publisher('/rover_nm/joint1_position_controller/command',Float64,queue_size =50)
pub2 = rospy.Publisher('/rover_nm/joint2_position_controller/command',Float64,queue_size =50)
pub3 = rospy.Publisher('/rover_nm/joint3_position_controller/command',Float64,queue_size =50)
pub4 = rospy.Publisher('/rover_nm/joint4_position_controller/command',Float64,queue_size =50)
pub5 = rospy.Publisher('/rover_nm/joint5_position_controller/command',Float64,queue_size =50)
pub6 = rospy.Publisher('/rover_nm/joint6_position_controller/command',Float64,queue_size =50)
rate = rospy.Rate(100)
[var1,var2,var3,var4,var5,var6]=[0,0,0,0,0,0]

while not rospy.is_shutdown():
	key_pressing_logic()
	pub1.publish(var1)
	pub2.publish(var2)
	pub3.publish(var3)
	pub4.publish(var4)
	pub5.publish(var5)
	pub6.publish(var6)
	rate.sleep()
