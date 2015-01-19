#Photo Analysis Program


#Setup:
#Graphics modules
import pygame
import pygame.camera
import pygame.image
from PIL import Image
from pygame.locals import *
#Random and Datetime
from random import *
from datetime import *


#Subroutines:
def ComparePixels(P1,P2,tolerance):
	t1 = abs(P1[0]-P2[0])
	t2 = abs(P1[1]-P2[1])
	t3 = abs(P1[2]-P2[2])
	if t1<= tolerance and t2 <=tolerance and t3 <=tolerance:
		return True
	else:
		return False

#Initialize Camera
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))

#Take a Base image
print "Please take a photo of the base scene"
raw_input("Please hit any key to take the base photo")
cam.start()
BasePhotoRaw = cam.get_image()
pygame.image.save(BasePhotoRaw, 'BasePhotoRaw.PNG')
cam.stop()
#Take an "Active Image" - with an individual or object in the scene
print "Please take a photo of the active scene"
raw_input("Please hit any key to take the active photo")
cam.start()
ActivePhotoRaw = cam.get_image()
pygame.image.save(ActivePhotoRaw, 'ActivePhotoRaw.PNG')
cam.stop()
#Determine the size of the photos
X_SIZE = BasePhotoRaw.get_width()
Y_SIZE = BasePhotoRaw.get_height()

print X_SIZE
print Y_SIZE

#def getPixel(X, Y)
	#return - RGB colour of Pixel
for test_tolerance in range (1,40):
	#scan photo and compare
	Tolerance = test_tolerance #Set to an arbitrary quantity for later calibration
	PositiveColour = (0,0,0)
	NegativeColour = (255,255,255)
	BasePhoto = Image.open('BasePhotoRaw.PNG')
	BasePhoto = BasePhoto.load()
	ActivePhoto = Image.open('ActivePhotoRaw.PNG')
	ActivePhoto = ActivePhoto.load()
	ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (255,255,255))
	ResultPhotoRaw.save("ResultPhotoRaw.PNG")
	ResultPhoto = Image.open('ResultPhotoRaw.PNG')
	ResultPhoto = ResultPhoto.load()
	
	
	ResultPhoto = ResultPhotoRaw.load()
	for x in range(0, X_SIZE):
		for y in range(0, Y_SIZE):
			Base = BasePhoto[x,y]
			Active = ActivePhoto[x,y]
			if ComparePixels(Base, Active, Tolerance):
				ResultPhoto[x,y] = PositiveColour
			else:
				ResultPhoto[x,y]= NegativeColour
	
	datenow = date.today()
	timenow = str(datetime.now()).strip('.')
	print timenow
	filename = "Result"+str(Tolerance)+str(timenow)+'.PNG'
	ResultPhotoRaw.save(filename)
	
	#analyse data set
	#Check (Xav,Yav):
		#whole photo
		#horizontal stripes
		#vertical stripes
		#store in an array
		#Maximum range of horizontal and vertical change
	#Compare current array to last several arrays
		#note differences in horizontal and vertical stripe averages with respect to whole picture
		#make some decision based on this.
