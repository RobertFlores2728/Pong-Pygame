import pygame,time

class Button:
    def __init__(self, gameManager, text, yPos, func):
        self.text = text

        self.gameManager = gameManager
        self.buttonSurface = pygame.Surface((150, 50))
        self.buttonSurface.fill((69, 16, 176))
        self.buttonRect = self.buttonSurface.get_rect()
        self.buttonRect.centerx = int(self.gameManager.screen.get_width() / 2)
        self.buttonRect.centery = yPos
        self.gameManager.screen.blit(self.buttonSurface, self.buttonRect)

        self.mouseHovering = False

        self.clickCooldown = 0.5
        self.futureTime = time.time() + self.clickCooldown

        self.func = func

    def update(self):
        self.check_mouse_hovering()
        self.input()

    def draw(self):
        # text
        font = pygame.font.SysFont('Comic Sans MS', 30)
        textSurface = font.render(self.text, True, (255, 255, 255))
        textRect = textSurface.get_rect()
        textRect.centerx = int(self.buttonSurface.get_width() / 2)

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
            self.func()
            self.futureTime = time.time() + self.clickCooldown

