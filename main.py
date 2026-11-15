 # corre a simulação

import pygame as py
from elements import Ball


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
                # if (len(ball_list)) < 2:
                ball_list.append(Ball(radius=30, pos_x = mouse_location[0], pos_y = mouse_location[1], mass=40))
                # else:
                  #   continue

    for ball in ball_list:
        ball.update(dt, width, height)


    for i in range(len(ball_list)):
        for j in range(i + 1, len(ball_list)):
            ball_list[i].ball_collision(ball_list[j], 0.8)

    for ball in ball_list:
        py.draw.circle(surface= screen, center=(ball.pos.x, ball.pos.y) ,radius = ball.radius, color="yellow")        

    py.display.flip()
    clock.tick(60)

    


py.quit()

