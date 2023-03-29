import sys
from Classes.Ghost import *
from Classes.Music import *
from Classes.Pacman import Pacman
from Classes.Pellet import *
from Classes.Wall import *
from Scripts.helpers import *


class Main:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.score = 0
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pacman")
        self.font = pygame.font.SysFont('Arial', 48)

        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        # self.pacman = pygame.sprite.Group()
        self.setup()

    def setup(self):
        maze = [
            "##################################################",
            "#......................####......................#",
            "#......................####......................#",
            "#..#####..###########..####..###########..#####..#",
            "#..#####..###########..####..###########..#####..#",
            "#..#####..###########..####..###########..#####..#",
            "#......................####......................#",
            "#......................####......................#",
            "########..#########............#########..########",
            "########..#########............#########..########",
            "########..#########..##....##..#########..########",
            ".....................#......#.....................",
            ".....................#......#........*.*..*..........",
            ".....................#......#.....................",
            "########..#########..########..#########..########",
            "########..#########............#########..########",
            "########..#########............#########..########",
            "#......................####......................#",
            "#......................####......................#",
            "#..#####..###########..####..###########..#####..#",
            "#..#####..###########..####..###########..#####..#",
            "#..#####..###########..####..###########..#####..#"
            "#..#####..###########..####..###########..#####..#",
            "#......................####......................#",
            "#......................####......................#",
            "##################################################"
        ]

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "#":
                    wall = Wall(j * WALL_WIDTH, i * WALL_HEIGHT)
                    self.walls.add(wall)
                    self.all_sprites.add(wall)

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "*":
                    p = Pellet(j * WALL_WIDTH, i * WALL_HEIGHT)
                    self.pellets.add(p)
                    self.all_sprites.add(p)

            # Add the wall to the all_sprites group
        self.all_sprites.add(wall)

        # Create the Pacman
        self.pacman = Pacman(25, 25)
        self.all_sprites.add(self.pacman)
        # self.pacman.eat_pellets(self.pellets)

        # Create the Ghosts
        self.ghosts.add(Ghost(320, 240, RED))
        self.ghosts.add(Ghost(320, 256, BLUE))
        self.ghosts.add(Ghost(304, 240, PINK))
        self.ghosts.add(Ghost(304, 256, ORANGE))
        self.all_sprites.add(self.ghosts)

    def run(self):
        main_theme = Music('pacman music/ingame_menu.mp3')
        main_theme.play()
        pygame.mixer.music.set_volume(0.1)
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.pacman.direction = "L"
                    elif event.key == pygame.K_RIGHT:
                        self.pacman.direction = "R"
                    elif event.key == pygame.K_UP:
                        self.pacman.direction = "U"
                    elif event.key == pygame.K_DOWN:
                        self.pacman.direction = "D"

            # Update the Pacman
            self.pacman.update(self.walls)
            self.pacman.eat_pellets(self.pellets, self)

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
            score_text = self.font.render("Score: " + str(self.score), True, WHITE)
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
        main_theme = Music('pacman music/ingame_theme.mp3')
        main_theme.fadeout()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()


main = Main()
main.run()
