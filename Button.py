import pygame


class Button:
    def __init__(self, text, position, size, color, font_size, font_color, action):
        self.text = text
        self.position = position
        self.size = size
        self.color = color
        self.font_size = font_size
        self.font_color = font_color
        self.action = action

        self.font = pygame.font.Font(None, self.font_size)
        self.surface = self.font.render(self.text, True, self.font_color)
        self.rect = self.surface.get_rect(center=self.position)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.surface, self.rect)
