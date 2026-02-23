import pygame
from constants import *
from circleshape import CircleShape

class Player(CircleShape):
    def __init__(self, x, y): # Initializes Player class with x and y arguments
        super().__init__(x, y, PLAYER_RADIUS) # Calls parent class and passes x, y, and PLAYER_RADIUS
        self.rotation = 0 # Sets Player rotation value
    
    def triangle(self): # Calculates triangle shape
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen): # Draws the player on the screen
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt): # Changes the player rotation based on PLAYER_TURN_SPEED in constants
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt): # Move player in direction of rotation
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def update(self, dt): # Updates player movement with key press
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # If 'a' key pressed, rotate left
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # If 'd' key pressed, rotate right
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]: # If 'w' key pressed, move forward
            self.move(dt) 
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # If 's' key pressed, move backwards
            self.move(dt * -1)