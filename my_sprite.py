import pygame 


class MySprite(pygame.sprite.Sprite):  
    def __init__(self, parent):
        super().__init__() 

        self.parent = parent 
        self.is_visible = True 
    
        self._image : pygame.Surface = None 

        self.children = pygame.sprite.Group() 
        self.visible_children = pygame.sprite.Group() 

    def get_global_pos(self):
        return self.rect.topleft + self.parent.get_global_pos() 
    
    def get_global_rect(self):
        return pygame.Rect(self.get_global_pos(), self.rect.size) 

    def update(self):
        visible_children = pygame.sprite.Group(filter(lambda sprite: sprite.is_visible, self.children)) 
        visible_children.update() 
    
        if len(self.children):
            self.image = self._image.copy() 
            visible_children.draw(self._image)  
        else:
            self.image = self._image 
            
    def set_local_pos(self, pos):
        self.rect.topleft = pos 