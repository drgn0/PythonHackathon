from vec2 import Vec2 


CELL_SIZE = 32 
MAP_SIZE = Vec2(20, 15) 
UI_SIZE = Vec2(MAP_SIZE.x, 2)
SCREEN_SIZE = MAP_SIZE + Vec2(0, UI_SIZE.y) 


SCREEN_SIZE_IN_PIXELS = tuple(SCREEN_SIZE * CELL_SIZE)


FPS = 75


BACKGROUND_COLOR = (60, 150, 70) 
UI_BACKGROUND_COLOR = (50, 130, 60) 



from pygame import USEREVENT 
