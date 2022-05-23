import pygame 

from my_sprite import MySprite 


class ButtonState:
    NOT_HOVERED_OVER = 0 
    HOVERED_OVER = 1 
    PRESSED = 2   

    colors = [(70, 70, 70), (64, 54, 60), (40, 40, 40)]  # corrospoinding to each state 

class Button(MySprite):
    original_color = pygame.Color(70, 70, 70) 
    pressed_color = pygame.Color(30, 30, 30) 

    def __init__(self, size, parent, func = None ):
        super().__init__(parent) 
    
        self._image = pygame.Surface(size)
        self.rect = self._image.get_rect() 

        self.state = None 
        self.func = func if func else default_func 
    

    def update(self):
        new_state = self.get_desired_state() 
        if self.state != new_state:
            self.check_press(new_state) 

            self.state = new_state 
            self.update_color() 
        
        super().update() 
    
    def get_desired_state(self):
        global_rect = self.get_global_rect() 
        mouse_pos = pygame.mouse.get_pos() 
        is_clicked = pygame.mouse.get_pressed()[0] 

        if not global_rect.collidepoint(mouse_pos):
            return ButtonState.NOT_HOVERED_OVER 
        
        # mouse is over button right now 
        return ButtonState.PRESSED if is_clicked else ButtonState.HOVERED_OVER 

    def check_press(self, new_state):
        if self.state == ButtonState.PRESSED and new_state == ButtonState.HOVERED_OVER:
            self.func() 

    def update_color(self):
        self._image.fill(ButtonState.colors[self.state]) 
        

def default_func():
    raise NotImplementedError("Button Click isn't bounded with any function.")