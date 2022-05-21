# from pygame import Vector2 
from my_scripts import Vec2 

CELL_SIZE = 32 
MAP_SIZE = Vec2(20, 15) 
SCREEN_SIZE = MAP_SIZE + Vec2(0, 2) 


SCREEN_SIZE_IN_PIXELS = tuple(SCREEN_SIZE * CELL_SIZE)


FPS = 75


BACKGROUND_COLOR = (60, 150, 70) 




from pygame import USEREVENT 
