import pygame
from Scripts.constants import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)  # Set the color of the wall
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
