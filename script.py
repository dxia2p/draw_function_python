import pygame

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
gameRunning = True
deltaTime = 0


def DrawRobot(location, color, color2, neckLength, bodyLength, bodyWidth):
    neckWidth = bodyWidth / 10 # the neck width will be hard coded to 10% the body width
    wheelRadius = bodyWidth / 3
    stripeWidth = 10 # this is the strip in the middle of the robot's body
    eyeRadius = bodyWidth / 8
    eyeOffset = bodyWidth / 4 # this is how much the eye will be offset to the right, right now it is 25% of the body's width
    pygame.draw.circle(window, color2, pygame.Vector2(location.x, location.y + bodyLength / 2), wheelRadius) # this draws the wheel of the robot
    pygame.draw.rect(window, color, pygame.Rect(location.x - (bodyWidth/2), (location.y - bodyLength/2),
                                bodyWidth, bodyLength)) # This is the body of the robot
    pygame.draw.rect(window, color, pygame.Rect(location.x - (neckWidth / 2), (location.y - neckLength),
                                neckWidth, neckLength)) # this is the neck of the robot
    pygame.draw.rect(window, color2, pygame.Rect(location.x - (bodyWidth/2), (location.y - bodyLength/2 + 20),
                                               bodyWidth, stripeWidth)) # the stripe will always be 20 pixels from the top of the body
    pygame.draw.circle(window, color2, pygame.Vector2(location.x, 
                                location.y - neckLength - bodyWidth / 2), bodyWidth / 2) # this is the head of the robot THE CENTER OF THE CIRCLE IS WHERE THE NECK ENDS
    pygame.draw.circle(window, "white", pygame.Vector2(location.x + eyeOffset, 
                                location.y - neckLength - bodyWidth / 2), eyeRadius) # draw the eye


while gameRunning:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # fill the window with a color to wipe away anything from last frame
    window.fill("purple")

    # RENDER HERE
    pygame.draw.circle(window, "blue", pygame.Vector2(0, 0), 50)
    DrawRobot(pygame.Vector2(100, 200), "red", "blue", 100, 100, 60) # using the function to draw robots
    DrawRobot(pygame.Vector2(400, 300), "gray", "green", 150, 50, 30)
    DrawRobot(pygame.Vector2(700, 600), "yellow", "orange", 40, 65, 50)
    # flip the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # 60 fps
pygame.quit()