#Update alpha 0.2
import pygame as p
from sprites import *
import random
p.init()
playerFile = "G8_up.png"
playerFile2 = "G8_down.png"
playerFile3 = "G8_left.png"
playerFile4 = "G8_right.png"
mapFile = "Global_map(2).png"
# fulscreen size = [1370, 700]
size = [1320, 680]
window = p.display.set_mode(size)
p.display.set_caption("Dangerous World")
screen = p.Surface(size)
f1 = p.font.Font(None, 36)
f2 = p.font.Font(None, 100)
speed = 1
debug = False
todgle_shack = True
todgle_debug = True

wmap = Worldmap(screen, mapFile, -2300, -1300, speed)
player = Player(screen, playerFile, playerFile2, playerFile3, playerFile4)
hbar = Bar(screen, 50, 600, 0, 100, 255, 0, 0)
fbar = Bar(screen, 50, 640, 0, 10, 0, 255, 0)

def draw():
    #                          color       x     y    width   height
    #p.draw.rect(screen, (255, 255, 255), (0,    0,    200,    50))
    if (debug):
        p.draw.rect(screen, (255, 255, 255), (0, 0, 200, 50))
    p.draw.rect(screen, (150, 0, 150), (0, 580, 300, 100))

def render_text(f1, text, show, x, y):
    if (show):
        text1 = f1.render(str(text)  , 1, (0, 0, 0))
        screen.blit(text1, (x, y))

def render_all():
    wmap.render()
    draw()
    player.render()
    hbar.render()
    fbar.render()
    render_text(f1, (wmap.x, wmap.y), debug, 10, 10)
    render_text(f2, 'OUT OF FUEL!', wmap.out, 400, 100)

running = True    
while (running):
    for e in p.event.get():
        if (e.type == p.QUIT):
            running = False
        if (e.type == p.KEYDOWN):
            if (e.key == p.K_END):
                running = False
            if (e.key == p.K_h):
                if (todgle_shack):
                    speed = 10
                    todgle_shack = False
                else:
                    speed = 1
                    todgle_shack = True
            if (e.key == p.K_F3):
                if (todgle_debug):
                    debug = True
                    todgle_debug = False
                else:
                    debug = False
                    todgle_debug = True

    wmap.move(speed, fbar)
    player.move(fbar)
    
    screen.fill([64, 0, 64])
    render_all()
    window.blit(screen, [0, 0])
    p.display.flip()
    p.time.delay(2)
p.quit()
exit()