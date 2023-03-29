import pygame
from Scripts.constants import *
import os

from Scripts.helpers import screen


class Pacman(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.images = []
        for i in range(0, 3):
            filename = os.path.join('pacwoman_sprites', f'tile00{i}.png')
            image = pygame.image.load(filename).convert_alpha()
            image = pygame.transform.scale(image, (width, height))
            self.images.append(image)
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2
        self.animation_delay = ANIMATION_DELAY_PACWOMAN_LEFT_SIDE
        self.animation_counter = ANIMATION_COUNTER
        self.speed = PACMAN_SPEED
        self.direction = "right"
        self.score = 0

    def update(self, walls):
        if self.direction == "left":
            self.rect.x -= self.speed
        elif self.direction == "right":
            self.rect.x += self.speed
        elif self.direction == "up":
            self.rect.y -= self.speed
        elif self.direction == "down":
            self.rect.y += self.speed
        self.collide_with_walls(walls)

        # Update the animation
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.image = self.images[self.current_image]

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

    def eat_pellets(self, pellets):
        # Check for collisions with pellets
        for pellet in pellets:
            if self.rect.colliderect(pellet.rect):
                pellets.remove(pellet)
                self.score += 10