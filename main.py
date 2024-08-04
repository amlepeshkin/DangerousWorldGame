#Update alpha 0.3
import pygame as p
from sprites import *
import math
p.init()
playerFile = "G8_up.png"
playerFile2 = "G8_down.png"
playerFile3 = "G8_left.png"
playerFile4 = "G8_right.png"
mapFile = "Global_map(2).png"
asteroidFile = "Asteroid.png"
# fulscreen size = [1370, 700]
size = [1320, 680]
window = p.display.set_mode(size)
p.display.set_caption("Dangerous World")
screen = p.Surface(size)
f1 = p.font.Font(None, 36)
f2 = p.font.Font(None, 100)
speed = 10
a = 0
b = 0
asteroid_number = 25
debug = False
todgle_shack = True
todgle_debug = True
asteroids = []

wmap = Worldmap(screen, mapFile, -2300, -1300, speed)
player = Player(screen, playerFile, playerFile2, playerFile3, playerFile4)
hbar = Bar(screen, 50, 600, 0, 100, 255, 0, 0)
fbar = Bar(screen, 50, 640, 0, 10, 0, 255, 0)
for _ in range(asteroid_number):
    #a = random.randint(0, 22000)
    #b = random.randint(0, 9000)
    a, b = rand(wmap)
    if (True):
        asteroids.append(Asteroid(screen, asteroidFile, a, b))

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
    for ast in asteroids:
        ast.render()
    draw()
    player.render()
    hbar.render()
    fbar.render()
    render_text(f1, (wmap.x, wmap.y), debug, 10, 10)
    render_text(f2, 'OUT OF FUEL!', (fbar.range <= fbar.min), 400, 100)
    render_text(f2, 'SPASESHIP IS BROKEN!', (hbar.range <= hbar.min), 300, 100)

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

    wmap.move(speed, fbar, hbar)
    player.move(fbar)
    for ast in asteroids:
        ast.move(wmap, fbar, hbar)
        if (intersect(size[0]/2-player.width/2, size[1]/2-player.height/2, ast.x+ast.width/2, ast.y+ast.height/2, ast.height/2)):
            hbar.damage(abs(ast.speed_x + ast.speed_y))
            ast.delete(wmap)
    
    screen.fill([64, 0, 64])
    render_all()
    window.blit(screen, [0, 0])
    p.display.flip()
    p.time.delay(2)
p.quit()
exit()