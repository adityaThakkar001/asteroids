# shot.py
import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.image = pygame.image.load('assets/shot.png').convert_alpha()
        bullet_width = SHOT_RADIUS * 4 
        bullet_length = SHOT_RADIUS * 6 
        self.original_image = pygame.transform.scale(self.image, (bullet_width, bullet_length))
        self.image = self.original_image
        self.rotation = rotation
        self.image = pygame.transform.rotate(self.original_image, -self.rotation + 90)
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        self.rect.center = self.position
        screen.blit(self.image, self.rect)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position