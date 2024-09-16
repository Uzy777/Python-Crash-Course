# 12-5. Keys:       Make a Pygame file that creates an empty screen. In the event loop, print the 'event.key' attribute whenever a 'pygame.KEYDOWN'
#                   event is detected. Run the program and press various keys to see how Pygame responds.

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Close window event
            running = False
        elif event.type == pygame.KEYDOWN:  # Key press event
            print(event.key)  # Print the key code

    clock.tick(60)  # Limit FPS to 60

# Properly quit Pygame
pygame.quit()

