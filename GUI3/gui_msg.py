#!/usr/bin/env python
import rospy
from custom_msg.msg import obavoid_flag_x_z
from std_msgs.msg import Float64
from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Imu
from sensor_msgs.msg import NavSatFix
from custom_msg.msg import g2g_x_z
from custom_msg.msg import gui_msg

gui_message = gui_msg()

def fnc_to_decide_oba_or_g2g(data):
    gui_message.flag_ob_avoid_or_g2g = data.flag
    # if self.flag_ob_avoid_or_g2g==1:
    #     self.G2G_label.setStyleSheet("background-color: rgb(117, 80, 123);")
    #     self.obstacle_aboidance_label.setStyleSheet("background-color: rgb(238, 238, 236);")
    # else:
    #     self.G2G_label.setStyleSheet("background-color: rgb(238, 238, 236);")
    #     self.obstacle_aboidance_label.setStyleSheet("background-color: rgb(117, 80, 123);")

def distace_callback_fnc(harsh):
    gui_message.distance=harsh.data
    # self.distance_to_goal_label.setText(str(self.distance))
    # print(".....distance_callback")

def flag_callback(harsh):
    gui_message.goal_no=harsh.data +1
    # print("goal no.:",self.goal_no)
    # if self.goal_no < (self.n +1):
    #     self.current_goal_no_label.setText(str(self.goal_no))
    # else:
    #     pass

def cmd_vel_msg_print_callback(msg):
    gui_message.linear_velocity_cmd_vel=msg.linear.x
    gui_message.angular_velocity_cmd_vel=msg.angular.z
    # self.cmd_vel_x_label.setText(str(self.linear_velocity_cmd_vel))
    # self.cmd_vel_angular_label.setText(str(self.angular_velocity_cmd_vel))

def imu_callback(msg):
    gui_message.imu_a_x= msg.linear_acceleration.x
    gui_message.imu_a_y=msg.linear_acceleration.y
    gui_message.imu_a_z=msg.linear_acceleration.z
    gui_message.imu_w_x=msg.angular_velocity.x
    gui_message.imu_w_y=msg.angular_velocity.y
    gui_message.imu_w_z=msg.angular_velocity.z
    # self.x_imu_linear_label.setText(str(self.imu_a_x))
    # self.y_imu_linear_label.setText(str(self.imu_a_y))
    # self.z_imu_linear_label.setText(str(self.imu_a_z))
    # self.x_imu_angular_label.setText(str(self.imu_w_x))
    # self.y_imu_angular_label_2.setText(str(self.imu_w_y))
    # self.z_imu_angular_label_3.setText(str(self.imu_w_z))

def current_location(msg):
    
    gui_message.gps_lat=msg.latitude
    gui_message.gps_lon=msg.longitude
    # self.lat_label.setText(str(self.gps_lat))
    # self.long_label.setText(str(self.gps_lon))

def location_in_x_y(msg):
    gui_message.location_x=msg.x
    gui_message.location_y=msg.z
    gui_msg_pub.publish(gui_message)
    # self.x_location_label.setText(str(self.location_x))
    # self.Y_loacation_label.setText(str(self.location_y))  

rospy.init_node('g2g_x_z', anonymous=True)
obavoid_sub = rospy.Subscriber('/obavoid_flag_x_z_topic',obavoid_flag_x_z ,fnc_to_decide_oba_or_g2g)
distance_sub = rospy.Subscriber('/distance_to_goal_topic', Float64,distace_callback_fnc)
flag_sub = rospy.Subscriber('/flag_topic_for_mutilple_goal', Int32,flag_callback)
cmd_vel_sub=rospy.Subscriber('/cmd_vel',Twist,cmd_vel_msg_print_callback)
imu_sub=rospy.Subscriber("/imu/data",Imu,imu_callback)
gps_sub=rospy.Subscriber('/gps_fix',NavSatFix,current_location)
location_x_y=rospy.Subscriber('/location_in_x_y',g2g_x_z,location_in_x_y)
gui_msg_pub = rospy.Publisher('/gui_msg_topic', gui_msg,latch=True,queue_size=10)
rospy.spin()