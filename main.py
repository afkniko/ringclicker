import pygame
import sys
from settings import Settings
from targets import Targets

class RingClicker:
    
    def __init__(self):
        
        pygame.init()

        # Assign Settings and Targets
        self.settings = Settings()
        self.targets = Targets()
        # Create window and set background color
        self.window = pygame.display.set_mode((self.settings.display_size))

        self.game = self.settings.bg
        self.over= self.settings.bg_over
        self.clock = pygame.time.Clock()
        self.target_count = 0
        self.target_exists = False
        # Hides cursor from screen
        #pygame.mouse.set_visible(False) 
        pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
        
    def run_game(self):
        
            self._start_game() 
            
            while True:   
                self._check_events()
                if self.settings.game_start: 
                    self._create_targets() 
                    self._destroy_target_timer()
                self._update_display()
                self.clock.tick(self.settings.fps)  
                self._game_over()         

                    
    def _check_events(self):
        
            for event in pygame.event.get():
                # Starts game by deciding target count with 1, 2 or 3
                if not self.settings.game_start and not self.settings.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.settings.game_start = True
                            self.target_count = 10
                            self._window_blit_game(self.game)
                        if event.key == pygame.K_2:
                            self.settings.game_start = True
                            self.target_count = 20
                            self._window_blit_game(self.game)    
                        if event.key == pygame.K_3:
                            self.settings.game_start = True
                            self.target_count = 30
                            self._window_blit_game(self.game)
                        if event.key == pygame.K_q:
                            sys.exit()
                        
                # While game running do this         
                if self.settings.game_start and not self.settings.game_over:
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                sys.exit()            
                    # When clicked, removes target with new background
                    # Probably there is a better way to do this.
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.settings.click_count += 1
                        if pygame.Rect(self.target.hitbox).collidepoint(event.pos[0], event.pos[1]):
                            self.settings.score += self.target.value
                            self.settings.update_speed(self.settings.score)
                            # Sets target_exists to false so next target could spawn
                            self.target_exists = False
                            self._window_blit_game(self.game)
                            
                # Let's user to play again with spacebar
                if not self.settings.game_start and self.settings.game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self._play_again()
                        else:
                            sys.exit()
       
                          
    def _update_display(self): 
        self._show_score()
        pygame.display.update()                      
    
    # Creates targets if no targets exists
    def _create_targets(self):
        if not self.target_exists :
            self.target = self.targets.spawn_target()
            self.window.blit(self.target.image, (self.target.rect.x, self.target.rect.y))
            self.start_ticks=pygame.time.get_ticks()
            self.target_count -= 1
            self.settings.count += 1
            self.target_exists = True
    
    # Helper to clear background  
    def _window_blit_game(self,bg):
        self.window.blit(bg, (0,0))
    
    # Shows score
    def _show_score(self):
        score = self.settings.score_font.render("Score:  " +str(self.settings.score),1, (0, 0, 0))
        self.window.blit(score, (10, 10))

                       
    # Remove target after delay time
    def _destroy_target_timer(self):
        if (pygame.time.get_ticks() - self.start_ticks)/1000 > self.settings.spawn_speed:
                self.target_exists = False
                self._window_blit_game(self.game) 
    # Ends game after target count reaches 0          
    def _game_over(self):
        if self.target_count < 0:
            self.settings.game_start = False
            self.settings.game_over = True
            self._window_blit_game(self.over)
            final_score = self.settings.score
            final_score_text = self.settings.score_font.render("You hit  " +str(final_score) +" targets and clicked "+ str(self.settings.click_count) + " times.",1, (0, 0, 0)) 
            self.window.blit(final_score_text, (200, 370) )
            self.window.blit(self.settings.over_text, (400, 400))
            self.window.blit(self.settings.again_text, (100, 460))
    
    # Creates background and start game text
    def _start_game(self):
        self.window.blit(self.game,(0,0))
       # self._window_fill_game(self.start)
        self.window.blit(self.settings.start_text, (50, 400))
     
    # Asks user to play again and sets variables to 0    
    def _play_again(self):
        self.settings.score = 0
        self.settings.game_over = False
        self.target_count = 0
        self.settings.click_count = 0
        self.start_ticks=pygame.time.get_ticks()
        self.run_game()
                    
if __name__ == "__main__":
    RingClicker().run_game()