#Update alpha 0.1
import pygame as p
from sprites import *
import random
p.init()
playerFile = "G8_up.png"
playerFile2 = "G8_down.png"
playerFile3 = "G8_left.png"
playerFile4 = "G8_right.png"
mapFile = "Global_map (2).png"
# fulscreen size = [1370, 700]
size = [1320, 680]
window = p.display.set_mode(size)
p.display.set_caption("Dangerous World")
screen = p.Surface(size)

speed = 1
todgle_shack = True

wmap = Worldmap(screen, mapFile, 0, 0, speed)
player = Player(screen, playerFile, playerFile2, playerFile3, playerFile4)

def worldmap():
    pass

def render_all():
    wmap.render()
    player.render()
running = True
worldmap()
screen.fill([64, 0, 64])
window.blit(screen, [0, 0])    
while (running):
    for e in p.event.get():
        if (e.type == p.QUIT):
            p.quit()
        if (e.type == p.KEYDOWN):
            if (e.key == p.K_END):
                p.quit()
            if (e.key == p.K_h):
                if (todgle_shack):
                    speed = 10
                    todgle_shack = False
                else:
                    speed = 1
                    todgle_shack = True
                player.move(speed)         
    wmap.move()
    player.move(speed)
    
    screen.fill([64, 0, 64])
    render_all()
    window.blit(screen, [0, 0])
    p.display.flip()
    p.time.delay(2)
p.quit()