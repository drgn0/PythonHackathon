import pygame 

from .button import Button 
from my_sprite import MySprite 

class UI(MySprite):
    def __init__(self, parent):
        self.initialise_sprite(parent)

        self.grid_toggle_button = Button((32, 32), parent = self) 
        self.grid_toggle_button.set_local_pos((600, 16))

        self.children.add(self.grid_toggle_button)
        

    def initialise_sprite(self, parent):
        super().__init__(parent = parent) 

        from my_constants import UI_SIZE, CELL_SIZE, UI_BACKGROUND_COLOR

        self._image = pygame.Surface(tuple(UI_SIZE * CELL_SIZE)) 
        self._image.fill(UI_BACKGROUND_COLOR)

        self.rect = self._image.get_rect() 
        # self.rect.top = MAP_SIZE.y * CELL_SIZE  # should be done in parent 
    
