import pygame
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() # Initialize pygame
    clock = pygame.time.Clock() # Create a pygame clock object
    delta_time = 0 # Delta Time in seconds. Updates every tick
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set pygame display to variables set in constant.py
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Initiate a player object in the middle of the screen
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}") # Prints pygame version
    print(f"Screen width: {SCREEN_WIDTH}") # Prints screen width
    print(f"Screen height: {SCREEN_HEIGHT}") # Prints screen height
    

    while True: # Game loop
        log_state() # Call logger
        for event in pygame.event.get(): # Handle game events
            if event.type == pygame.QUIT: # If game is quit, end game loop
                return
        screen.fill("black") # Fill screen black
        updatable.update(delta_time) # Updates player movement
        for each in drawable: # Draw the player on the screen
            each.draw(screen)
        pygame.display.flip() # Update display
        delta_time = (clock.tick(60)) / 1000 # Pause the game loop for 1/60th of a second. Runs game smoothly at 60FPS


if __name__ == "__main__": # Calls main only if the file is run directly, not imported
    main()