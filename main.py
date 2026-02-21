import pygame
from constants import *
from logger import log_state

def main():
    pygame.init() # Initialize pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set pygame display to variables set in constant.py
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}") # Prints pygame version
    print(f"Screen width: {SCREEN_WIDTH}") # Prints screen width
    print(f"Screen height: {SCREEN_HEIGHT}") # Prints screen height
    
    while True: # Game loop
        log_state() # Call logger
        for event in pygame.event.get(): # Handle game events
            if event.type == pygame.QUIT: # If game is quit, end game loop
                return
        screen.fill("black") # Fill screen black
        pygame.display.flip() # Update display



if __name__ == "__main__": # Calls main only if the file is run directly, not imported
    main()