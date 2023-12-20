import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a function to draw a button
def draw_button(text, rect):
    # Set up the font
    font = pygame.font.Font(None, 36)

    # Render the text
    text_surface = font.render(text, True, BLACK)

    # Create a rectangle for the text surface
    text_rect = text_surface.get_rect(center=rect.center)

    # Get the mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Check if the mouse is hovering over the button
    hover = rect.collidepoint(mouse_pos)

    # Draw the button
    if hover:
        pygame.draw.rect(screen, (200, 200, 200), rect)
    else:
        pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, BLACK, rect, 2)

    # Draw the text on the screen
    screen.blit(text_surface, text_rect)

# Create a function to draw the menu
def draw_menu(play_button, exit_button, mouse_pos):
    # Clear the screen
    screen.fill(WHITE)

    # Calculate the positions
    play_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 3 + 100)
    exit_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - SCREEN_HEIGHT // 3 + 170)

    # Draw the buttons
    draw_button("Mängi", play_button)
    draw_button("Välju", exit_button)

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

# Create a function to handle the difficulty selection
def difficulty_selection():
    running = True

    # Define the buttons
    easy_button = pygame.Rect(0, 0, 200, 50)
    medium_button = pygame.Rect(0, 0, 200, 50)
    hard_button = pygame.Rect(0, 0, 200, 50)
    back_button = pygame.Rect(0, 0, 200, 50)

    while running:
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click was within the buttons
                if easy_button.collidepoint(mouse_pos):
                    # The 'Kerge' button was clicked
                    new_game(kerge)
                    running = False
                elif medium_button.collidepoint(mouse_pos):
                    # The 'Paras' button was clicked
                    new_game(paras)
                    running = False
                elif hard_button.collidepoint(mouse_pos):
                    # The 'Raske' button was clicked
                    new_game(raske)
                    running = False
                elif back_button.collidepoint(mouse_pos):
                    # The 'Tagasi' button was clicked
                    return  # Go back to the main menu

        # Draw the difficulty selection
        draw_difficulty_selection(easy_button, medium_button, hard_button, back_button, mouse_pos)

        # Update the display
        pygame.display.flip()

def draw_difficulty_selection(easy_button, medium_button, hard_button, back_button, mouse_pos):
    # Clear the screen
    screen.fill(WHITE)

    # Calculate the positions
    easy_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
    medium_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    hard_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100)
    back_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    # Draw the buttons
    draw_button("Kerge", easy_button)
    draw_button("Paras", medium_button)
    draw_button("Raske", hard_button)
    draw_button("Tagasi", back_button)

# Create a function to handle the menu
def menu():
    running = True

    # Define the buttons
    play_button = pygame.Rect(0, 0, 200, 50)
    exit_button = pygame.Rect(0, 0, 200, 50)

    while running:
        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click was within the buttons
                if play_button.collidepoint(mouse_pos):
                    # The 'Mängi' button was clicked
                    difficulty_selection()
                elif exit_button.collidepoint(mouse_pos):
                    # The 'Välju' button was clicked
                    running = False

        # Draw the menu
        draw_menu(play_button, exit_button, mouse_pos)

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

menu()
