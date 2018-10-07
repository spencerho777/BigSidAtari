HEIGHT = 720
WIDTH = 1280

class Bouncer:
    
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 40
        self.w = 200
        self.h = 10
        
    def drawBouncer(self):
        
        fill(0, 102, 153)
        rectMode(CENTER)
        rect(self.x, self.y, self.w, self.h)
        
    def updateBouncer(self):
        
        self.x = mouseX
        
        
