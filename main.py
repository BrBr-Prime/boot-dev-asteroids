# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from circleshape import CircleShape

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print (f"{screen}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    print("Starting Asteroids!")
    while True:
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()



if __name__ == "__main__":
    main()
    