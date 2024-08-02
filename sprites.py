#Update alpha 0.2
import pygame as p
p.init()
size = [1320, 680]


class Bar():
    def __init__(self, screen, x, y, min, max, r = 0, g = 0, b = 255):
        self.screen = screen
        self.x, self.y = x, y
        self.r, self.g, self.b = r, g, b
        self.min, self.max = min, max
        self.range = max - min
        self.percent = self.range / 200
        self.range /= self.percent
    def render(self):
        p.draw.rect(self.screen, (0, 0, 0), (self.x - 5, self.y - 5, 210, 30))
        p.draw.rect(self.screen, (self.r, self.g, self.b), (self.x, self.y, self.range, 20))
    def damage(self, damage):
        if (self.range - damage > self.min-damage):
            self.range -= damage



class Worldmap ():
    def __init__(self, screen, bitmap, x, y, speed = 1):
        self.screen = screen
        self.bitmap = p.image.load(bitmap)
        self.x, self.y = x, y
        self.speed = speed
        self.out = False
    def render(self):
        self.screen.blit(self.bitmap,(self.x, self.y) )
    def move(self, speed, bar):
        self.speed = speed
        change = 1000
        keyp = p.key.get_pressed()
        if (bar.range > 0):
            if (keyp[p.K_w]):
                self.y += self.speed
                bar.damage(speed/change)
            if (keyp[p.K_a]):
                self.x += self.speed
                bar.damage(speed/change)
            if (keyp[p.K_s]):
                self.y -= self.speed
                bar.damage(speed/change)
            if (keyp[p.K_d]):
                self.x -= self.speed
                bar.damage(speed/change)
        else:
            self.out = True



class Player ():
    def __init__(self, screen, up, down, left, right):
        self.screen = screen
        self.up = p.image.load(up)
        self.down = p.image.load(down)
        self.left = p.image.load(left)
        self.right = p.image.load(right)
        self.bitmap = self.up
        self.height, self.width = self.bitmap.get_height(), self.bitmap.get_width()
    def move(self, bar):
        keyp = p.key.get_pressed()
        if (bar.range > 0):
            if (keyp[p.K_w]):
                self.bitmap = self.up
            if (keyp[p.K_a]):
                self.bitmap = self.left
            if (keyp[p.K_s]):
                self.bitmap = self.down
            if (keyp[p.K_d]):
                self.bitmap = self.right
        self.height, self.width = self.bitmap.get_height(), self.bitmap.get_width()
    def render(self):
        self.screen.blit(self.bitmap,(size[0]/2-self.width/2, size[1]/2-self.height/2))