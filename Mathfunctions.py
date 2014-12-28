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



