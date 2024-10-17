import pygame
from circleshape import *
from constants import *
from bullet import *


# Class for player sprite
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.velocity = PLAYER_MOVE_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.__move(dt)
        if keys[pygame.K_s]:
            self.__move(-dt)
        if keys[pygame.K_a]:
            self.__rotate(-dt)
        if keys[pygame.K_d]:
            self.__rotate(dt)
        if keys[pygame.K_SPACE]:
            self.__shoot()

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.__triangle(), PLAYER_LINE_WIDTH)
    
    def __triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def __rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def __move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.velocity * dt

    def __shoot(self):
        bullet = Bullet(self.position.x, self.position.y, BULLET_RADIUS)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * BULLET_MOVE_SPEED
