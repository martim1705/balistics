 # corre a simulação

import pygame as py
from elements import Ball 
from physics import *

height = 720
width = 720

mouse_location = (0,0)

ball_list = []

py.init()
screen = py.display.set_mode((width, height))
clock = py.time.Clock()

running = True

while (running):

    dt = clock.get_time() / 1000.0   
    screen.fill("black")

    mouse_location = py.mouse.get_pos()

    # for balls in ball_list:

    for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            elif event.type == py.MOUSEBUTTONDOWN:
                ball_list.append(Ball(radius=30, pos_x = mouse_location[0], pos_y = mouse_location[1], mass=40))
                
        # y = y0 + v0 * t - (g * t**2) / 2
    for ball in ball_list:

        if (ball.pos_y + ball.radius >= height):
             ball.pos_y = height - ball.radius
             if (ball.v_y > 0):  
                ball.v_y = - ball.v_y

             ball.pos_y += (g * dt * dt) / 2.0 + ball.v_y * dt
             
             # print("collision")
        else:
            ball.pos_y += (g * dt * dt) / 2.0 + ball.v_y * dt
            ball.v_y += g * dt
        py.draw.circle(surface= screen, center=(ball.pos_x, ball.pos_y) ,radius = ball.radius, color="yellow")        

    py.display.flip()
    clock.tick(60)

    


py.quit()

