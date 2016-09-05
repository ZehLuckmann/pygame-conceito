import pygame
from pygame.locals import *
from sys import exit
from gameObject import GameObject
from player import Player

class Scene(object):
    
    def __init__(self, name):  
        pygame.init()
        self.name = name     
        self.screen = None
        self.background = None
        self.game_objects = []
        self.clock = pygame.time.Clock()
    
    def set_video(self, width, height):
        self.screen = pygame.display.set_mode((width, height), 0, 32)
        pygame.display.set_caption(self.name)
            
    def set_background(self, background_filename):
        self.background = pygame.image.load(background_filename).convert()

    def add(self, game_object):
        self.game_objects.append(game_object)
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            self.screen.blit(self.background, (0, 0))
            
            for obj in self.game_objects:
                obj.update()
                self.screen.blit(obj.surface, obj.get_position())
            
            pygame.display.update()
            time_passed = self.clock.tick(30)
            
if __name__ == '__main__':    
    cenario = Scene('Fase 01')
    cenario.set_video(960, 560)
    cenario.set_background('../resources/bg.png')
    
    player = Player()
    player.set_position(100, 100)
    player.set_surface("../resources/player.png")
    
    print player.get_position() 
    cenario.add(player)
    
    cenario.start()