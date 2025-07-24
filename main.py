# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import time
from constants import *
from asteroidfield import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid


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
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable, )
    player = Player(x, y)
    asteroidfield = AsteroidField()

    print("Starting Asteroids!")
    while True:
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        
        for drawable_object in drawable:
            drawable_object.draw(screen)
        
        updatable.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                time.sleep(2)
                sys.exit()

        pygame.display.flip()




if __name__ == "__main__":
    main()
    