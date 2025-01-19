import pygame
from constants import *

class Menu:
    def __init__(self):
        self.font_big = pygame.font.Font('assets\SF Distant Galaxy AltOutline.ttf', 115)
        self.font_small = pygame.font.Font('assets\Conthrax-SemiBold.otf', 45)
        self.options = ['Play', 'Controls', 'Quit']
        self.selected = 0
        
        self.title = self.font_big.render('ASTEROIDS', True, (255, 255, 0))
        self.title_rect = self.title.get_rect()
        
        self.texts = []
        self.text_rects = []
        self.selected_texts = []
        
        for option in self.options:
            text = self.font_small.render(option, True, (255, 255, 255))
            text_selected = self.font_small.render(option, True, (57, 255, 20))
            self.texts.append(text)
            self.selected_texts.append(text_selected)
            self.text_rects.append(text.get_rect())
    
    def draw(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        self.title_rect.centerx = screen_width // 2
        self.title_rect.top = screen_height // 4
        screen.blit(self.title, self.title_rect)

        for i, rect in enumerate(self.text_rects):
            rect.centerx = screen_width // 2
            rect.top = self.title_rect.bottom + i * 80 + 50
            
            if i == self.selected:
                screen.blit(self.selected_texts[i], rect)
            else:
                screen.blit(self.texts[i], rect)
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    if self.selected == 0:  
                        return 'play'
                    elif self.selected == 1:  
                        return 'controls'
                    elif self.selected == 2:
                        return 'quit'
        return None

class Controls:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.controls = [
            'CONTROLS:',
            'W - Thrust forward',
            'S - Thrust backward',
            'A - Rotate left',
            'D - Rotate right',
            'SPACE - Shoot',
            '',
            'Press ESC to return'
        ]
        self.texts = []
        self.text_rects = []
        
        for control in self.controls:
            text = self.font.render(control, True, (255, 255, 255))
            self.texts.append(text)
            self.text_rects.append(text.get_rect())
    
    def draw(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        for i, rect in enumerate(self.text_rects):
            rect.centerx = screen_width // 2
            rect.top = screen_height // 4 + i * 50
            screen.blit(self.texts[i], rect)
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 'menu'
        return None