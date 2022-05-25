import pygame 

import Globals 
from my_constants import * 
from game_initialiser import GameInitialiser 


class Game(GameInitialiser):
    def __init__(self):
        Globals.game = self 
        super().__init__() 

    def get_global_pos(self):
        return pygame.Vector2(0, 0) 

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
        self.update() 
        self.draw() 

        pygame.display.update() 
        self.clock.tick(FPS)
    
    def update(self):
        self.visible_children = pygame.sprite.Group(filter(lambda sprite: sprite.is_visible, self.children))

        self.visible_children.update() 

    def draw(self):
        self.main_screen.fill(BACKGROUND_COLOR) 
        self.visible_children.draw(self.main_screen) 


if __name__ == '__main__':
    game = Game() 
    game.game_loop()

