HEIGHT = 720
WIDTH = 1280

class Sid():
    
    def __init__(self):
        
        self.sprite = loadImage("Sid.png")
        self.x = WIDTH // 2
        self.y = HEIGHT - 200
        self.d = 70
        self.r = self.d // 2
        self.movementX = 4
        self.originalY = 7
        self.movementY = 7
        self.velocity = PVector(0, self.movementY)
        self.diedAt = 0
        self.isMoving = True
        self.mouseControl = False
        self.blocksKilled = 0
        self.lives = 1
        
    def drawSid(self):
        
        imageMode(CENTER)
        image(self.sprite, self.x, self.y, self.d, self.d)
        
    def updateSid(self, bouncer, blocks):
        
        #print(self.x + self.r, self.x - self.r)
        #print(bouncer.x - bouncer.w // 2, bouncer.x + bouncer.w // 2)
        #print('\n')
        
        if self.isMoving:
            # Speed Increase
            self.movementY += 0.01
            
            # Bouncer Logic
            if ((self.y + self.r >= bouncer.y - bouncer.h // 2) and
            (self.x + self.r > bouncer.x - bouncer.w // 2) and
            (self.x - self.r < bouncer.x + bouncer.w // 2)):
                self.y = bouncer.y - bouncer.h // 2 - self.r
                self.velocity.y = -self.movementY
                ballDist = self.x - bouncer.x
                self.velocity.x = (ballDist / 100) * self.movementX * (self.movementY / self.originalY)
            
            # Right Wall    
            if self.x + self.r >= WIDTH:
                self.x = WIDTH - self.r
                self.velocity.x *= -1
            
            # Left Wall    
            if self.x - self.r <= 0:
                self.x = self.r
                self.velocity.x *= -1
            
            # Ceiling    
            if self.y - self.r <= 0:
                self.velocity.y *= -1
                self.y = self.r
            
            # Ground
            if self.y + self.r >= HEIGHT:
                self.lives -= 1
                self.resetSid()
    
            # Block Collision
            for block in blocks:
                testX = self.x
                testY = self.y
                
                if self.x < block.x - block.w // 2: testX = block.x - block.w // 2
                elif self.x > block.x + block.w // 2: testX = block.x + block.w // 2
                
                if self.y < block.y - block.h // 2: testY = block.y - block.h // 2
                elif self.y > block.y + block.h // 2: testY = block.y + block.h // 2
                
                distX = self.x - testX
                distY = self.y - testY
                distance = sqrt( (distX ** 2) + (distY ** 2) )
                
                if distance <= self.r:
                    boundaryX = self.r + block.w // 2
                    boundaryY = self.r + block.h // 2
                    #print(self.x - block.x)
                    #print(self.y - block.y)
                    
                    # Left wall
                    if self.x - block.x <= -boundaryX + 30 and self.x - block.x >= -boundaryX:
                        #print("left")
                        if self.velocity.x == -self.movementX:
                            self.velocity.y *= -1
                        else:
                            self.velocity.x = -self.movementX
                        block.banished = True
                    
                    # Right wall    
                    elif self.x - block.x >= boundaryX - 30 and self.x - block.x <= boundaryX:
                        #print("right")
                        if self.velocity.x == self.movementX:
                            self.velocity.y *= -1
                        else:
                            self.velocity.x = self.movementX
                        block.banished = True
                    
                    # Top wall    
                    elif self.y - block.y <= -boundaryY + 30 and self.y - block.y >= -boundaryY:
                        #print("up")
                        self.velocity.y = -self.movementY
                        block.banished = True
                    
                    # Bottom wall
                    elif self.y - block.y >= boundaryY - 30 and self.y - block.y <= boundaryY:
                        #print("down")
                        self.velocity.y = self.movementY
                        block.banished = True
                        
                    if block.banished:
                        self.blocksKilled += 1
                    
            if not self.mouseControl:
                self.x += self.velocity.x
                self.y += self.velocity.y
            else:
                self.x = mouseX
                self.y = mouseY
        else:
            if millis() - self.diedAt >= 2000:
                self.isMoving = True
                
            else:
                self.x = mouseX
            
    def resetSid(self):
        self.movementY = self.originalY
        self.isMoving = False
        self.x = mouseX
        self.y = HEIGHT - 200
        self.velocity = PVector(0, self.movementY)
        self.diedAt = millis()
