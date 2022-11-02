#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#   exemplo adaptado do livro:
#   
#  Programming Robots with ROS.
#  A Practical Introduction to the Robot Operating System
#  Example 12-5. follower_p.py pag265
#  
#  Referendia PD:https://github.com/martinohanlon/RobotPID/blob/master/mock/mock_robot_pd.py
# 
# Para executar:
#
#       rosrun exemplos222 follower_comportamentos_linha.py
# 
# Em outro terminal:
#
#       rosrun exemplos222 follower_comportamentos_controller.py       

from traitlets import Bool
import rospy
import numpy as np
import math
import cv2
import time
from sensor_msgs.msg import Image, CompressedImage, LaserScan
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError
from tf import transformations
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool

class Follower:

    def __init__(self):
        
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel',
                                             Twist, 
                                             queue_size=1)

        self.linha_sub = rospy.Subscriber('/cmd_vel_linha',
                                             Twist, 
                                             self.velocidade_linha)
        self.ve_linha_sub = rospy.Subscriber('/ve_linha',
                                                 Bool,
                                                 self.ve_linha_cb)

        self.laser_subscriber = rospy.Subscriber('/scan',
                                                  LaserScan, 
	 		                                    self.laser_callback)

        self.odom_subscriber = rospy.Subscriber('/odom',
                                                  Odometry, 
	 		                                    self.odom_callback)
        
        self.twist = Twist()
        self.laser_msg = LaserScan()
        
        # Velocidades comandadas pelos comportamentos 
        self.vel_linha = None

        # Variaveis de controle
        self.angulo = 0

        # Variaveis de estado
        self.ve_linha = False
        self.obstaculo = False
        self.goal = None

        self.hertz = 250
        self.rate = rospy.Rate(self.hertz)

    def velocidade_linha(self, msg):
        self.vel_linha = msg

    def ve_linha_cb(self, msg):
        self.ve_linha = msg.data

    def odom_callback(self, msg):
        quat = msg.pose.pose.orientation
        lista = [quat.x, quat.y, quat.z, quat.w]
        angulos = np.degrees(transformations.euler_from_quaternion(lista))
        self.angulo = angulos[2] # Eixo Z

    def laser_callback(self, msg):
        self.laser_msg = msg
        if msg.ranges[0] < 0.3:
            self.obstaculo = True
        else:
            self.obstaculo = False

    def procura_linha(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.1

    def gira_90(self):

        # Comportamento de giar sentido anti-horário
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.1

        if self.goal is None:
            # Define o ângulo de objetivo
            self.goal = self.angulo + 90
            if self.goal > 180:
                self.goal -= 360
        else:
            # Decide quando para de girar
            diferenca = self.goal - self.angulo
            if diferenca > 180:
                diferenca -= 360
            elif diferenca < -180:
                diferenca += 360
            
            if abs(diferenca) < math.radians(5): # Tolerância de 5 graus
                self.goal = None
                # Manda o robô para frente
                self.twist.linear.x = 0.1
                self.twist.angular.z = 0.0
                
   
    def control(self):
        print(f"Obstaculo: {self.obstaculo}")
        print(f"Goal: {self.goal}")
    
        # Arbitrador do comportamento
        
        # Plano A - Girar tem prioridade 
        if self.obstaculo or self.goal is not None:
            self.gira_90()

        # Plano B
        elif self.ve_linha:
            #self.segue_linha()
            self.twist = self.vel_linha #usa comportamento implementado em outro arquivo

        else:
            self.procura_linha()

        #... Completar o codigo do arbitrador

        ### END CONTROL
        #publica velocidade
        self.cmd_vel_pub.publish(self.twist)
        rospy.loginfo("linear: %f angular: %f", self.twist.linear.x, self.twist.angular.z)
        self.rate.sleep()


# Main loop
if __name__=="__main__":
    rospy.init_node('follower_controller')
    follower = Follower()

    while not rospy.is_shutdown():
        follower.control()

# END ALL
