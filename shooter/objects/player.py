import pygame
from gameObject import GameObject
from shot import Shot
from pygame.locals import *



class Player(GameObject): 
    def __init__(self):     
        super(Player, self).__init__()
        self.speed = {'x': 0, 'y': 0}
        pass
    
    def movimenta_personagem(self):
        #Captura as teclas que o usuario apertou
        pressed_keys = pygame.key.get_pressed()

        #Realiza os tratamentos de aceleracao do jogador        
        self.speed = {'x': 0, 'y': 0}
        if pressed_keys[K_w]:
            self.speed['y'] = -7
        elif pressed_keys[K_s]:
            self.speed['y'] = 7

        if pressed_keys[K_a]:
            self.speed['x'] = -7
        elif pressed_keys[K_d]:
            self.speed['x'] = 7
            
        self.position['x'] += self.speed['x']
        self.position['y'] += self.speed['y']
        
    def atira(self):
        #Captura as teclas que o usuario apertou
        pressed_keys = pygame.key.get_pressed()
        direction = ""
        #Realiza os tratamentos de aceleracao do jogador
        if pressed_keys[K_UP]:
            direction = "up"
        elif pressed_keys[K_DOWN]:
            direction = "down"
        elif pressed_keys[K_LEFT]:
            direction = "left"
        elif pressed_keys[K_RIGHT]:
            direction = "right"
            
        s = Shot(self.position['x'], self.position['y'], direction, "../resources/shot.png")
    
    def update(self):
        self.movimenta_personagem()
        self.atira()