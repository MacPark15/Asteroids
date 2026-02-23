import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def collides_with(self, other): # Checks for collision
        if self.position.distance_to(other.position) < (self.radius + other.radius): # If center to center position > radius of both
            return True # Collision
        else:
            return False # No Collision

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass