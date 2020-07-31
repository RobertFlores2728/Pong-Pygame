import sys, pygame, random

class Ball:


    def __init__(self, screen, gameObjects):
        self.color = (random.randint(200,255), random.randint(200,255), 150)
        self.screen = screen

        self.gameObjects = gameObjects

        self.ballRect = pygame.Rect(int(screen.get_width() / 2), random.randint(20, screen.get_height() - 20), 20, 20)
        self.ballTravelX = 1  # amount the ball travels on the x axis. increases with each hit
        self.ballTravelY = random.randint(-100, 100) / 100  # 1 = greatest curve, 0 = straight
        self.ballSpeed = 10

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

    def check_paddle_collision_player(self):
        if self.gameObjects.paddlePlayer is None:
            return

        # check paddle ball collision
        if self.gameObjects.paddlePlayer.paddleRect.colliderect(self.ballRect) and self.ballTravelX < 0:
            # get new y direction of ball
            self.ballTravelX = -self.ballTravelX
            self.ballTravelY = (self.ballRect.centery - self.gameObjects.paddlePlayer.paddleRect.centery) / 100  # new y travel
            self.ballTravelX += 0.1  # new x travel
            if self.ballTravelX > 2.5:
                self.ballTravelX = 2.5
            print("Collision!")

    def update(self):
        self.move()
        self.draw()
        self.check_paddle_collision_player()
