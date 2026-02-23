import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init() # Initialize pygame
    clock = pygame.time.Clock() # Create a pygame clock object
    delta_time = 0 # Delta Time in seconds. Updates every tick
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Set pygame display to variables set in constant.py
    updatable = pygame.sprite.Group() # Create updatable group
    drawable = pygame.sprite.Group() # Create drawable group
    asteroids = pygame.sprite.Group() # Create asteroids group
    Player.containers = (updatable, drawable) # Add Player to updatable and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable) # Add Asteroid to asteroids, updatable, and drawable groups
    AsteroidField.containers = (updatable) # Add AsteroidField to updatable group
    asteroidfield = AsteroidField() # Create AsteroidField Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # Initiate a player object in the middle of the screen
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}") # Prints pygame version
    print(f"Screen width: {SCREEN_WIDTH}") # Prints screen width
    print(f"Screen height: {SCREEN_HEIGHT}") # Prints screen height
    

    while True: # Game loop
        log_state() # Call logger
        for event in pygame.event.get(): # For each event in pygame events...
            if event.type == pygame.QUIT: # If game is quit, end game loop
                return
        screen.fill("black") # Fill screen black
        updatable.update(delta_time) # Updates player movement
        for asteroid in asteroids: # For each asteroid in asteroids group...
            if asteroid.collides_with(player): # If asteroid collides with player...
                log_event("player_hit") # Log 'player_hit'
                print("Game over!") # Print 'Game Over'
                sys.exit() # Exit program
        for each in drawable: # For each drawable object...
            each.draw(screen) # Draw it on the screen
        pygame.display.flip() # Update display
        delta_time = (clock.tick(60)) / 1000 # Pause the game loop for 1/60th of a second. Runs game smoothly at 60FPS


if __name__ == "__main__": # Calls main only if the file is run directly, not imported
    main()