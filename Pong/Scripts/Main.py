import sys, pygame

from Scripts.Ball import *
from Scripts.PaddlePlayer import *
from Scripts.PaddleAI import *
from Scripts.GameManager import *


pygame.init()




def main():
    screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
    clock = pygame.time.Clock()

    gameManager = GameManager(screen)

    gameManager.spawn_game_objects()


    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()





        # Update screen
        pygame.display.flip()
        screen.fill((100, 100, 255))

        gameManager.update()

    return



main()
