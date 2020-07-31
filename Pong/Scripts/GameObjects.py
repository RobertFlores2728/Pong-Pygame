import sys, pygame

class GameObjects:

    def __init__(self):
        self.ball = None

    def set_ball(self, ball):
        self.ball = ball
        self.ball.color = (50, 255, 50)