import pygame
from Scripts.constants import *


class Pellet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(WHITE)  # Set the color of the pellet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
