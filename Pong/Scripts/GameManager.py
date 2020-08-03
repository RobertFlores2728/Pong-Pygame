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

    def set_ball(self, ball):
        self.ball = ball

    def set_player_paddle(self, paddlePlayer):
        self.paddlePlayer = paddlePlayer

    def set_ai_paddle(self, paddleAI):
        self.paddleAI = paddleAI

    def spawn_game_objects(self):
        # create player paddle
        paddlePlayer = PaddlePlayer(self.screen)
        gameManager.set_player_paddle(paddlePlayer)

        # create ai paddle
        paddleAI = PaddleAI(self.screen, gameManager)
        gameManager.set_ai_paddle(paddleAI)

        # create ball object
        ball = Ball(self.screen, gameManager)
        gameManager.set_ball(ball)