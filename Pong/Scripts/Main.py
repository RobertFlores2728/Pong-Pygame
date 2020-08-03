import sys, pygame

from Scripts.Ball import *
from Scripts.PaddlePlayer import *
from Scripts.PaddleAI import *
from Scripts.GameManager import *


pygame.init()




def main():

    gameManager = GameManager()

    gameManager.start()


    while True:








        gameManager.update()

    return



main()
