import pygame 
from pygame import Vector2 

from my_constants import CELL_SIZE, MAP_SIZE
from my_sprite import MySprite  

class Cell:
    EMPTY = 0 
    ENTRY_POINT = 1
    EXIT_POINT = 2

    TOWER = 3

class Map(MySprite):
    def __init__(self, parent):
        super().__init__(parent)
        self.cells = [[Cell.EMPTY] * MAP_SIZE.y for x in range(MAP_SIZE.x)] 

        self.initialise_sprite() 
    
    def initialise_sprite(self):
        self._image = pygame.Surface(tuple(MAP_SIZE * CELL_SIZE), pygame.SRCALPHA).convert_alpha() 
        self.rect = self._image.get_rect() 

        self.draw_lines()

    def draw_lines(self):
        color = pygame.Color(100, 100, 100, 200)
        
        # Horizontal Lines 
        for y in range(1, MAP_SIZE.y + 1):  # TODO:  + 1 doesn't work.. maybe, bcz it's out of self.image bound  ?
            pygame.draw.line(self._image, color,  
                Vector2(0, y) * CELL_SIZE,
                Vector2(MAP_SIZE.x, y) * CELL_SIZE
            )
        
        # Vertical Lines 
        for x in range(1, MAP_SIZE.x):
            pygame.draw.line(self._image, color,   # TODO:  choose btw  line and aaline
                Vector2(x, 0) * CELL_SIZE, 
                Vector2(x, MAP_SIZE.y) * CELL_SIZE
            )
    
    def toggle_visible(self):
        self.is_visible = not self.is_visible 

        
