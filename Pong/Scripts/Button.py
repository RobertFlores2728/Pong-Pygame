import pygame,time

class Button:
    def __init__(self, gameManager):
        self.gameManager = gameManager
        self.buttonSurface = pygame.Surface((100, 100))
        self.buttonSurface.fill((200, 255, 0))
        self.buttonRect = self.buttonSurface.get_rect()
        self.buttonRect.centerx = int(self.gameManager.screen.get_width() / 2)
        self.buttonRect.centery = int(self.gameManager.screen.get_height() / 2)
        self.gameManager.screen.blit(self.buttonSurface, self.buttonRect)

        self.mouseHovering = False

        self.clickCooldown = 0.5
        self.futureTime = time.time() + self.clickCooldown

    def update(self):
        self.check_mouse_hovering()
        self.input()

    def draw(self):
        # text
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = "Resume"
        textSurface = font.render(text, True, (255, 255, 255))
        textRect = textSurface.get_rect()
        textRect.centerx = int(self.gameManager.screen.get_width() / 2)

        self.buttonSurface.blit(textSurface, textRect)

        # button
        self.gameManager.screen.blit(self.buttonSurface, self.buttonRect)

    def check_mouse_hovering(self):
        if(pygame.mouse.get_pos()[0] > self.buttonRect.left and pygame.mouse.get_pos()[0] < self.buttonRect.right):
            if (pygame.mouse.get_pos()[1] > self.buttonRect.top and pygame.mouse.get_pos()[1] < self.buttonRect.bottom):
                self.mouseHovering = True
                return

        self.mouseHovering = False

    def input(self):
        if(pygame.mouse.get_pressed()[0] == 1 and self.mouseHovering and self.futureTime < time.time()):
            print("button clicked!")
            self.gameManager.paused = False
            self.futureTime = time.time() + self.clickCooldown

