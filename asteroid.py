import pygame
import random
from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, ASTEROID_LINE_WIDTH)
    
    def split(self):
        self.kill()

        # this was a small asteroid, so it is now destroyed
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid1.velocity = vector1 * ASTEROID_MOVE_SPEED_INCREASE

        asteroid2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        asteroid2.velocity = vector2 * ASTEROID_MOVE_SPEED_INCREASE
