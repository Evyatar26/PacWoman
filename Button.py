from Scripts.helpers import *
import pygame


class Button:
    def __init__(self, image, loc, text, font, size, color):
        self.image = image
        self.loc = loc
        self.text = text
        self.font = font
        self.size = size
        self.color = color

    def image_button(self):
        img = pygame.image.load(self.image)
        img = pygame.transform.scale(img, self.size)
        screen.blit(img, self.loc)

    def button_text(self):
        font = pygame.font.SysFont(self.font, self.size)
        text = font.render(self.text, True, self.color)
        screen.blit(text, self.loc)
