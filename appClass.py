import sys
import pygame
from settings import *


vector = pygame.math.Vector2

class App():
    def __init__(self):
        self.screen = pygame.display.set_mode((Width, Height))
        self.clock = pygame.time.Clock()
        self.state = 'start'
        self.running = True
        self.intro = 'intro'
    def run(self):
        while self.running:
            if self.state =='start':
                self.intro_events()
                self.intro_update()
                self.intro_draw()
                self.clock.tick(FPS)    
        #pygame.quit()
        #sys.exit()

    def intro_events(self):
        
            #if event.type == pygame.QUIT():
                #self.running = False
        pass

    def intro_update(self):
        pass

    def intro_draw(self):
        for event in pygame.event.get():
            pygame.display.update()