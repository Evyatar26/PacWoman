import pygame
import random
from Scripts.constants import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)  # Set the color of the ghost
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = GHOST_SPEED
        self.direction = "left"

    def change_direction(self):
        directions = ["left", "right", "up", "down"]
        if self.rect.x % 16 == 0 and self.rect.y % 16 == 0:
            self.direction = random.choice(directions)

    def collide_with_walls(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == "right":
                    self.rect.right = wall.rect.left
                elif self.direction == "left":
                    self.rect.left = wall.rect.right
                elif self.direction == "up":
                    self.rect.top = wall.rect.bottom
                elif self.direction == "down":
                    self.rect.bottom = wall.rect.top

    def update(self, walls, pacman):
        if self.direction == "L":
            self.rect.x -= self.speed
        elif self.direction == "R":
            self.rect.x += self.speed
        elif self.direction == "U":
            self.rect.y -= self.speed
        elif self.direction == "D":
            self.rect.y += self.speed

        self.collide_with_walls(walls)
        self.change_direction()
