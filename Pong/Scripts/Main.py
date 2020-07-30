import sys, pygame

from Scripts.Ball import Ball

pygame.init()




def main():
    screen = pygame.display.set_mode((1500, 1000))  # screen is a Surface object
    clock = pygame.time.Clock()

    # create ball object
    ball1 = Ball(screen)

    blue = (100, 100, 255)
    black = (0, 0, 0)
    white = (255, 255, 255)

    paddleRect = pygame.Rect(0, 0, 50, 200)
    paddleSpeed = 20

    ballRect = pygame.Rect(int(screen.get_width() / 2), int(screen.get_height() / 2), 20, 20)
    ballTravelX = 1  # should be 1 or -1 only. ball either goes left or right
    ballTravelY = 1  # 1 = greatest curve, 0 = straight
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




        # Update screen
        pygame.display.flip()
        screen.fill(blue)

        # draw paddle
        pygame.draw.rect(screen, black, paddleRect)



        # check paddle ball collision
        if paddleRect.colliderect(ballRect) and ballTravelX < 0:
            # get new y direction of ball
            ballTravelX = -ballTravelX
            ballTravelY = (ballRect.centery - paddleRect.centery)/100 # new y travel
            ballTravelX += 0.1 # new x travel
            if ballTravelX > 2.5:
                ballTravelX = 2.5
            print("Collision!")

        # ball boundaries check, bounce around walls
        if ballRect.x > screen.get_width() - ballRect.width:
            ballTravelX = -ballTravelX
        if ballRect.x < 0:
            ballTravelX = -ballTravelX
        if ballRect.y > screen.get_height() - ballRect.height:
            ballTravelY = -ballTravelY
        if ballRect.y < 0:
            ballTravelY = -ballTravelY

        # move ball
        ballRect.x += int(ballTravelX * ballSpeed)
        ballRect.y += int(ballTravelY * ballSpeed)

        # draw ball
        pygame.draw.rect(screen, white, ballRect)


        # move ball object
        ball1.move()

        # draw ball object
        ball1.draw()

    return



main()
