import pygame as pg
import math

pg.init()
screen = pg.display.set_mode((800,600))
blueship_png = pg.image.load('blueship.png')
redship_png = pg.image.load('redship.png')
ex1 = pg.image.load('ex1.gif')
ex2 = pg.image.load('ex2.gif')
ex3 = pg.image.load('ex3.gif')
ex4 = pg.image.load('ex4.gif')
missile_png = pg.image.load('missile.png')

blueship = []
redship = []
missile = []


for n in range(0,360):
    blueship.append(pg.transform.rotozoom(blueship_png,-n,0.12))
    redship.append(pg.transform.rotozoom(redship_png,-n,0.12))
    missile.append(pg.transform.rotozoom(missile_png,-n,0.12))

t0 = 0.001 * pg.time.get_ticks()
maxdt = 0.5 # time step limit to avoid jumps

pg.event.pump()
keys = pg.key.get_pressed()

running = True
while running:
    t = 0.001 * pg.time.get_ticks()
    dt = min(t - t0, maxdt)   # set maximum limit to dt

    for event in pg.event.get():
        if event.type == pg.QUIT: # Checking for quit
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE: # Checking if escape key is pressed
                running = False

    redship_position = [300,300]
    blueship_position = [500,300]
    redship_angle = 180
    blueship_angle = 0
    v = 200 # pixels/s
    
    if dt>0.0:
        t0 = t
        redship_position[0] = (redship_position[0] + math.cos(math.radians(redship_angle)) * v * dt) % 800
        redship_position[1] = (redship_position[1] + math.sin(math.radians(redship_angle)) * v * dt) % 600
        blueship_position[0] = (blueship_position[0] + math.cos(math.radians(blueship_angle)) * v * dt) % 800
        blueship_position[1] = (blueship_position[1] + math.sin(math.radians(blueship_angle)) * v * dt) % 600

        screen.fill((0, 0, 0))  # Fill the screen with black
        #screen.blit(redship[int(redship_angle) % 360], redship_position)
        #screen.blit(blueship[int(blueship_angle) % 360], blueship_position)
        screen.blit(redship[int(redship_angle) % 360], (redship_position[0] - redship[int(redship_angle) % 360].get_width() // 2, redship_position[1] - redship[int(redship_angle) % 360].get_height() // 2))
        screen.blit(blueship[int(blueship_angle) % 360], (blueship_position[0] - blueship[int(blueship_angle) % 360].get_width() // 2, blueship_position[1] - blueship[int(blueship_angle) % 360].get_height() // 2))
    
        # Update the display
        pg.display.flip()
pg.quit()
