import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a function to draw the menu
def draw_menu():
    # Clear the screen
    screen.fill(WHITE)

    # Set up the font
    font = pygame.font.Font(None, 36)

    # Render the text
    text = font.render("Mängi", True, BLACK)
    
    # Calculate the position
    text_pos = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))

    # Draw the text on the screen
    screen.blit(text, text_pos)

    # Render the text
    text = font.render("Välju", True, BLACK)
    
    # Calculate the position
    text_pos = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    # Draw the text on the screen
    screen.blit(text, text_pos)

# Create a function to draw the game
def draw_game():
    # Clear the screen
    screen.fill(WHITE)

    # Set up the font
    font = pygame.font.Font(None, 36)

    # Render the text
    text = font.render("Game goes here", True, BLACK)
    
    # Calculate the position
    text_pos = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    # Draw the text on the screen
    screen.blit(text, text_pos)

# Create a function to handle the menu
def menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Here you can add code to handle button clicks
                pass

        # Draw the menu
        draw_menu()

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

menu()
