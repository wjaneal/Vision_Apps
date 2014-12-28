import pygame
import pygame.camera
import pygame.image
from pygame.locals import *
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image1 = cam.get_image()
pygame.image.save(image1,'test1.PNG')
#/usr/share/pyshared/pygame/examples/camera.py ?

