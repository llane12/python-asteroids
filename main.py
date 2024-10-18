import pygame
from sys import exit
from constants import *
from player import *
from asteroid import *
from asteroidfield import *


def main():
    init_result = pygame.init()
    print("Starting asteroids!")
    print(f"pygame init result: {init_result}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # logic
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            for bullet in bullets:
                if bullet.collides_with(asteroid):
                    bullet.kill()
                    asteroid.split()

            if asteroid.collides_with(player):
                print("Game over!")
                exit()

        # rendering
        screen.fill((10, 10, 10))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
