# 13-1. Stars:      Find an image of a star. Make a grid of stars appear on the screen.

import pygame

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1200, 1200))  # Adjust screen size as needed
clock = pygame.time.Clock()
running = True

# Load the image (no resizing)
image = pygame.image.load("Chapter 13: Aliens/Try It Yourself/star.png")

# Get the size of the image to position it in the grid
image_width, image_height = image.get_size()

# Calculate padding and positions
# Center the grid within the window by calculating margins
padding_x = (screen.get_width() - (image_width * 3)) // 4  # Padding between columns
padding_y = (screen.get_height() - (image_height * 3)) // 4  # Padding between rows


# Function to draw the 3x3 grid without resizing
def draw_grid():
    for row in range(3):
        for col in range(3):
            x = padding_x + col * (image_width + padding_x)
            y = padding_y + row * (image_height + padding_y)
            screen.blit(image, (x, y))  # Draw image at the grid cell position


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill screen with white background
    draw_grid()  # Draw the 3x3 grid with images

    pygame.display.flip()  # Update display
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
