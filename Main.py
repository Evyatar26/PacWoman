from Scripts.helpers import *

def main():
    pygame.init()

    finish = False
    while not finish:

        pygame.display.set_caption('PacWoman')
        img = pygame.image.load("Images/55050.jpg")
        img = pygame.transform.scale(img,
                                     (650, 460))
        screen.blit(img, (300, 150))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                img = pygame.image.load("Images/pacman.jpeg")
                img = pygame.transform.scale(img,(300,150))
                screen.blit(img,(80,80))
        pygame.display.flip()
    pygame.quit()
main()