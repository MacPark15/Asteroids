import pygame
import sys

pygame.font.init()
font = pygame.font.SysFont('Arial', 24)

class Score:
    def __init__(self):
        self.score = 0

    def draw(self, screen): # Draws the score to the screen
        text = font.render(f"Score: {self.score}", True, "white")
        screen.blit(text, (10, 5))

    def add(self, points): # Updates score
        self.score += points
