#Photo Analysis Program - Isolates an object using a base picture and an active picture
#Modification - filter out noise by combining two pictures processed to optimize background and foreground detection



#Setup:
#Graphics modules
import pygame
import pygame.camera
import pygame.image
from PIL import Image, ImageDraw
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

def ProcessPhoto(BasePhoto, ActivePhoto, Tolerance, BackgroundColour, ForegroundColour, X_SIZE, Y_SIZE, filename):
        PositiveColour = ForegroundColour
        NegativeColour = BackgroundColour
        #BasePhoto = Image.open(BasePhoto)
        #BasePhoto = BasePhoto.load()
        #ActivePhoto = Image.open(ActivePhoto)
        #ActivePhoto = ActivePhoto.load()
        ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (255,255,255))
	ResultPhotoRaw.save(filename)
        ResultPhoto = ResultPhotoRaw.load()
        for x in range(0, X_SIZE):
                for y in range(0, Y_SIZE):
                        Base = BasePhoto[x,y]
                        Active = ActivePhoto[x,y]
                        if ComparePixels(Base, Active, Tolerance):
                                ResultPhoto[x,y] = PositiveColour
                        else:
                                ResultPhoto[x,y]= NegativeColour
	ResultPhotoRaw.save("Testing.PNG")
	return ResultPhotoRaw

def NeighborhoodScan(ScanRadius, Photo, ForegroundColour, BackgroundColour, x, y):
	#Takes a photo in two RGB colours, ForegroundColour and BackgroundColour and scans pixels in the neighborhood to determine 
	#to determine whether to keep the pixel colour the same or change it based on the colours of other nearby pixels
	Sum = 0
	#The following nested loop adds one for Foreground Colour and Subtracts one for background colour
	for X in range(x-ScanRadius, x+ScanRadius):
		for Y in range(y-ScanRadius, y+ScanRadius):
			if Photo[X,Y] == ForegroundColour:
				Sum+=1
			else:
				Sum-=1
	#If the sum is positive, then the foreground colour wins and vice versa
	if Sum >=0:
		return ForegroundColour
	else:
		return BackgroundColour		
			
def PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour):
	if NeighborhoodForeground == PositiveColour and NeighborhoodBackground == PositiveColour:
		return PositiveColour
	elif NeighborhoodForeground == PositiveColour and NeighborhoodBackground == NegativeColour:
		return PositiveColour
	elif NeighborhoodForeground == NegativeColour and NeighborhoodBackground == PositiveColour:
		return PositiveColour
	else:	
		return NegativeColour

def SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, Size, X_SIZE, Y_SIZE):
	#Check for square regions in the Foreground Photo within 'Size' of point (x,y) that are only of the foreground colour.
	#Paste these into the BackgroundPhoto to create the ResultPhoto
	X_Squares = int(X_SIZE/(2*Size+1))
	Y_Squares = int(Y_SIZE/(2*Size+1))
	ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (0,0,0))
        ResultPhotoRaw.save("TestSquareOverlay.PNG")
        ResultPhoto = ResultPhotoRaw.load()
	draw = ImageDraw.Draw(ResultPhotoRaw)
	for x in range(0, X_Squares):
		for y in range(0, Y_Squares):
			X = (2*Size+1)*x+Size
			Y = (2*Size+1)*y+Size
			#print X, Y
			Check = True
			for xi in range(X-Size, X+Size):
				for yi in range(Y-Size, Y+Size):
					if ForegroundPhoto[xi,yi] == NegativeColour:
						Check = False
			
			if Check == True:
				draw.rectangle(((X-Size, Y-Size),(X+Size, Y+Size)), "white")
				print X,Y
	ResultPhotoRaw.save("Testing.PNG")
        return ResultPhotoRaw
	

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
	#scan photo and compare
ScanRadius = 2 #Square 'radius' to check adjacent pixels
ToleranceBackground = 40 #Set to an arbitrary quantity for later calibration
ToleranceForeground = 2
PositiveColour = (0,0,0) #Black
NegativeColour = (255,255,255) #White

BasePhoto = Image.open('BasePhotoRaw.PNG')
BasePhoto = BasePhoto.load()
ActivePhoto = Image.open('ActivePhotoRaw.PNG')
ActivePhoto = ActivePhoto.load()

#Prepare the ResultPhoto as a blank white photo
ResultPhotoRaw = Image.new("RGB", (X_SIZE, Y_SIZE), (255,255,255))
ResultPhotoRaw.save("ResultPhotoRaw.PNG")
ResultPhoto = Image.open('ResultPhotoRaw.PNG')
ResultPhoto = ResultPhoto.load()
ResultPhoto = ResultPhotoRaw.load()

#Save a photo processed with ForegroundTolerance:
#BasePhoto, ActivePhoto, Tolerance, ForegroundColour, BackgroundColour)
ForegroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceForeground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'F.PNG') 
ForegroundPhotoRaw.save('Foreground.PNG')
ForegroundPhoto = ForegroundPhotoRaw.load()
#Save a photo processed with BackgroundTolerance:
BackgroundPhotoRaw = ProcessPhoto(BasePhoto, ActivePhoto, ToleranceBackground, PositiveColour, NegativeColour, X_SIZE, Y_SIZE, 'B.PNG')
BackgroundPhotoRaw.save('Background.PNG')
BackgroundPhoto = BackgroundPhotoRaw.load()

#Option 1: Process Background and Foreground photos, comparing pixel colours
#Compare the two photos
#for x in range(0+ScanRadius, X_SIZE-ScanRadius):
#	for y in range(0+ScanRadius, Y_SIZE-ScanRadius):
#		#Check the pixel colour of the foreground photo
#		NeighborhoodForeground = NeighborhoodScan(ScanRadius, ForegroundPhoto, PositiveColour, NegativeColour, x, y)
#		#Check the pixel colour of the background photo
#		NeighborhoodBackground = NeighborhoodScan(ScanRadius, BackgroundPhoto, PositiveColour, NegativeColour, x, y)
#		#Make a decision as to the final pixel colour:
#		ResultPhoto[x,y] = PixelDecision(NeighborhoodForeground, NeighborhoodBackground, PositiveColour, NegativeColour)

#Option 2: Use the SquareOverlay Algorithm to fill in the Object on the Background Photo, saving the result 
SquareSize = 5
ResultPhoto = SquareOverlay(ForegroundPhoto, BackgroundPhotoRaw, PositiveColour, NegativeColour, SquareSize, X_SIZE, Y_SIZE)

datenow = date.today()
timenow = str(datetime.now()).strip('.')
#print timenow
filename = "Result"+str(ToleranceForeground)+"_"+str(ToleranceBackground)+"_"+str(timenow)+'.PNG'
print filename
#ResultPhotoRaw.save(filename)

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
