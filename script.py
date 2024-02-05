import pygame

# pygame setup
pygame.init()
window = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
gameRunning = True
deltaTime = 0


def DrawRobot(location, color, neckLength, bodyLength, bodyWidth):
    pygame.draw.rect(window, color,
                     pygame.Rect(location.x - (bodyWidth/2), (location.y - bodyLength/2),
                                 bodyWidth, bodyLength), )

while gameRunning:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False

    # fill the window with a color to wipe away anything from last frame
    window.fill("purple")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(window, "blue", pygame.Vector2(0, 0), 50)
    DrawRobot(pygame.Vector2(0, 0), "red", 10, 100, 20)
    # flip the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # 60 fps
pygame.quit()