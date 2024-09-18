# 13-3. Raindrops:      Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall toward the bottom of the screen until they disappear.

import pygame
from random import randint

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 600))  # Adjust screen size as needed
clock = pygame.time.Clock()
running = True

# Load the raindrop image
raindrop_image = pygame.image.load("Chapter 13: Aliens/Try It Yourself/raindrop.png")

# Get the size of the raindrop image
raindrop_width, raindrop_height = raindrop_image.get_size()

# Create a list to store the positions of the raindrops in the grid
raindrops = []

# Number of rows and columns for the raindrop grid
rows = 5
cols = 8

# Padding between raindrops
padding_x = 20
padding_y = 20

# Set up the initial position of each raindrop in the grid
for row in range(rows):
    for col in range(cols):
        x = col * (raindrop_width + padding_x)
        y = row * (raindrop_height + padding_y)
        raindrops.append([x, y])

# Speed at which the raindrops fall
fall_speed = 5

# Function to draw and animate raindrops
def draw_raindrops():
    for drop in raindrops:
        # Update the y position to make the raindrop fall
        drop[1] += fall_speed

        # If the raindrop goes off the screen, reset it to the top
        if drop[1] > screen.get_height():
            drop[1] = -raindrop_height

        # Draw the raindrop
        screen.blit(raindrop_image, (drop[0], drop[1]))

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill the screen with black background

    draw_raindrops()  # Draw the raindrops and update their positions

    pygame.display.flip()  # Update display
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
