from gameObject import GameObject
class Shot(GameObject):
    
    def __init__(self, positionx, positiony, direction, surface):
        super(Shot, self).__init__()
        self.set_surface(surface)
        self.create()
        self.set_position(positionx, positiony)
        self.direction = direction
        self.create()
        
    def create(self): 
            
        sx = 10
        sy = 10
        if self.direction == 'up':
            sy = -10
        elif self.direction == 'down':
            sy = 10
        elif self.direction == 'left':
            sx = -10
        elif self.direction == 'right':
            sx = 10
        
        print "Teste"
        return {
            'position': [x, y],
            'speed': {
                    'x': sx,
                    'y': sy
                }
        }

    #Move o tiro
    def move(self):
        s['position'][0] += s['speed']['x']
        s['position'][1] += s['speed']['y']

    