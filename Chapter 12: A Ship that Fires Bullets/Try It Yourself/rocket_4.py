# 12-4. Rocket:         Make a game that begins with a rocket in the center of the screen. Allow the player to move the rocket up, down, left or right
#                       using the four arrow keys. Make sure the rocket never moves beyond any edge of the screen.

# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Load the rocket image
rocket = pygame.image.load(
    "Chapter 12: A Ship that Fires Bullets/Try It Yourself/rocket.bmp"
)
rocket = pygame.transform.scale(rocket, (100, 100))
rocket_rect = rocket.get_rect()
rocket_rect.center = screen.get_rect().center

moving_right = False
moving_left = False
moving_up = False
moving_down = False

rocket_speed = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            elif event.key == pygame.K_LEFT:
                moving_left = True
            elif event.key == pygame.K_UP:
                moving_up = True
            elif event.key == pygame.K_DOWN:
                moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            elif event.key == pygame.K_LEFT:
                moving_left = False
            elif event.key == pygame.K_UP:
                moving_up = False
            elif event.key == pygame.K_DOWN:
                moving_down = False

    if moving_right and rocket_rect.right < screen.get_rect().right:
        rocket_rect.x += rocket_speed
    if moving_left and rocket_rect.left > 0:
        rocket_rect.x -= rocket_speed
    if moving_up and rocket_rect.top > 0:
        rocket_rect.y -= rocket_speed
    if moving_down and rocket_rect.bottom < screen.get_rect().bottom:
        rocket_rect.y += rocket_speed

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE

    screen.blit(rocket, rocket_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
