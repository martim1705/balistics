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

        # floor 
        if (self.pos.y + self.radius >= height):
                     self.pos.y = height - self.radius
                     if (self.v.y > 0):  
                        self.v.y = - self.v.y * energy_loss
            

        elif (self.pos.y - self.radius <= 0):
             if (self.v.y < 0):
                  self.v.y = -self.v.y * 0.8

        # sides

        if (self.pos.x - self.radius <= 0):
             self.pos.x = self.radius
             if (self.v.x < 0):
                  self.v.x = -self.v.x * energy_loss
        elif (self.pos.x + self.radius >= width):
             self.pos.x = width - self.radius
             if (self.v.x > 0):
                  self.v.x = -self.v.x * energy_loss
        
        
    