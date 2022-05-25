import pygame 

from my_constants import * 


class GameInitialiser:
    # initialises everything in game. 
    # main Game class will inherit from it. 
    def __init__(self):
        pygame.init() 
        self.main_screen = pygame.display.set_mode(SCREEN_SIZE_IN_PIXELS)
        self.clock = pygame.time.Clock() 

        self.initialise_sprites() 
    
    def initialise_sprites(self):
        self.initialise_UI() 
        self.initialise_map() 

        self.children = pygame.sprite.Group(self.map, self.UI) 
    
    def initialise_map(self):
        from map import Map 

        self.map = Map(parent = self) 
    
    def initialise_UI(self):
        from user_interface.ui import UI 

        self.UI = UI(parent = self) 
        self.UI.set_local_pos((0, MAP_SIZE.y * CELL_SIZE))
        