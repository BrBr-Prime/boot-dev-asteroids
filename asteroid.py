from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        width = 2
        color = "white"
        center = self.position
        radius = self.radius
        pygame.draw.circle(screen, color, center, radius, width)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = 0
        pygame.Vector2(0, 1)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
