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
        self.window.fill(self.settings.bg_color)
        self.clock = pygame.time.Clock()
        
        # Create custom event for spawning the targets
        self.target_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.target_event, self.targets.spawn_delay)
        self.target_list = []
        
    def run_game(self):
        
        
        while True:
            
            self._check_events()
            self.clock.tick(self.settings.fps)
            pygame.display.flip()
            
    
    def _check_events(self):
        
        for event in pygame.event.get():
            # Game ends  when 10 targets are in screen
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                            
                # TODO Destroy ring on click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if pygame.Rect(self.target.hitbox).collidepoint(event.pos[0], event.pos[1]):
                  
                        print("Hit")
                        self.target.kill()
                        self.window.blit(self.window, (self.target.rect.x, self.target.rect.y))
                        self.target.rm_obj()
                        self.window.fill(self.settings.bg_color)
                        self.settings.score += self.target.value

                            
                if event.type == self.target_event:
                    
                    self.window.fill(self.settings.bg_color)
                    self.target = self.targets.spawn_target()        
                    self.window.blit(self.targets.image, self.target)
                    self.settings.targets_on_screen += 1
            
             
                        
                
if __name__ == "__main__":
    RingClicker().run_game()