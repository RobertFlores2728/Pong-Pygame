import sys, pygame

class GameObjects:

    def __init__(self):
        self.ball = None
        self.paddlePlayer = None
        self.paddleAI = None

    def set_ball(self, ball):
        self.ball = ball

    def set_player_paddle(self, paddlePlayer):
        self.paddlePlayer = paddlePlayer

    def set_ai_paddle(self, paddleAI):
        self.paddleAI = paddleAI