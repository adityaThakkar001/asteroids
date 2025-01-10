import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.original_image = pygame.image.load('assets/asteroid.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (radius * 2, radius * 2))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.rotation = 0
        self.rotation_speed = random.uniform(-50, 50)

    def draw(self, screen):
        self.image = pygame.transform.rotate(self.original_image, self.rotation)
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid1.velocity = self.velocity.rotate(angle) * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        asteroid2.velocity = self.velocity.rotate(-angle) * 1.2