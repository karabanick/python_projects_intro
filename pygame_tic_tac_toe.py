import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Tic Tac Toe')

# Game variables
running = True

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle player move
            pass
    
    # Drawing the board and pieces
    screen.fill((255, 255, 255))  # Clear screen to white
    # Draw board and pieces here
    
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()
sys.exit()