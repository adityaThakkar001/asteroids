import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = location

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
    BackGround = Background('assets\stars_space_dark_139528_1280x720.jpg', [0,0])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
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