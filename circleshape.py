import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(self.containers)        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self, other_circle_shape):
        min = self.radius + other_circle_shape.radius
        distance = self.position.distance_to(other_circle_shape.position)
        return distance <= min
