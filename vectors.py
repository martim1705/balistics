# VECTORS
from math import sqrt
class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, constant):
        return Vector2(self.x * constant, self.y * constant)

    def length(self):
        return round(sqrt(self.x*self.x + self.y * self.y),3)

    def normalized(self):
        
        if (self.x == 0):
            self.x = 0
        else:
            self.x = self.x / self.length()
        
        if (self.y == 0):
            self.y = 0
        else:
            self.y = self.y / self.length()
        return Vector2(self.x, self.y)

    def dot(self, other):
        return self.x * other.x + self.y * other.y


    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return f"({self.x}, {self.y})"
# teste
vector_test = Vector2(0,3)
other = Vector2(1,2)
print(-vector_test)