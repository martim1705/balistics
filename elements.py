from physics import *
from vectors import *

GRAVITY = Vector2(0, g)

class Ball:

    def __init__(self, radius, pos_x, pos_y, mass,v_x = 0, v_y = 0):
        self.radius = radius
        self.pos = Vector2(pos_x, pos_y)
        self.mass = mass # kg
        self.v= Vector2(v_x, v_y)

    def update(self, dt, width, height):    

        self.pos += (GRAVITY * (dt * dt / 2.0)) + (self.v * dt)
        self.v += GRAVITY * dt

        if (self.pos.y + self.radius >= height):
                     self.pos.y = height - self.radius
                     if (self.v.y > 0):  
                        self.v.y = - self.v.y * energy_loss

        if (abs(self.v.y) < 5):
            self.v.y = 0
    