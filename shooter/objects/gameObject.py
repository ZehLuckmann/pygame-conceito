import pygame 

class GameObject(object):        
        
    def __init__(self):         
        print "OK"
        self.surface = None     
        self.position = {'x': 0, 'y': 0}
        
    def set_surface(self, surface_image):
        self.surface = pygame.image.load(surface_image).convert_alpha()    
        
    def set_position(self, x, y):
        self.position['x'] = x 
        self.position['y'] = y
    
    def get_position(self):
        return [self.position['x'], self.position['y']]
    