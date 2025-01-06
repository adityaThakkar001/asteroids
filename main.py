import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ck = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2, radius = PLAYER_RADIUS, rotation = 180)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for dr in drawable:
            dr.draw(screen)
        for up in updatable:
            up.update(dt)
        pygame.display.flip()
        ck.tick(60)
        dt = ck.get_time()/1000

if __name__ == "__main__":
    main()