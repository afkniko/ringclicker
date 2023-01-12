import pygame
import sys
from settings import Settings

class RingClicker:
    
    def __init__(self):
        
        pygame.init()

        # Assign Settings
        self.settings = Settings()

        # Create window and set background color
        self.window = pygame.display.set_mode((self.settings.display_size))
        self.window.fill(self.settings.bg_color)
        self.clock = pygame.time.Clock()
        
        # Create custom event for spawning the targets
        self.target_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.target_event, self.settings.spawn_delay)
        
        # Load game image
        self.target = pygame.transform.scale(pygame.image.load("assets/ring1.bmp"), self.settings.target_size)

    def run_game(self):
        
        while True:
            
            # Track input
            self._check_events()

            # Update window
            self._update_window()
            
            #self.settings.counter += 1
            self.clock.tick(60)
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_q:
                          sys.exit()
                elif event.type == self.target_event:
                    self._spawn_targets()
                    
    # Update window helper
    def _update_window(self):
        
        pygame.display.flip()
    
    def _spawn_targets(self):
        self.window.blit(self.target, self.settings.target_spawn())

        
if __name__ == "__main__":
    RingClicker().run_game()