import pygame 
from pygame import Vector2 

import Globals 
from vec2 import Vec2 
from my_constants import CELL_SIZE, MAP_SIZE
from my_sprite import MySprite  


INF = float('inf')
DIRECTIONS = ( Vec2(-1, 0), Vec2(1, 0), Vec2(0, -1), Vec2(0, 1) ) 


class Cell:
    EMPTY = 0 
    ENTRY_POINT = 1
    EXIT_POINT = 2

    TOWER = 3


class Map(MySprite):
    def __init__(self, parent):
        super().__init__(parent)
        self.cells = self.get_new_map(Cell.EMPTY)  

        self.initialise_pathfinding_stuff() 

        self.initialise_sprite() 
        self.children.add(GridLines(parent=self)) 
    
    def initialise_sprite(self):
        self._image = pygame.Surface(tuple(MAP_SIZE * CELL_SIZE), pygame.SRCALPHA).convert_alpha() 
        self.rect = self._image.get_rect() 

    def initialise_pathfinding_stuff(self):
        self.direction_to_go = self.get_new_map(DIRECTIONS[0])
        self.initialise_entry_exit_positions() 
        self.update_navigation() 
    
    def initialise_entry_exit_positions(self):
        mid_y = MAP_SIZE.y // 2
        self.entry_point = Vec2(0, mid_y) 
        self.exit_points = tuple([Vec2(MAP_SIZE.x - 1, mid_y - 3), Vec2(MAP_SIZE.x - 1, mid_y + 3) ])

        self.set_cell(self.entry_point, Cell.ENTRY_POINT) 
        for exit in self.exit_points:
            self.set_cell(exit, Cell.EXIT_POINT) 
        
    def update_navigation(self):
        cost = self.get_cost_map() 
        self.update_directions(cost) 
    
    def update_directions(self, cost_map):
        def cost(dir):
            cell = dir + Vec2(x, y)  
            if not self.is_valid_cell(cell):
                return INF 
            return cost_map[cell.x][cell.y] 

        for x in range(len(cost_map)):
            for y in range(len(cost_map[0])):
                self.direction_to_go[x][y] = min(
                    DIRECTIONS, 
                    key = cost 
                )
          
    def get_cost_map(self):
        cost = self.get_new_map(INF)  # Dikshara's Map 

        for exit_point in self.exit_points:
            queue = [exit_point] 
            queue_i = 0
            cost[exit_point.x][exit_point.y] = 0 

            while queue_i < len(queue):
                current = queue[queue_i] 
                cost_of_current = cost[current.x][current.y] 

                for direction in DIRECTIONS:
                    neibour = current + direction

                    if self.is_movement_allowed_on(neibour):
                        if cost[neibour.x][neibour.y] > cost_of_current + 1:
                            cost[neibour.x][neibour.y] = cost_of_current + 1 
                            queue.append(neibour) 
                
                queue_i += 1 

        return cost 
    

    def is_movement_allowed_on(self, cell):
        if self.is_valid_cell(cell):
            if self.cells[cell.x][cell.y] in (Cell.EMPTY, Cell.ENTRY_POINT, Cell.EXIT_POINT):
                return True 
        
        return False 

    def is_valid_cell(self, cell):
        return 0 <= cell.x < MAP_SIZE.x and 0 <= cell.y < MAP_SIZE.y 
    
    def get_new_map(self, initial_val):
        return [[initial_val] * MAP_SIZE.y for x in range(MAP_SIZE.x)] 

    def set_cell(self, pos, val):
        self.cells[pos.x][pos.y] = val 
        
    
        
class GridLines(MySprite):
    def __init__(self, parent):
        super().__init__(parent) 

        self._image = pygame.Surface(tuple(MAP_SIZE * CELL_SIZE), pygame.SRCALPHA).convert_alpha() 
        self.rect = self._image.get_rect() 

        self.draw_lines()

        Globals.game.UI.grid_toggle_button.func = self.toggle_visible 

    def draw_lines(self):
        color = pygame.Color(100, 100, 100, 200)
        
        # Horizontal Lines 
        for y in range(1, MAP_SIZE.y):
            pygame.draw.line(self._image, color,  
                Vector2(0, y) * CELL_SIZE,
                Vector2(MAP_SIZE.x, y) * CELL_SIZE
            )
        
        # Vertical Lines 
        for x in range(1, MAP_SIZE.x):
            pygame.draw.line(self._image, color,  
                Vector2(x, 0) * CELL_SIZE, 
                Vector2(x, MAP_SIZE.y) * CELL_SIZE
            )