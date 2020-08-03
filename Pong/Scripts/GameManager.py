import sys, pygame

from Scripts.Ball import *
from Scripts.PaddlePlayer import *
from Scripts.PaddleAI import *

class GameManager:

    def __init__(self, screen):
        self.ball = None
        self.paddlePlayer = None
        self.paddleAI = None

        self.screen = screen
        self.clock = None

        self.gameObjects = []

    def setup_pygame(self):
        self.screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
        self.clock = pygame.time.Clock()

    def spawn_game_objects(self):
        # create player paddle
        self.paddlePlayer = PaddlePlayer(self.screen)
        self.gameObjects.append(self.paddlePlayer)

        # create ai paddle
        self.paddleAI = PaddleAI(self.screen, self)
        self.gameObjects.append(self.paddleAI)

        # create ball object
        self.ball = Ball(self.screen, self)
        self.gameObjects.append(self.ball)

    def update_game_objects(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def check_input(self):
        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            print("p was pressed!")

    def update_screen(self):
        # Update screen
        self.clock.tick(120)
        pygame.display.flip()
        self.screen.fill((100, 100, 255))

    def update(self):
        self.check_input()
        self.update_game_objects()

