import pygame 


from my_constants import * 

class Game:
    def __init__(self):
        pygame.init() 
        pygame.display.set_caption("..a game  ?") 

        self.main_screen = pygame.display.set_mode(SCREEN_SIZE_IN_PIXELS)
        self.clock = pygame.time.Clock() 

        from map import Map 
        self.map = Map() 

        self.stuff_to_draw = pygame.sprite.Group(self.map) 
    
    def game_loop(self):
        while True:
            exit_game = self.handle_events() 
            if exit_game:
                break 

            self.simulate_frame() 
    
    def handle_events(self):
        # returns whether game should be discontinued 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 
                return True 
        
        return False 
    
    def simulate_frame(self):
        self.update_stuff() 
        self.draw_stuff() 

        pygame.display.update() 
        self.clock.tick(FPS)
    
    def update_stuff(self):
        self.stuff_to_draw.update() 
    

    def draw_stuff(self):
        self.main_screen.fill(BACKGROUND_COLOR) 

        self.stuff_to_draw.draw(self.main_screen) 

if __name__ == '__main__':
    game = Game() 
    game.game_loop() 

