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

    # create player paddle
    paddlePlayer = PaddlePlayer(screen)
    gameManager.set_player_paddle(paddlePlayer)


    # create ai paddle
    paddleAI = PaddleAI(screen, gameManager)
    gameManager.set_ai_paddle(paddleAI)


    # create ball object
    ball = Ball(screen, gameManager)
    gameManager.set_ball(ball)




    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            print("p was pressed!")



        # Update screen
        pygame.display.flip()
        screen.fill((100, 100, 255))

        # update player paddle object
        paddlePlayer.update()

        # update ai paddle object
        paddleAI.update()

        # update ball object
        ball.update()

    return



main()
