import pygame

from Scripts.helpers import *


def main():
    pygame.init()
    pygame.display.set_caption("PacWoman")
    currect_state = 'menu'
    finish = False
    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

        if currect_state == 'menu':
            screen.fill(WHITE)
            play_button = pygame.image.load(PLAY_IMAGE_BUTTON)
            play_button = pygame.transform.scale(play_button, (MENU_BUTTON_SIZE_X_Y, MENU_BUTTON_SIZE_X_Y))
            screen.blit(play_button, (MENU_BUTTON1_x, MENU_BUTTON1_y))

        if currect_state == 'game':
            pass

        if currect_state == 'leaderboard':
            pass

        if currect_state == 'settings':
            pass


        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
