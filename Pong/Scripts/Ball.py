import sys, pygame, random, time, threading
from Scripts.GameObject import *

class Ball(GameObject):


    def __init__(self, gameManager):
        self.color = (random.randint(200,255), random.randint(200,255), 150)

        self.gameManager = gameManager

        self.ballRect = pygame.Rect(int(self.gameManager.screen.get_width() / 2), random.randint(20, self.gameManager.screen.get_height() - 20), 20, 20)
        self.ballTravelX = 1  # amount the ball travels on the x axis. increases with each hit
        self.ballTravelY = 0#random.randint(-100, 100) / 100  # 1 = greatest curve, 0 = straight
        self.ballSpeed = 10



    def draw(self):
        # draw ball
        pygame.draw.rect(self.gameManager.screen, self.color, self.ballRect)

    def move(self):
        # ball boundaries check, bounce around walls
        if self.ballRect.y > self.gameManager.screen.get_height() - self.ballRect.height:
            self.ballTravelY = -self.ballTravelY
        if self.ballRect.y < 0:
            self.ballTravelY = -self.ballTravelY

        # move ball
        self.ballRect.x += int(self.ballTravelX * self.ballSpeed)
        self.ballRect.y += int(self.ballTravelY * self.ballSpeed)

    def check_paddle_collision_player(self):
        if self.gameManager.paddlePlayer is None:
            return

        # check paddle ball collision
        if self.gameManager.paddlePlayer.paddleRect.colliderect(self.ballRect) and self.ballTravelX < 0:
            # get new y direction of ball
            self.ballTravelX = -self.ballTravelX
            self.ballTravelY = (self.ballRect.centery - self.gameManager.paddlePlayer.paddleRect.centery) / 99  # new y travel
            self.ballTravelX += 0.1  # new x travel
            if self.ballTravelX > 2.5:
                self.ballTravelX = 2.5


    def check_paddle_collision_ai(self):
        if self.gameManager.paddleAI is None:
            return

        # check paddle ball collision
        if self.gameManager.paddleAI.paddleRect.colliderect(self.ballRect) and self.ballTravelX > 0:
            # get new y direction of ball
            self.ballTravelX = -self.ballTravelX
            self.ballTravelY = (self.ballRect.centery - self.gameManager.paddleAI.paddleRect.centery) / 99  # new y travel
            self.ballTravelX -= 0.1  # new x travel
            if self.ballTravelX > 2.5:
                self.ballTravelX = 2.5

    def check_if_scored(self):
        if self.gameManager.intermission:
            return

        if self.ballRect.x > self.gameManager.screen.get_width() or self.ballRect.x < 0 - self.ballRect.width:
            self.gameManager.intermission = True
            timer1 = threading.Timer(1.0, self.reset_ball)
            timer1.start()

        if self.ballRect.x > self.gameManager.screen.get_width():
            self.gameManager.playerScore += 1
        if self.ballRect.x < 0 - self.ballRect.width:
            self.gameManager.AIScore += 1



    def reset_ball(self):
        self.ballRect = pygame.Rect(int(self.gameManager.screen.get_width() / 2),
                                    random.randint(20, self.gameManager.screen.get_height() - 20), 20, 20)
        self.ballTravelX = 1  # amount the ball travels on the x axis. increases with each hit
        self.ballTravelY = 0  # random.randint(-100, 100) / 100  # 1 = greatest curve, 0 = straight
        self.gameManager.paddleAI.new_offset()
        self.gameManager.intermission = False


    def update(self):
        self.check_if_scored()
        self.check_paddle_collision_player()
        self.check_paddle_collision_ai()
        self.move()
        self.draw()

    def test(self):
        print("RUNS!")
