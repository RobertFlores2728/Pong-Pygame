import sys, pygame

class PaddlePlayer:

    def __init__(self, screen):
        self.screen = screen
        self.paddleRect = pygame.Rect(0, 0, 50, 200)
        self.paddleSpeed = 20

    def input(self):
        keys = pygame.key.get_pressed()

        # Move paddle
        if keys[pygame.K_w]:
            self.paddleRect.y -= self.paddleSpeed
        if keys[pygame.K_s]:
            self.paddleRect.y += self.paddleSpeed

        # paddle boundaries check
        if self.paddleRect.y < 0:
            self.paddleRect.y = 0
        elif self.paddleRect.y > self.screen.get_height() - self.paddleRect.height:
            self.paddleRect.y = self.screen.get_height() - self.paddleRect.height

    def draw(self):
        # draw paddle
        pygame.draw.rect(self.screen, (0,0,0), self.paddleRect)

    def update(self):
        self.input()
        self.draw()