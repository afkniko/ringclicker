import pygame

class Settings:
    
    def __init__(self):
        
        # Set display
        width = 1200
        height = 800
        self.display_size = (width, height)
        self.bg_color = (150, 150, 150)
        
        # Set font
        self.myfont = pygame.font.SysFont("monospace", 32)
        
        # Set FPS
        self.fps = 60
        # Score
        self.score = 10
        self.score_text = self.myfont.render("Score: " +str(self.score),1, (0, 0, 0))
        # Target count
        self.targets_in_list = 0
        self.targets_on_screen = 0

        self.targetsGroup = pygame.sprite.Group()

        
    def update_score(self):
        self.score += 1