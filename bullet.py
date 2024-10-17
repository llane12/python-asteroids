import pygame
from circleshape import *
from constants import *


class Bullet(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, BULLET_RADIUS, BULLET_LINE_WIDTH)
