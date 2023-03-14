import pygame.image
import os


# class SpriteSheet:
#
#     def __init__(self, filename, sprite_width, sprite_height):
#         self.sprite_sheet = pygame.image.load(filename).convert_alpha()
#         self.sprite_width = sprite_width
#         self.sprite_height = sprite_height
#         self.num_sprites_x = self.sprite_sheet.get_width() // self.sprite_width
#         self.num_sprites_y = self.sprite_sheet.get_height() // self.sprite_height
#
#     def get_sprite(self, x, y):
#         sprite_rect = pygame.Rect(x * self.sprite_width, y * self.sprite_height, self.sprite_width,
#                                   self.sprite_height)
#         sprite = self.sprite_sheet.subsurface(sprite_rect)
#         return sprite

class Pacman1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        for i in range(1, 3):
            filename = os.path.join('pacwoman_sprites', f'tile{i}.png')
            image = pygame.image.load(filename).convert_alpha()
            self.images.append(image)
        self.current_image = 0
        self.image = self.images[self.current_image]
        self.rect = self.image.get_rect()
        #  change location
        self.rect.center = (400, 300)
        self.animation_delay = 10
        self.animation_counter = 0

    def update(self):
        # Update the animation
        self.animation_counter += 1
        if self.animation_counter >= self.animation_delay:
            self.animation_counter = 0
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
            self.image = self.images[self.current_image]
