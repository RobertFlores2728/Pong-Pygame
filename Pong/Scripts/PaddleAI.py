import sys, pygame, random
from Scripts.GameObject import *

class PaddleAI(GameObject):

    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.paddleRect = pygame.Rect(self.gameManager.screen.get_width() - 50, 0, 50, 200)
        self.paddleSpeed = 10
        self.offset = 0

    def move(self):
        if(self.gameManager.ball is None):
            return

        # Move paddle
        position = self.gameManager.ball.ballRect.centery + self.offset
        if self.paddleRect.centery < position - 10:
            self.paddleRect.y += self.paddleSpeed
        elif self.paddleRect.centery > position + 10:
            self.paddleRect.y -= self.paddleSpeed

        # paddle boundaries check
        if self.paddleRect.y < 0:
            self.paddleRect.y = 0
        elif self.paddleRect.y > self.gameManager.screen.get_height() - self.paddleRect.height:
            self.paddleRect.y = self.gameManager.screen.get_height() - self.paddleRect.height

    def draw(self):
        # draw paddle
        pygame.draw.rect(self.gameManager.screen, (0,0,0), self.paddleRect)

    def new_offset(self):
        if self.paddleRect.colliderect(self.gameManager.ball.ballRect):
            self.offset = random.randint(-110, 110)


    def update(self):
        self.move()
        self.draw()
        self.new_offset()

