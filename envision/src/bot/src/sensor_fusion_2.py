#!/usr/bin/env python
import numpy as np
from numpy.linalg import inv
import rospy
from std_msgs.msg import Float64,Time
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3,Pose
from custom_msg.msg import updated_xy

xy_msg =updated_xy()
time_stamp=rospy.Time()
a_x = a_y = w_z = 0.0
seconds=cur_time = dt = prv_time= 0.0
flag=0
[x,y,v_x,v_y,a_x,a_y,v_z]=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
[x_m,y_m]=[0.0,0.0]
noise_ax = 1
noise_ay = 1

I=np.identity(4)
#initial X matrix
X=np.array([[0],
               [0],
               [0],
               [0]])
#initail measurement matrix:
Y=np.array([
    [x_m],
    [y_m]
])
#Q=process noise covariance matrix
Q = np.zeros([4, 4])

#R=measurement_covariance matrix (gps)
R = np.array([
        [noise_ax, 0],
        [0, noise_ay]
        ])

#define H matrix here
H=np.array([
    [1,0,0,0],
    [0,1,0,0]
])
# defining A ,B matrix
def initialization_A_B_P_Q_U(dt,a_x,a_y):
    global Q,A,B,U,P
    P = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0.01, 0],
        [0, 0, 0, 0.01]
        ])
    A = np.array([
            [1.0, 0.0, dt, 0.0],
            [0.0, 1.0, 0.0, dt],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0]
            ])
    B =np.array([
            [0.5*dt*dt,0.0],
            [0.0,0.5*dt*dt],
            [dt,0.0],
            [0.0,dt]])
    U=np.array([[a_x],[a_y]])
    
    #Updating Q matrix
    dt_2 = dt * dt
    dt_3 = dt_2 * dt
    dt_4 = dt_3 * dt

    Q[0][0] = dt_4/4*noise_ax
    Q[0][2] = dt_3/2*noise_ax
    Q[1][1] = dt_4/4*noise_ay
    Q[1][3] = dt_3/2*noise_ay
    Q[2][0] = dt_3/2*noise_ax
    Q[2][2] = dt_2*noise_ax
    Q[3][1] = dt_3/2*noise_ay
    Q[3][3] = dt_2*noise_ay
    
    
def imu_data_collection(msg):
    global a_x,a_y,time_stamp,seconds,Y,dt
    a_x=msg.linear_acceleration.x
    a_y=msg.linear_acceleration.y
    w_z=msg.angular_velocity.z
    time_stamp=msg.header.stamp
    #print('time_stamp:',time_stamp)
    seconds=time_stamp.to_sec()
    #print("senconds new:",seconds)
    time_diff(seconds)
    initialization_A_B_P_Q_U(dt,a_x,a_y)
    predict()
    update(Y)
    
def gps_data_collection(gps_pose):
    global Y
    x_m=gps_pose.position.x
    y_m=gps_pose.position.y
    Y=np.array([
        [x_m],
        [y_m]
    ])
    list_Y=np.array(Y)
    print('measured value:',list_Y)
    
    
def time_diff(seconds):   
    global cur_time,dt,prv_time,flag
    if flag==1:
        pass
    else:
        prv_time=seconds
        flag=1
    cur_time = seconds
    dt = cur_time - prv_time
    prv_time = cur_time
    #print('dt:',dt)

# Predict Step
def predict():
    global X,P,Q,A,B,U
    X = np.matmul(A,X)+np.matmul(B,U)
    list_X=np.array(X)
    print('predicted value:',list_X)
    At = np.transpose(A)
    P = np.add(np.matmul(A, np.matmul(P, At)), Q)

# update step
def update(Y):
    global P,H,X,I,xy_msg
    Ht=np.transpose(H)
    S=np.add(np.matmul(H,np.matmul(P,Ht)),R)
    K=np.matmul(P,Ht)
    Si=inv(S)
    K=np.matmul(K,Si)
    list_k=np.array(K)
    print('Kalman gain:',list_k)
    G=np.subtract(Y,np.matmul(H,X))
    
    #new state
    X=np.add(X,np.matmul(K,G))
    xy_msg.x=X[0][0]
    xy_msg.y=X[1][0]
    pub.publish(xy_msg)
    P=np.matmul(np.subtract(I,np.matmul(K,H)),P)
    list_x=np.array(X)
    print('updated matrix:',list_x)
    
    
pub = rospy.Publisher('/updated_xy_topic',updated_xy,queue_size=50)
gps_data = rospy.Subscriber('/distance',Pose,gps_data_collection)
imu_data = rospy.Subscriber('/imu',Imu,imu_data_collection)

rospy.init_node('rover_nm_node2', anonymous=True)
rospy.spin()
    
