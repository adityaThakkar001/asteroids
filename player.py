import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, radius, rotation, timer):
        super().__init__(x, y, radius)
        self.rotation = rotation
        self.timer = timer
        self.original_image = pygame.image.load('assets/ship.png').convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (radius * 3.5, radius * 3.5))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, screen):
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, self.rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.timer = PLAYER_SHOOT_COOLDOWN
                self.shoot(self.position)
        self.rect.center = self.position

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, position):
        shot = Shot(position.x, position.y, self.rotation)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED