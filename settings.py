import pygame

class Settings:
    
    def __init__(self):
        
        # Set display
        width = 1200
        height = 800
        self.display_size = (width, height)
        self.bg = pygame.image.load("assets/bg.png")
        self.bg_over = pygame.image.load("assets/gameover.png")
        self.bg_start = (100, 50, 100)
        self.bg_game = (10, 120, 144)
        # Set start and over
        self.game_start = False
        self.game_over = False
        
        # Set font
        self.score_font = pygame.font.SysFont("monospace", 32)
        start_font = pygame.font.SysFont("monospace", 32)
        end_font = pygame.font.SysFont("monospace", 64)
        again_font = pygame.font.SysFont("monospace", 42)
        # Set FPS
        self.fps = 60

        self.score = 0
        self.count = 0
        self.click_count = 0
        self.start_text = start_font.render("Press 1 for 10 targets, 2 for 20 targets, 3 for 30 targets",1, (255, 255, 255))
        self.over_text = end_font.render("GAME OVER!",1, (0, 0, 0))
        self.again_text = again_font.render("Press 'SPACE' to play again! Q to quit",1, (0, 0, 0))


        # Set speed for spawning
        self.spawn_speed = 1
        
    def update_score(self):
        self.score += 1
        
    def update_speed(self, score):
        self.spawn_speed -= score*0.005