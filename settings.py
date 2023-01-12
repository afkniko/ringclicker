import random

class Settings:
    
    def __init__(self):
        
        # Set display
        width = 1200
        height = 800
        self.display_size = (width, height)
        self.bg_color = (0, 0, 0)
        
        # Size for target img
        # TODO Make img change size according to time/score
        target_w = 50 # Width
        target_h = 50 # Height
        self.target_size = (target_w, target_h)
        self.targets_spawned = 0
        
        # Set spawn delay
        self.spawn_delay = 1000
        
        # Score
        self.score = 0
        
        
    def target_spawn(self):
        # Target spawn points
        target_spawn = (random.randrange(50,1150),random.randrange(50,750))
        return target_spawn
        
    
    def update_speed(self):
        self.speed = self.speed