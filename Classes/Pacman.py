import os

import pygame

from Scripts.constants import *


class Pacman(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.pacwoman_animation = {'L': [], 'R': [], 'U': [], 'D': []}
        for direction in ['L', 'R', 'U', 'D']:
            for i in range(1, 4):
                image = pygame.image.load(f'pacwoman_sprites/pac{direction}{i}.png').convert_alpha()
                image = pygame.transform.scale(image, (width, height))
                self.pacwoman_animation[direction].append(image)
        self.current_image = 0
        self.animation_delay = ANIMATION_DELAY_PACWOMAN_LEFT_SIDE
        self.animation_counter = ANIMATION_COUNTER
        self.speed = PACMAN_SPEED
        self.direction = "R"
        self.images = self.pacwoman_animation[self.direction]
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_WIDTH // 2
        self.rect.y = WINDOW_HEIGHT // 2
        self.score = 0

    def update(self, walls):
        if self.direction == "L":
            self.rect.x -= self.speed
        elif self.direction == "R":
            self.rect.x += self.speed
        elif self.direction == "U":
            self.rect.y -= self.speed
        elif self.direction == "D":
            self.rect.y += self.speed
        self.images = self.pacwoman_animation[self.direction]
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
                if self.direction == "R":
                    self.rect.right = wall.rect.left
                elif self.direction == "L":
                    self.rect.left = wall.rect.right
                elif self.direction == "U":
                    self.rect.top = wall.rect.bottom
                elif self.direction == "D":
                    self.rect.bottom = wall.rect.top

    def eat_pellets(self, pellets, main):
        minecraft_eating = pygame.mixer.Sound('pacman music/minecraft_eating.mp3')
        # Check for collisions with pellets
        for pellet in pellets:
            if self.rect.colliderect(pellet.rect):
                pellet.kill()
                minecraft_eating.stop()
                minecraft_eating.play()
                main.score += 10
