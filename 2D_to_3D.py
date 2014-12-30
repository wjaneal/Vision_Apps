from Mathfunctions import *

#Set up number of pixels of each webcam in the X and Y directions
C1X = 640
C1Y = 480
C2X = 640
C2Y = 480

#Set up cameras centred about (0,0,0)
d1 = -1.0 #X axis location of camera 1
d2 = 1.0 #X axis location of camera 2
theta1 = -45.0 #Towards + x-axis
theta2 = +45.0 #Towards - x-axis
alpha = 10.0 #Lateral spread angle of camera field of view

#Determine the slopes, in degrees, of the lines representing the lateral edges of each
#camera's field of view

line_1_m_left = 90.0+theta1+alpha
line_1_m_right = 90.0+theta1-alpha
line_2_m_left = 90.0+theta2+alpha
line_2_m_right = 90.0-theta2+alpha

#Determine equations for each line at the edges of the camera's field of view


