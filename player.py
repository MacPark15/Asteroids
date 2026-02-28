import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y): # Initializes Player class with x and y arguments
        super().__init__(x, y, PLAYER_RADIUS) # Calls parent class and passes x, y, and PLAYER_RADIUS
        self.x = x
        self.y = y
        self.rotation = 0 # Sets Player rotation value
        self.shot_cooldown = 0 # Sets weapon cooldown
        self.current_speed = 0
        self.direction = ""
        self.move_cooldown = 0
    
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
        if self.current_speed < PLAYER_SPEED:
            self.current_speed += PLAYER_ACCELERATION
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * self.current_speed * dt
        #rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def decelerate(self, dt):
        if self.current_speed > 0:
            self.current_speed -= PLAYER_DECELERATION
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * self.current_speed * dt
        if self.direction == "forward":
            self.position += rotated_with_speed_vector
        else:
            self.position -= rotated_with_speed_vector

    def update(self, dt): # Updates player movement with key press
        self.shot_cooldown -= dt
        self.move_cooldown -= dt
        # KEYPRESSES
        keys = pygame.key.get_pressed()
        # MOVEMENT
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # If 'a' key pressed, rotate left
            self.rotate(dt * -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # If 'd' key pressed, rotate right
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]: # If 'w' key pressed, move forward
            self.move(dt) 
            self.direction = "forward"
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]: # If 's' key pressed, move backwards
            self.move(dt * -1)
            self.direction = "backward"
        else:
            self.decelerate(dt)
        # SHOOTING
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self): # Shoot method
        if self.shot_cooldown > 0:
            return
        else:
            self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS) # Create Shot object
        shot_vector = pygame.Vector2(0, 1) # Start with vector (0, 1)...
        shot_rotated_vector = shot_vector.rotate(self.rotation) # Add player rotation...
        shot.velocity = shot_rotated_vector * PLAYER_SHOOT_SPEED # Apply rotated vector * PLAYER_SHOOT_SPEED to shot velocity
