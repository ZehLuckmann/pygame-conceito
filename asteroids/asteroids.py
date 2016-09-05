import pygame
from pygame.locals import *
from sys import exit
from random import randrange

#Cria os asteroides
def create_asteroid(asteroids):
    return {
        'surface': pygame.image.load('asteroid.png').convert_alpha(),
        'position': [randrange(892), -64],
        'speed': randrange(10)
    }
    pass

#Move o Asteroide
def move_asteroids(asteroids):
    for asteroid in asteroids:
        asteroid['position'][1] += asteroid['speed']
    pass  

#Destroi os asteroides que estao fora do jogo
def remove_used_asteroids(asteroids):
    for asteroid in asteroids:
        if asteroid['position'][1] > 560:
            asteroids.remove(asteroid)
    pass

#Retorna area de colisao do objeto
def get_rect(obj):
    return Rect(obj['position'][0], obj['position'][1], 
                obj['surface'].get_width(), obj['surface'].get_height())
    pass

#Verifica a collisao entre os objetos
def ship_collided(ship, asteroids):
    ship_rect = get_rect(ship)
    for asteroid in asteroids:
        if ship_rect.colliderect(get_rect(asteroid)):
            return True
    return False
    pass

def main():
    #Inicia o objeto pygame
    pygame.init()
    
    #Configura o quadro
    screen = pygame.display.set_mode((956, 560), 0, 32)

    #Prepara o objeto do background
    background_filename = 'bg_big.png'
    background = pygame.image.load(background_filename).convert()

    #Prepara o objeto da nave 
    ship = {
        'surface': pygame.image.load('ship.png').convert_alpha(),
        'position': [randrange(956), randrange(560)],
        'speed': {
                'x': 0,
                'y': 0
            }
    }
    
    collided = False
    
    #Propriedades do  asteroide
    ticks_to_asteroid = 90
    asteroids = []

    #Titulo da tela
    pygame.display.set_caption('Asteroides')
    #Captura o clock do jogo
    clock = pygame.time.Clock()        
    
    while True:
        #Verifica se o usuario quer fechar a tela
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()                
        
        #reseta velocidade da nave
        ship['speed'] = {'x': 0, 'y': 0}
        
        if not ticks_to_asteroid:
            #Novo asteroide e reinicia a contagem
            ticks_to_asteroid = 90
            asteroids.append(create_asteroid(asteroids))
        else:
            #Diminui a contagem
            ticks_to_asteroid -= 1
            
        #Captura as teclas que o usuario apertou
        pressed_keys = pygame.key.get_pressed()

        #Realiza os tratamentos de aceleracao da nave
        if pressed_keys[K_UP]:
            ship['speed']['y'] = -5
        elif pressed_keys[K_DOWN]:
            ship['speed']['y'] = 5

        if pressed_keys[K_LEFT]:
            ship['speed']['x'] = -5
        elif pressed_keys[K_RIGHT]:
            ship['speed']['x'] = 5

        #Atualiza background
        screen.blit(background, (0, 0))    

        #Atualiza nave
        if not collided:
            collided = ship_collided(ship, asteroids)
            ship['position'][0] += ship['speed']['x']
            ship['position'][1] += ship['speed']['y']
            screen.blit(ship['surface'], ship['position'])       

        #Atualiza asteroides
        move_asteroids(asteroids)
        for asteroid in asteroids:
            screen.blit(asteroid['surface'], asteroid['position'])
        
        remove_used_asteroids(asteroids);
        
        #Atualiza tela
        pygame.display.update()
        #Define o limite do framerate
        time_passed = clock.tick(30) 
        
    pass


main()