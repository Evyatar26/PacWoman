import sys

import pygame

from Classes.Ghost import *
from Classes.Pacman import Pacman
from Classes.Pellet import *
from Classes.Wall import *
from Classes.Music import *
from Scripts.constants import *
from Scripts.helpers import *
# from Pacman1 import Pacman1


class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pacman")
        self.font = pygame.font.SysFont('Arial', 48)
        self.score = 0

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.pacman = pygame.sprite.Group()

        self.setup()

    def setup(self):
        # Create the walls
        level_map = [
            "W" * WINDOW_WIDTH,
            ("W" + " " * (WINDOW_WIDTH - 2) + "W") * ((WINDOW_HEIGHT - 2) // 2),
            "W" + " " * (WINDOW_WIDTH - 2) + "P",
            ("W" + " " * (WINDOW_WIDTH - 2) + "W") * ((WINDOW_HEIGHT - 2) // 2),
            "W" * WINDOW_WIDTH
        ]

        # add pellets to the level map
        for i in range(1, WINDOW_HEIGHT - 1):
            if i % 2 == 1:
                row = ""
                for j in range(1, WINDOW_WIDTH - 1):
                    if j % 2 == 1:
                        row += "."
                    else:
                        row += " "
                level_map.insert(i, "W" + row + "W")

        for row, tiles in enumerate(level_map):
            for col, tile in enumerate(tiles):
                if tile == "W":
                    wall = Wall(col * 16, row * 16, 16, 16)
                    self.all_sprites.add(wall)
                    self.walls.add(wall)
                elif tile == "P":
                    pellet = Pellet(col * 16 + 4, row * 16 + 4)
                    self.all_sprites.add(pellet)
                    self.pellets.add(pellet)

        # Create the Pacman
        self.pacman = Pacman(33, 33)
        self.all_sprites.add(self.pacman)

        # Create the Ghosts
        self.ghosts.add(Ghost(320, 240, RED))
        self.ghosts.add(Ghost(320, 256, BLUE))
        self.ghosts.add(Ghost(304, 240, PINK))
        self.ghosts.add(Ghost(304, 256, ORANGE))
        self.all_sprites.add(self.ghosts)

    def run(self):

        main_theme = Music('pacman music/ingame_theme.mp3')
        main_theme.play()
        running = True
        while running:

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pacman.direction = "left"
                    elif event.key == pygame.K_RIGHT:
                        self.pacman.direction = "right"
                    elif event.key == pygame.K_UP:
                        self.pacman.direction = "up"
                    elif event.key == pygame.K_DOWN:
                        self.pacman.direction = "down"

            # Update the Pacman
            self.pacman.update(self.walls)
            self.pacman.eat_pellets(self.pellets)

            # music

            # Update the Ghosts
            for ghost in self.ghosts:
                ghost.update(self.walls, self.pacman)

            # Check if Pacman collides with a ghost
            if pygame.sprite.spritecollideany(self.pacman, self.ghosts):
                self.game_over()

            # Draw the scene
            self.screen.fill(BLACK)
            self.all_sprites.draw(self.screen)

            # Draw the score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (16, 16))

            # create pacman animation
            # self.pacman.update()
            # self.pacman.draw()

            pygame.display.flip()
            self.clock.tick(60)

    def game_over(self):
        screen.fill(BLACK)
        self.font = pygame.font.SysFont('Arial', 72)
        game_over_text = self.font.render("GAME OVER", True, RED)
        self.screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2 - 50))
        pygame.display.flip()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()


main = Main()
main.run()
