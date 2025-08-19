from circleshape import CircleShape
from constants import *
from asteroid import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        color = "white"
        line_width = 2
        points = self.triangle()
        pygame.draw.polygon(screen, color, points, line_width)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        
        if keys[pygame.K_w]:
            self.move(dt, 1)

        if keys[pygame.K_s]:
            self.move(dt, -1)
        
        if keys[pygame.K_SPACE]:
            print("Spacebar pressed!")
            self.shoot()



    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN
        print("Shooting!")
        print(f"Player position: {self.position.x}, {self.position.y}")
        shot = Shot(self.position.x, self.position.y)
        print("Shot created successfully")
        velocity = pygame.Vector2(0, 1)
        velocity = velocity.rotate(self.rotation)
        velocity = velocity * PLAYER_SHOOT_SPEED
        shot.velocity = velocity
        print("Velocity set successfully")
