import sys, pygame, time

from Scripts.Ball import *
from Scripts.PaddlePlayer import *
from Scripts.PaddleAI import *
from Scripts.Button import *

class GameManager:

    def __init__(self):
        self.playerScore = 0
        self.AIScore = 0

        self.paused = False
        self.hasScored = False

        self.ball = None
        self.paddlePlayer = None
        self.paddleAI = None

        self.screen = None
        self.clock = None

        self.gameObjects = []
        self.uiObjects = []

    def setup_pygame(self):
        self.screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
        self.clock = pygame.time.Clock()

    def setup_ui(self):
        button = Button(self)
        self.uiObjects.append(button)

    def update_ui(self):
        for uiObject in self.uiObjects:
            uiObject.update()

    def draw_ui(self):
        for uiObject in self.uiObjects:
            uiObject.draw()


    def spawn_game_objects(self):
        # create player paddle
        self.paddlePlayer = PaddlePlayer(self)
        self.gameObjects.append(self.paddlePlayer)

        # create ai paddle
        self.paddleAI = PaddleAI(self)
        self.gameObjects.append(self.paddleAI)

        # create ball object
        self.ball = Ball(self)
        self.gameObjects.append(self.ball)

    def update_game_objects(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_p:
                    print("p was pressed!")
                    self.paused = not (self.paused)
                    print(self.paused)

    def draw_game_objects(self):
        for gameObject in self.gameObjects:
            gameObject.draw()




    def update_screen(self):
        # Update screen
        self.clock.tick(120)
        pygame.display.flip()
        self.screen.fill((100, 100, 255))

    def update_score_text(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        score = str(self.playerScore) + " - " + str(self.AIScore)
        textSurface = font.render(score, True, (255, 255, 255))
        textRect = textSurface.get_rect()
        textRect.centerx = int(self.screen.get_width() / 2)

        self.screen.blit(textSurface, textRect)


    def start(self):
        self.setup_pygame()
        self.setup_ui()
        self.spawn_game_objects()

    def update(self):
        if not(self.paused):
            self.update_game_objects()
        if self.paused:
            self.update_ui()
            self.draw_ui()

        self.draw_game_objects()
        self.update_screen()
        self.update_score_text()

        self.check_input()








