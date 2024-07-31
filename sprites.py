#Update alpha 0.1
import pygame as p
p.init()
size = [1320, 680]

class Worldmap ():
    def __init__(self, screen, bitmap, x, y, speed = 1):
        self.screen = screen
        self.bitmap = p.image.load(bitmap)
        self.x, self.y = x, y
        self.speed = speed
        #self.height, self.width = self.bitmap.get_height(), self.bitmap.get_width()
    def render(self):
        #self.screen.blit(p.transform.scale(self.bitmap, (int(self.bitmap.get_width()), int(self.bitmap.get_height()))), self.bitmap)
        self.screen.blit(self.bitmap,(self.x, self.y) )
    def move(self):
        keyp = p.key.get_pressed()
        if (keyp[p.K_w]):
            self.y += self.speed
        if (keyp[p.K_a]):
            self.x += self.speed
        if (keyp[p.K_s]):
            self.y -= self.speed
        if (keyp[p.K_d]):
            self.x -= self.speed
class Player ():
    def __init__(self, screen, up, down, left, right):
        self.screen = screen
        self.up = p.image.load(up)
        self.down = p.image.load(down)
        self.left = p.image.load(left)
        self.right = p.image.load(right)
        self.bitmap = self.up
        self.height, self.width = self.bitmap.get_height(), self.bitmap.get_width()
    def move(self, speed):
        keyp = p.key.get_pressed()
        if (keyp[p.K_w]):
            self.bitmap = self.up
        if (keyp[p.K_a]):
            self.bitmap = self.left
        if (keyp[p.K_s]):
            self.bitmap = self.down
        if (keyp[p.K_d]):
            self.bitmap = self.right
        self.speed = speed
        self.height, self.width = self.bitmap.get_height(), self.bitmap.get_width()
    def render(self):
        self.screen.blit(self.bitmap,(size[0]/2-self.width/2, size[1]/2-self.height/2))