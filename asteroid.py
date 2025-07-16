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