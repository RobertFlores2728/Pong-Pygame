import sys, pygame
from Scripts.GameObject import *

class PaddlePlayer(GameObject):

    def __init__(self):
        self.paddleRect = pygame.Rect(0, 0, 50, 200)

    def input(self):
        keys = pygame.key.get_pressed()

        """ Move paddle
        if keys[pygame.K_w]:
            self.paddleRect.y -= self.paddleSpeed
        if keys[pygame.K_s]:
            self.paddleRect.y += self.paddleSpeed
        """

        mousePositionY = pygame.mouse.get_pos()[1]
        self.paddleRect.y = mousePositionY

        # paddle boundaries check
        if self.paddleRect.y < 0:
            self.paddleRect.y = 0
        elif self.paddleRect.y > self.gameManager.screen.get_height() - self.paddleRect.height:
            self.paddleRect.y = self.gameManager.screen.get_height() - self.paddleRect.height



    def draw(self):
        # draw paddle
        pygame.draw.rect(self.gameManager.screen, (0,0,0), self.paddleRect)

    def update(self):
        self.input()
        self.draw()