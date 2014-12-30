from math import *

#Define a Vector as a List of numbers of length 3
#Example: u = [2,3,1] and v=[3,-6,-7]
#Vectors are often defined as classes in Python.  For now, we will stick to lists....

def vector_sum(u,v):
	return[u[0]+v[0], u[1]+v[1], u[2]+v[2]]

def vector_diff(u,v):
	return[u[0]-v[0], u[1]-v[1], u[2]-v[2]]

def scalar_mult(c,u):
	return[c*u[0],c*u[1],c*u[2]]

def dot_product(u,v):
	return u[0]*v[0]+u[1]*v[1]+u[2]*v[2]

def cross_product(u,v):
	return [u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0]]

def magnitude(u):
	return (u[0]*u[0]+u[1]*u[1]+u[2]*u[2])**0.5

def unit_vector(u):
	m=magnitude(u)
	return scalar_mult(1.0/m, u)

def projection(u,v):
	#Projection of u onto v:
	mag = dot_product(u,v)/dot_product(u,u)
	return mag*unit_vector(v)

def Line_Intersection_3D(l1, l2):
	m1 = l1.P0[0]
	m2 = l1.P0[1]
	m3 = l1.P0[2]
	n1 = l2.P0[0]
	n2 = l2.P0[1]
	n3 = l2.P0[2]
	x1 = l1.m[0]
	y1 = l1.m[1]
	z1 = l1.m[2]
	x2 = l2.m[0]
	y2 = l2.m[1]
	z2 = l2.m[2]
	#Takes two lines of type Line_3D and returns their point of intersection, if any, returning false otherwise
	l1 = (m1*(y2-y1)-m2*(x2-x1))/(m2*n1-m1*n2)
	l2 = (m2*(z2-z1)-m3*(y2-y1))/(m3*n2-m2*n3)	
	l3 = (m1*(z2-z1)-m3*(x2-x1))/(m3*n1-m1*n3)
	#For now, return l1, l2 and l3 and the approximate point of convergence as determined by l1- if they are similar, then the lines approximately have a point of convergence
	#The program can determine if all three ls are sufficiently similar to declare a convergence.
	return[l1,l2,l3, vector_sum(l2.P0, scalar_mult(l1, l2.m))]

class Line_3D:
	def __init__(self, P0, m):
		#Initialize with a 3D vector for the initial point and a 3D vector for the slopw
		self.P0 = P0
		self.m = m


	def Point_on_Line(self, k):
		#Return a 
		return vector_sum(self.P0, scalar_mult(k,m))



