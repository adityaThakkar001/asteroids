import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from menu import Menu, Controls

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()  
        self.rect.left, self.rect.top = location

class GameState:
    MENU = "menu"
    GAME = "game"
    CONTROLS = "controls"

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    current_state = GameState.MENU
    
    menu = Menu()
    controls = Controls()
    background = Background('assets/stars_space_dark_139528_1280x720.jpg', [0,0])
    
    def init_game():
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (shots, updatable, drawable)
        
        player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2, 
                       radius=PLAYER_RADIUS, rotation=180, timer=0)
        AsteroidField(asteroids)
        
        return updatable, drawable, asteroids, shots, player
    
    game_objects = None
    dt = 0

    while True:
        screen.fill([0, 0, 0])
        screen.blit(background.image, background.rect)
        
        if current_state == GameState.MENU:
            menu.draw(screen)
            result = menu.handle_input()
            if result == 'play':
                current_state = GameState.GAME
                game_objects = init_game()
            elif result == 'controls':
                current_state = GameState.CONTROLS
            elif result == 'quit':
                return
                
        elif current_state == GameState.CONTROLS:
            controls.draw(screen)
            result = controls.handle_input()
            if result == 'menu':
                current_state = GameState.MENU
            elif result == 'quit':
                return
                
        elif current_state == GameState.GAME:
            updatable, drawable, asteroids, shots, player = game_objects
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        current_state = GameState.MENU
                        continue
            
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
                    current_state = GameState.MENU
                    break
        
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time()/1000

if __name__ == "__main__":
    main()