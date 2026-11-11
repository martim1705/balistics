from physics import *

class Ball:

    def __init__(self, radius, pos_x, pos_y, mass,v_x = 0, v_y = 0):
        self.radius = radius
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.mass = mass # kg
        self.v_x = v_x
        self.v_y = v_y

    def update(self, dt, width, height):

        self.pos_y += (g * dt * dt) / 2.0 + self.v_y * dt
        self.v_y += g * dt

        if (self.pos_y + self.radius >= height):
                     self.pos_y = height - self.radius
                     if (self.v_y > 0):  
                        self.v_y = - self.v_y * energy_loss

        if (abs(self.v_y) < 5):
            self.v_y = 0
    