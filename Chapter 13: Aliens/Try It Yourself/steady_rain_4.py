# 13-4. Steady Rain:        Modify your code in Exercise 13-3 so when a row of rain-drops disappears off the bottom of the screen, a new row appears at the top of the screen and begins to fall.

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
    row_list = []  # A row list to store all raindrops in that row
    for col in range(cols):
        x = col * (raindrop_width + padding_x)
        y = row * (raindrop_height + padding_y)
        row_list.append([x, y])
    raindrops.append(row_list)

# Speed at which the raindrops fall
fall_speed = 10

# Function to draw and animate raindrops
def draw_raindrops():
    for row in raindrops:
        # Update the y position for each raindrop in the row
        for drop in row:
            drop[1] += fall_speed

        # If the entire row of raindrops goes off the screen, reset the row to the top
        if row[0][1] > screen.get_height():  # Check the first raindrop in the row
            for drop in row:
                drop[1] = -raindrop_height  # Reset the entire row to the top

        # Draw each raindrop
        for drop in row:
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
