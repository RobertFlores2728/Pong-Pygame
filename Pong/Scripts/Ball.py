import sys, pygame

class Ball:


    def __init__(self, screen, gameObjects):
        self.color = (255, 200, 200)
        self.screen = screen

        self.gameObjects = gameObjects

        self.ballRect = pygame.Rect(int(screen.get_width() / 2), int(screen.get_height() / 2), 20, 20)
        self.ballTravelX = 1  # should be 1 or -1 only. ball either goes left or right
        self.ballTravelY = -1  # 1 = greatest curve, 0 = straight
        self.ballSpeed = 10  # speed will increase with each hit

    def draw(self):
        # draw ball
        pygame.draw.rect(self.screen, self.color, self.ballRect)

    def move(self):
        # ball boundaries check, bounce around walls
        if self.ballRect.x > self.screen.get_width() - self.ballRect.width:
            self.ballTravelX = -self.ballTravelX
        if self.ballRect.x < 0:
            self.ballTravelX = -self.ballTravelX
        if self.ballRect.y > self.screen.get_height() - self.ballRect.height:
            self.ballTravelY = -self.ballTravelY
        if self.ballRect.y < 0:
            self.ballTravelY = -self.ballTravelY

        # move ball
        self.ballRect.x += int(self.ballTravelX * self.ballSpeed)
        self.ballRect.y += int(self.ballTravelY * self.ballSpeed)
