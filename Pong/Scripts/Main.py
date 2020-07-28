import sys, pygame

pygame.init()


def main():
    screen = pygame.display.set_mode((720, 480)) # screen is a Surface object

    blue = (100, 100, 255)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            print("p was pressed!")





        # Update screen
        screen.fill(blue)
        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 200, 200], 20)
        pygame.display.flip()





    return



main()
