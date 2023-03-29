import pygame
import random
from Scripts.constants import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.direction = None
        self.image = pygame.Surface((20, 20))
        self.image.fill(color)  # Set the color of the ghost
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = GHOST_SPEED

    def change_direction(self, pacman):
        directions = ["L", "R", "U", "D"]
        if self.rect.x % 16 == 0 and self.rect.y % 16 == 0:
            x1 = self.rect.x
            y1 = self.rect.y
            x2 = pacman.x
            y2 = pacman.y
            if x1 < x2:
                self.direction = random.choice(directions)
            elif x1 > x2:
                self.direction = random.choice(directions)
            elif y1 < y2:
                self.direction = random.choice(directions)
            elif y1 > y2:
                self.direction = random.choice(directions)

    def collide_with_walls(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == "R":
                    self.rect.right = wall.rect.left
                elif self.direction == "L":
                    self.rect.left = wall.rect.right
                elif self.direction == "U":
                    self.rect.top = wall.rect.bottom
                elif self.direction == "D":
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
        self.change_direction(pacman)
