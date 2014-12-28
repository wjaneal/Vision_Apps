import pygame
import pygame.camera
import pygame.image
from PIL import Image

from pygame.locals import *

from random import *

pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image1 = cam.get_image()

#Get the width of the photo and print it
#Get the height of the photo and print it
#Select a random Pixel based on the width and Height
#Print the RGB colour components of the Pixel
H = image1.get_height()
W = image1.get_width()
x = int(random()*W)
y = int(random()*H)

#Save the image:
pygame.image.save(image1,'test1.PNG')
#Load the image using the PIL module:
im = Image.open("test1.PNG") #Can be many different formats.
pix = im.load()
print im.size #Get the width and height of the image
print "The colour of pixel (", x, ", ", y, ") is: ", pix[x,y] #Get the RGBA Value of the a pixel of an image



