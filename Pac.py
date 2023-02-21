import pygame
from helpers import *

class Pac:
    def __init__(self,imgSrcMouthOpen,imgSrcMouthClosed,location,pacWidth,pacHeight):
        self.imgMouthOpen = imgSrcMouthOpen
        self.imgMouthClosed = imgSrcMouthClosed
        self.location = location
        self.pacWidth = pacWidth
        self.pacHeight = pacHeight


    def drawPac(self,imgSrc,location,pacWidth,pacHeight):
        img = pygame.image.load(imgSrc)
        img = pygame.transform.scale(img,(pacWidth,pacHeight))
        screen.blit(img,location)