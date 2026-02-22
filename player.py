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