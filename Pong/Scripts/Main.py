import sys, pygame

pygame.init()


def main():
    screen = pygame.display.set_mode((1500, 1000)) # screen is a Surface object
    clock = pygame.time.Clock()

    blue = (100, 100, 255)

    paddleRect = pygame.Rect(0, 0, 50, 200)
    paddleSpeed = 20

    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            print("p was pressed!")
        if keys[pygame.K_w]:
            paddleRect.y -= paddleSpeed
        if keys[pygame.K_s]:
            paddleRect.y += paddleSpeed

        if paddleRect.y < 0:
            paddleRect.y = 0
        elif paddleRect.y > screen.get_height() - paddleRect.height:
            paddleRect.y = screen.get_height() - paddleRect.height
        print(screen.get_height())



        # Update screen
        pygame.display.flip()
        screen.fill(blue)

        # draw
        pygame.draw.rect(screen, (0, 0, 0), paddleRect)






    return



main()
