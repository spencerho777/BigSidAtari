HEIGHT = 720
WIDTH = 1280

class Block():
    
    def __init__(self, x, y, w, sprite):
        
        self.sprite = sprite
        self.x = x
        self.y = y
        self.w = w
        self.h = 80
        self.banished = False
        
    def drawBlock(self):
        rectMode(CENTER)
        fill(0)
        rect(self.x - 1, self.y - 1, self.w, self.h)
        imageMode(CENTER)
        image(self.sprite, self.x, self.y, self.w - 2, self.h - 2)
        
