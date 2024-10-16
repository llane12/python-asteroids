import pygame
from constants import *

def main():
    init_result = pygame.init()
    print("Starting asteroids!")
    print(f"pygame init result: {init_result}")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_loop(screen)

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((10, 10, 10))
        pygame.display.flip()

if __name__ == "__main__":
    main()
