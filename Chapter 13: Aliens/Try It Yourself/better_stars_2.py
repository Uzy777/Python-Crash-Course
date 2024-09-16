# 13-2. Better Stars:       You can make a realistic star pattern by introducing randomness when you place each star. Recall from Chapter 9 that you can get a random number like this:
#
#                               from random import randint
#                               random_number = randint(-10, 10)
#
#                           This code returns a random integer between -10 and 10. Using your code in Exercise 13-1, adjust each star's position by a random amount.


import pygame
from random import randint

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
padding_x = (screen.get_width() - (image_width * 3)) // 4  # Padding between columns
padding_y = (screen.get_height() - (image_height * 3)) // 4  # Padding between rows

# Generate random offsets once and store them in a list
random_offsets = []
for row in range(3):
    for col in range(3):
        random_offset_x = randint(-100, 100)
        random_offset_y = randint(-100, 100)
        random_offsets.append((random_offset_x, random_offset_y))


# Function to draw the 3x3 grid without resizing, using stored random offsets
def draw_grid():
    for row in range(3):
        for col in range(3):
            x = padding_x + col * (image_width + padding_x)
            y = padding_y + row * (image_height + padding_y)

            # Get the pre-calculated random offset for this star
            random_offset_x, random_offset_y = random_offsets[row * 3 + col]

            # Draw the image at the grid cell position with the random offset
            screen.blit(image, (x + random_offset_x, y + random_offset_y))


# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill screen with white background
    draw_grid()  # Draw the 3x3 grid with images and fixed random offsets

    pygame.display.flip()  # Update display
    clock.tick(60)  # Cap the frame rate to 60 FPS

pygame.quit()
