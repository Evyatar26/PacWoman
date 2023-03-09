import pygame
from Scripts.constants import *
class Pacman(pygame.sprite.Sprite):
    class Pacman(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.Surface((16, 16))
            self.image.fill(YELLOW)  # Set the color of Pacman
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
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