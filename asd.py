#1 utanför
#2 contour
#3 inne

import pygame
import sys
import numpy as np
import os

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (adjust as needed)
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Point Creator")

# Check for existing files
existing_files = os.listdir()
existing_indices = [int(file.split('.')[0]) for file in existing_files if file.endswith('.npy')]

# Determine the next available index for saving
if existing_indices:
    next_index = max(existing_indices) + 1
else:
    next_index = 1

# Create a mask to store points
mask = np.zeros((0, 3), dtype=np.int32)  # Initialize mask with 3 columns: x, y, value

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                point = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1]
                mask = np.append(mask, [point], axis=0)
            elif event.key == pygame.K_2:
                point = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 2]
                mask = np.append(mask, [point], axis=0)
            elif event.key == pygame.K_3:
                point = [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 3]
                mask = np.append(mask, [point], axis=0)
            elif event.key == pygame.K_s:
                np.save(f"{next_index}.npy", mask)
                next_index += 1
                running = False
            elif event.key == pygame.K_r:
                if mask.shape[0] > 0:
                    mask = np.delete(mask, -1, axis=0)

    # Fill the background with white
    screen.fill(WHITE)

    # Draw points on the screen
    for point in mask:
        if point[2] == 1:
            color = RED
        elif point[2] == 2:
            color = GREEN
        elif point[2] == 3:
            color = BLUE
        pygame.draw.circle(screen, color, (point[0], point[1]), 5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()