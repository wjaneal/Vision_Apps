from Mathfunctions import *

#Pi is always handy:
PI = 4*atan(1)

#Set up number of pixels of each webcam in the X and Y directions
C1X = 640
C1Y = 480
C2X = 640
C2Y = 480

#Set up cameras centred about (0,0,0)
d1 = -1.0 #X axis location of camera 1
d2 = 1.0 #X axis location of camera 2
theta1 = 45.1 #Towards + x-axis
theta2 = +45.0 #Towards - x-axis
alpha = 10.0 #Lateral spread angle of camera field of view
beta = 8.0
#Determine the slopes, in degrees, of the lines representing the lateral edges of each
#camera's field of view

line_1_m_left = 90.0+theta1+alpha
line_1_m_right = 90.0+theta1-alpha
line_2_m_left = 90.0+theta2+alpha
line_2_m_right = 90.0-theta2+alpha

#Determine equations for each line at the edges of the camera's field of view

m1x = sin(PI*(90-theta1)/180)
m1y = cos(PI*(90-theta1)/180)
m2x = sin(PI*(90-theta2)/180)
m2y = cos(PI*(90-theta2)/180)
print m1x, m1y, m2x,m2y, 'Slopes'
P01 = [d1,0.0,0.0]
P02 = [d2,0.0,0.0]
m1 = [m1x,m1y,0.0]
m2 = [m2x,m2y,0.0]
l1 = Line_3D(P01,m1)
l2 = Line_3D(P02,m2)
print l1.P0, l1.m, l2.P0, l2.m, "Testing 2" 
print Line_Intersection_2D(l1,l2), '2D'
print Line_Intersection_3D(l1,l2), '3D'


