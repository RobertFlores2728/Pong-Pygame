import sys, pygame

from Scripts.Ball import *
from Scripts.PaddlePlayer import *
from Scripts.PaddleAI import *

class GameManager:

    def __init__(self):
        self.playerScore = 0
        self.AIScore = 0

        self.paused = False
        self.intermission = False

        self.ball = None
        self.paddlePlayer = None
        self.paddleAI = None

        self.screen = None
        self.clock = None

        self.gameObjects = []

    def setup_pygame(self):
        self.screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
        self.clock = pygame.time.Clock()


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




    def update_screen(self):
        # Update screen
        self.clock.tick(120)
        pygame.display.flip()
        self.screen.fill((100, 100, 255))

    def update_score_text(self):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        score = str(self.playerScore) + " - " + str(self.AIScore)
        textSurface = font.render(score, True, (255, 255, 255))

        self.screen.blit(textSurface, textSurface.get_rect())


    def start(self):
        self.setup_pygame()
        self.spawn_game_objects()

    def update(self):
        if not(self.paused):
            self.update_game_objects()
        if self.paused:
            self.draw_menu()
        self.update_screen()
        self.update_score_text()

        self.check_input()

    def draw_menu(self):
        print("drawing menu...")

