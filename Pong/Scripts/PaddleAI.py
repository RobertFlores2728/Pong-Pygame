import sys, pygame

class PaddleAI:

    def __init__(self, screen, gameObjects):
        self.screen = screen
        self.gameObjects = gameObjects
        self.paddleRect = pygame.Rect(self.screen.get_width() - 50, 0, 50, 200)
        self.paddleSpeed = 7

    def move(self):
        if(self.gameObjects.ball is None):
            return

        # Move paddle
        if self.paddleRect.centery < self.gameObjects.ball.ballRect.centery:
            self.paddleRect.y += self.paddleSpeed
        elif self.paddleRect.centery > self.gameObjects.ball.ballRect.centery:
            self.paddleRect.y -= self.paddleSpeed


        # paddle boundaries check
        if self.paddleRect.y < 0:
            self.paddleRect.y = 0
        elif self.paddleRect.y > self.screen.get_height() - self.paddleRect.height:
            self.paddleRect.y = self.screen.get_height() - self.paddleRect.height

    def draw(self):
        # draw paddle
        pygame.draw.rect(self.screen, (0,0,0), self.paddleRect)

    def update(self):
        self.move()
        self.draw()