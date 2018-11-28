from Bouncer import Bouncer
from Sid import Sid
from Block import Block
import random

HEIGHT = 720
WIDTH = 1280


def setup():
    
    global heavenBackground, hellBackground, happySid, sadSid, gameOver, bouncer, sid, blockList, gameStart, backgroundImage, backgroundImages, score
    size(WIDTH, HEIGHT)
    #pixelDensity(2)
    
    backgroundImages = [loadImage("Glacier 1.jpg"), loadImage("Glacier 2.jpg"), loadImage("Glacier 3.jpg")]
    backgroundImage = backgroundImages[0]
    happySid = loadImage("Happy Sid.png")
    sadSid = loadImage("Sad Sid.png")
    heavenBackground = loadImage("Clouds.jpg")
    hellBackground = loadImage("Hell.jpg")
    
    blockList = makeBlocks() #[Block(300, 300, 200, loadImage("Ice.jpg"))]# 
    bouncer = Bouncer()
    sid = Sid()
    
    gameStart = False
    sid.isMoving = False
    gameOver= False
    score = 0
    
def makeBlocks():
    global numberOfBlocks
    numberOfBlocks = 0
    blockSprite = loadImage("Ice.jpg")
    blocks = []
    
    spaceBetween = 5
    startLevel = 100
    levelSpace = 85
    for level in range(1, 5):
        levelBlocks = []
        blockSpace = 10
        while blockSpace <= WIDTH - spaceBetween:
            
            wid = random.randint(100, 200)
            
            #print(blockSpace + wid // 2, 65 * level, wid)
            levelBlocks.append(Block(blockSpace + wid // 2, startLevel + levelSpace * level, wid, blockSprite))
            numberOfBlocks += 1
            blockSpace += wid + spaceBetween
            if (WIDTH - spaceBetween) - blockSpace <= 300:
                numberOfBlocks += 1
                wid = (WIDTH - spaceBetween) - blockSpace
                levelBlocks.append(Block(blockSpace + wid // 2, startLevel + levelSpace * level, wid, blockSprite))
                break
        
        blocks.append(levelBlocks)
    
    #print(numberOfBlocks)
    return blocks
    
def draw():
    global blockList, score, gameOver
    
    if not gameOver:
        background(backgroundImage)
            
        for j in range(len(blockList)):
            i = 0
            while i < len(blockList[j]):
                if blockList[j][i].banished:
                    del blockList[j][i]
                    score += 10
                    
                else:
                    blockList[j][i].drawBlock()
                    i += 1
        
            
        bouncer.drawBouncer()
        sid.drawSid()
        
        if numberOfBlocks == sid.blocksKilled:
            transitionToNextLevel(sid)
            
            
        for k in range(sid.lives-1):
            imageMode(CENTER)
            image(sid.sprite, 50 + (k * 60), HEIGHT - 50, 50, 50)
        
        if gameStart: 
            bouncer.updateBouncer()
            
            if sid.y - sid.r <= 185 + 40: testBlocks = blockList[0] + blockList[1]
            elif sid.y - sid.r <= 270 + 40: testBlocks = blockList[1] + blockList[2]
            elif sid.y - sid.r <= 355 + 40: testBlocks = blockList[2] + blockList[3]
            else: testBlocks = blockList[3]
            
            sid.updateSid(bouncer, testBlocks)
        
        else:
            textSize(96)
            fill(255)
            textAlign(CENTER)
            text("Press Space to Start", WIDTH // 2, HEIGHT // 2)
            
        textSize(28)
        fill(255)
        textAlign(CENTER)
        text("Score: " + str(score), WIDTH - 100, HEIGHT - 20)
        
        if sid.lives == 0:
            gameOver = True
        
    else:
        drawGameOver(score)

def transitionToNextLevel(sid):
    global blockList, backgroundImage
    sid.resetSid()
    sid.blocksKilled = 0
    sid.lives += 1
    sid.originalY += 0.5
    blockList = makeBlocks()
    backgroundImage = backgroundImages[random.randint(0, len(backgroundImages) - 1)]

def drawGameOver(score):
    
    textSize(81)
    textAlign(LEFT)
    if score < 1000:
        background(hellBackground)
        image(sadSid, WIDTH - 175, 475)
        fill(255, 0, 14)
        text("Big Sid is Disappointed", 10, HEIGHT * 1 / 4)
        text("in Your Lack of Effort", 85, HEIGHT * 1 / 4 + 100)
        
    else:
        background(heavenBackground)
        image(happySid, WIDTH - 175, 475)
        fill(0, 102, 153)
        text("Big Sid is Exalted", 10, HEIGHT * 1 / 4)
        text("by Your Loyalty", 75, HEIGHT * 1 / 4 + 100)
        
    
    
            
#def mousePressed():
#    sid.mouseControl = not sid.mouseControl
    
def keyPressed():
    global gameStart
    gameStart = not gameStart
