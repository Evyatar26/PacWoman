import pygame


class Music:

    def __init__(self, filename):
        self.filename = filename
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play(-1)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def fadeout(self):
        pygame.mixer.music.fadeout(1500)

    def stop(self):
        pygame.mixer.music.stop()
