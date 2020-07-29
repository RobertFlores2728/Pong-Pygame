import sys, pygame

pygame.init()



def main():
    screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
    clock = pygame.time.Clock()

    blue = (100, 100, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)

    paddleRect = pygame.Rect(0, 0, 50, 200)
    paddleSpeed = 20

    ballRect = pygame.Rect(int(screen.get_width() / 2), int(screen.get_height() / 2), 20, 20)
    ballDirectionX = 1  # should be 1 or -1 only. ball either goes left or right
    ballDirectionY = 1  # can be a number with greater fidelity. dictates curve of ball
    ballSpeed = 10  # speed will increase with each hit

    while True:
        clock.tick(120)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            print("p was pressed!")
        # Move paddle
        if keys[pygame.K_w]:
            paddleRect.y -= paddleSpeed
        if keys[pygame.K_s]:
            paddleRect.y += paddleSpeed

        # paddle boundaries check
        if paddleRect.y < 0:
            paddleRect.y = 0
        elif paddleRect.y > screen.get_height() - paddleRect.height:
            paddleRect.y = screen.get_height() - paddleRect.height


        # ball boundaries check, bounce around walls
        if ballRect.x > screen.get_width() - ballRect.width:
            ballDirectionX = -ballDirectionX
        if ballRect.x < 0:
            ballDirectionX = -ballDirectionX
        if ballRect.y > screen.get_height() - ballRect.height:
            ballDirectionY = -ballDirectionY
        if ballRect.y < 0:
            ballDirectionY = -ballDirectionY




        # Update screen
        pygame.display.flip()
        screen.fill(blue)

        # draw paddle
        pygame.draw.rect(screen, black, paddleRect)


        # move ball
        ballRect.x += ballDirectionX * ballSpeed
        ballRect.y += ballDirectionY * ballSpeed

        # draw ball
        pygame.draw.rect(screen, white, ballRect)

        # check collision
        if paddleRect.colliderect(ballRect):
            ballDirectionX = -ballDirectionX
            print("Collision!")



    return



main()
