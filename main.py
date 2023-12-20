import pygame
import sys
import random

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Read file
with open("poomismang\lemmad.txt", encoding="cp1252") as f:
    words =  f.read().split('\n')

# Make difficulties
easy = [word for word in words if len(word) <= 4]
medium = [word for word in words if 4 < len(word) < 7]
hard = [word for word in words if len(word) > 6]

# Set up some constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    guess = self.text
                    self.text = ''  # Clear the input field
                    self.txt_surface = FONT.render(self.text, True, self.color)
                    return guess
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.display.update(self.rect)

def draw_game_state(word, guessed, wrong, attempts, screen):

    # Render the text
    text_surface = FONT.render("Sõna: " + ' '.join(letter if letter in guessed else '_' for letter in word), True, BLACK)

    # Draw the text on the screen
    screen.blit(text_surface, (20, 20))

    # Draw the wrong letters
    draw_wrong_letters(wrong, screen)

    # Draw the hangman
    # Add your hangman drawing code here
    
    # Update the display
    pygame.display.update()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

def draw_wrong_letters(wrong, screen):
    # Render the text
    wrong_text = ", ".join(wrong)
    text_surface = FONT.render("Valed katsed: " + wrong_text, True, BLACK)

    # Draw the text on the screen
    screen.blit(text_surface, (20, 60))  # Adjust the position as needed
    pygame.display.flip()  # Update the screen

def new_game(difficulty):
    running = True
    game_over = False
    attempts = 7  # Maximum number of incorrect guesses
    word = difficulty[random.randint(0, len(difficulty)-1)]
    guessed = []
    wrong = []

# Define the input box
    input_box = InputBox(100, 100, 140, 32)

# Define the submit button
    submit_button = pygame.Rect(250, 100, 100, 32)

# Define the back button
    back_button = pygame.Rect(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 100, 100, 50)

    while running:
        # Clear the screen
        screen.fill(WHITE)
        guess = None  # Initialize guess to None before the event loop

        for event in pygame.event.get():
            # Handle the event in the input box
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                guess = input_box.handle_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if game_over and back_button.collidepoint(event.pos):
                    menu()
                elif submit_button.collidepoint(event.pos) and guess is not None:  # If a guess was returned
                    if guess in word:
                        guessed.append(guess)
                        if all(letter in guessed for letter in word):
                            print(f"Tubli! Sa arvasid sõna ära! Sõna oli {word}.")
                            game_over = True
                    else:
                        attempts -= 1
                        wrong.append(guess)

            if guess is not None:  # If Enter was pressed
                if guess in word:
                    guessed.append(guess)
                    if all(letter in guessed for letter in word):
                        print(f"Tubli! Sa arvasid sõna ära! Sõna oli: {word}.")
                        game_over = True
                else:
                    attempts -= 1
                    wrong.append(guess)

            if attempts == 0:
                game_over_screen("lose", word)
            elif all(letter in guessed for letter in word):
                game_over_screen("victory", word)

        # Draw the input box
        input_box.draw(screen)

        # Draw the submit button
        draw_button("Sisesta", submit_button)

        # Draw the back button if the game is over
        if game_over:
            draw_button("Tagasi", back_button)

        # Draw the game state
        draw_game_state(word, guessed, wrong, attempts, screen)

    # Go back to the main menu after the game ends
    menu()

def game_over_screen(result, word):
    running = True

    # Define the back button
    back_button = pygame.Rect(0, 0, 220, 50)
    back_button.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    menu()

        # Clear the screen
        screen.fill(WHITE)

        # Display the game result
        result_text = "Sa võitsid! Õige sõna oli: " + word if result == "win" else "Sa kaotasid. Õige sõna oli: " + word
        draw_text(result_text, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

        # Draw the back button
        draw_button("Tagasi menüüsse", back_button)

        # Update the display
        pygame.display.update()

        # Cap the frame rate at 60 FPS
        clock.tick(60)

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

def draw_text(text, position):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=position)
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
                    # The 'Easy' button was clicked
                    new_game(easy)
                    running = False
                elif medium_button.collidepoint(mouse_pos):
                    # The 'Medium' button was clicked
                    new_game(medium)
                    running = False
                elif hard_button.collidepoint(mouse_pos):
                    # The 'Hard' button was clicked
                    new_game(hard)
                    running = False
                elif back_button.collidepoint(mouse_pos):
                    # The 'Back' button was clicked
                    return  # Go back to the main menu

        # Draw the difficulty selection
        draw_difficulty_selection(easy_button, medium_button, hard_button, back_button, mouse_pos)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS

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
                    # The 'Play' button was clicked
                    difficulty_selection()
                elif exit_button.collidepoint(mouse_pos):
                    # The 'Exit' button was clicked
                    running = False

        # Draw the menu
        draw_menu(play_button, exit_button, mouse_pos)

        # Update the display
        pygame.display.flip()
        clock.tick(60)  # Cap the frame rate at 60 FPS

    pygame.quit()
    sys.exit()

menu()
