from physics import *
from vectors import *

GRAVITY = Vector2(0, g)
FRICTION = Vector2(-1000.0, 0.0)
class Ball:

    def __init__(self, radius, pos_x, pos_y, mass,v_x = 0, v_y = 0):
        self.radius = radius
        self.pos = Vector2(pos_x, pos_y)
        self.mass = mass # kg
        self.v= Vector2(v_x, v_y)

    def update(self, dt, width, height):
    

        # ----------------------- collisions ------------------------- 


        # floor 
        if self.on_floor(height):
            
            self.pos.y = height - self.radius
            if (self.v.y > 0):  
                self.v.y = - self.v.y * energy_loss

            dir_X = 1 if self.v.x > 0 else -1 if self.v.x < 0 else 0
            old_vx = self.v.x
            acc = (GRAVITY + (FRICTION * dir_X))
            self.pos += ( acc * (dt * dt / 2.0)) + (self.v * dt)
            self.v += (acc) * dt
            if old_vx * self.v.x < 0:   # o atrito fê-la mudar de sentido → parou
                self.v.x = 0
            
        else:    
            # ceiling
            if (self.pos.y - self.radius <= 0):
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
            
            # between balls

            # ----------------------- movement -------------------------

            self.pos += (GRAVITY * (dt * dt / 2.0)) + (self.v * dt)
            self.v += GRAVITY * dt

    def ball_collision(self, other, e):

        if (abs((self.pos - other.pos).length()) <= (self.radius + other.radius)):
          n = other.pos - self.pos
          n_normalized = n.normalized()

          v_n_1_i = self.v.dot(n_normalized)
          v_n_2_i = other.v.dot(n_normalized)

          if (v_n_1_i - v_n_2_i > 0):
               v_n_1_f = (v_n_1_i + v_n_2_i - e * (v_n_1_i - v_n_2_i)) / 2
               v_n_2_f = (v_n_1_i + v_n_2_i + e * (v_n_1_i - v_n_2_i)) / 2 

               self.v.x += (v_n_1_f - v_n_1_i) * n_normalized.x
               self.v.y += (v_n_1_f - v_n_1_i) * n_normalized.y
               other.v.x += (v_n_2_f - v_n_2_i) * n_normalized.x
               other.v.y += (v_n_2_f - v_n_2_i) * n_normalized.y

    def on_floor(self, height):
        return (self.pos.y + self.radius >= height)

    def direction(self):
        speed = self.v.length()

        if speed == 0:
            return Vector2(0,0)
        return self.v.normalized()

