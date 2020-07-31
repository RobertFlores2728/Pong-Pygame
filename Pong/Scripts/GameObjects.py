import sys, pygame

class GameObjects:

    def __init__(self):
        self.ball = None
        self.paddlePlayer = None

    def set_ball(self, ball):
        self.ball = ball

    def set_player_paddle(self, paddlePlayer):
        self.paddlePlayer = paddlePlayer