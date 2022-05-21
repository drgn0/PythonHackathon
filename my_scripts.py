class Vec2:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
    
    def __mul__(self, val):
        return Vec2(self.x * val, self.y * val) 
    
    def __rmul__(self, val):
        return Vec2(self.x * val, self.y * val)

    def __truediv__(self, val):
        return Vec2(self.x / val, self.y / val) 

    def __floordiv__(self, val):
        return Vec2(self.x // val, self.y // val) 

    def __add__(self, vec):
        assert(isinstance(vec, Vec2)) 
        return Vec2(
            self.x + vec.x, 
            self.y + vec.y 
        )
    
    def __sub__(self, vec):
        assert(isinstance(vec, Vec2))
        return Vec2(
            self.x - vec.x, 
            self.y - vec.y 
        )

    def __iter__(self):
        yield self.x 
        yield self.y 

    def __repr__(self) -> str:
        return str((self.x, self.y)) 


if __name__ == '__main__':
    x = Vec2(4, 2) 
    y = Vec2(5, 1) 
