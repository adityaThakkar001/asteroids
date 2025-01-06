import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ck = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2, radius = PLAYER_RADIUS, rotation = 180, timer = 0)
    AsteroidField(asteroids)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for dr in drawable:
            dr.draw(screen)
        for up in updatable:
            up.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot): 
                    asteroid.split() 
                    shot.kill()
            if asteroid.collides(player):
                return
        pygame.display.flip()
        ck.tick(60)
        dt = ck.get_time()/1000

if __name__ == "__main__":
    main()