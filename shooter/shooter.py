import pygame
from pygame.locals import *
from sys import exit
from random import randrange

def create_shot(x, y, direction):
    sx = 0
    sy = 0
    if direction == 'up':
        sy = -10
    elif direction == 'down':
        sy = 10
    elif direction == 'left':
        sx = -10
    elif direction == 'right':
        sx = 10
        
    return {
        'surface': pygame.image.load('resources/shot.png').convert_alpha(),
        'position': [x, y],
        'speed': {
                'x': sx,
                'y': sy
            }
    }

#Move o tiro
def move_shots(shots):
    for s in shots:
        s['position'][0] += s['speed']['x']
        s['position'][1] += s['speed']['y']
    pass

#Destroi os tiros que estao fora do jogo
def remove_used_shots(shots):
    for s in shots:
        if (s['position'][1] > 560) or (s['position'][1] < -0) or (s['position'][0] > 956) or (s['position'][0] < -0):            
            shots.remove(s)
    pass

def main():
    #Inicia o objeto pygame
    pygame.init()
    
    #Configura o quadro
    screen = pygame.display.set_mode((956, 560), 0, 32)

    #Prepara o objeto do background
    background_filename = 'resources/bg.png'
    background = pygame.image.load(background_filename).convert()

    #Prepara o objeto da jogador 
    player = {
        'surface': pygame.image.load('resources/player.png').convert_alpha(),
        'position': [randrange(956), randrange(560)],
        'speed': {
                'x': 0,
                'y': 0
            }
    }
    
    
    #Titulo da tela
    pygame.display.set_caption('Caasi')
    #Captura o clock do jogo
    clock = pygame.time.Clock()        
    
    shots = []
    game_over = False

    while True:
        #Verifica se o usuario quer fechar a tela
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()                
                
        #Captura as teclas que o usuario apertou
        pressed_keys = pygame.key.get_pressed()

        #Realiza os tratamentos de aceleracao do jogador        
        player['speed'] = {'x': 0, 'y': 0}
        if pressed_keys[K_w]:
            player['speed']['y'] = -8
        elif pressed_keys[K_s]:
            player['speed']['y'] = 8

        if pressed_keys[K_a]:
            player['speed']['x'] = -8
        elif pressed_keys[K_d]:
            player['speed']['x'] = 8
        
        #Realiza os tratamentos de ataque do jogador        
        shot_direction = ''
        if pressed_keys[K_UP]:
            shot_direction = 'up'
        elif pressed_keys[K_DOWN]:
            shot_direction = 'down'
        elif pressed_keys[K_LEFT]:
            shot_direction = 'left'
        elif pressed_keys[K_RIGHT]:
            shot_direction = 'right'
            
        
        #Atualiza background
        screen.blit(background, (0, 0))    

        #Atualiza jogador
        if not game_over:
            player['position'][0] += player['speed']['x']
            player['position'][1] += player['speed']['y']
            screen.blit(player['surface'], player['position'])       
            
            if shot_direction != '':                
                shots.append(create_shot(player['position'][0], player['position'][1], shot_direction)   )
        
        #Atualiza tiros
        move_shots(shots)
        for s in shots:
            screen.blit(s['surface'], s['position'])
        
        remove_used_shots(shots);   
        
        #Atualiza tela
        pygame.display.update()
        #Define o limite do framerate
        time_passed = clock.tick(30)  
        
    pass


main()