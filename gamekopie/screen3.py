import screen2
from screen2 import *

class screen3:
    def __init__(self):
        self.currentPlayer = 0
        self.allTaken = False
    def setCurrentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
    
    def getCurrentPlayer(self):
        return self.currentPlayer
    
    def allTaken(self):
        self.allTaken = True
    
global s3
s3 = screen3()

global allTaken
allTaken = False

global flagDict
flagDict = {}

global allPlayersChosen
allPlayersChosen = False

global playerCount
playercount = ""

def setup():
    w = width/7          
    x = width/2-width/7-width/14
    y = height/3.5
    x2 = width/2 + width/14
    y2 = y + w + height/14
    
    
    global backCo
    backX = width/7
    backY = height-height/7
    backW = 250
    backH = 50
    backCo = [backX,backY,backW,backH]
    
    #1player
    oneCo = [x,y,w,w]
    twoCo = [x2,y,w,w]
    threeCo = [x,y2,w,w]
    fourCo = [x2,y2,w,w]
    


    
def draw(players, playerNames):
    
    currentSpeler = getCurrentPlayer()
    if currentSpeler == len(playerNames):
        setAllTaken()
        
    mainColor = color(234,222,191)
    background(mainColor)
    global s3, p
    i = 0
    
    
    f = createFont("Harrington",32)
    textFont(f,30) 
    
    w = width/7          
    x = width/2-width/7-width/14
    y = height/3.5
    x2 = width/2 + width/14
    y2 = y + w + height/14
    
    
    backX = width/7
    backY = height-height/7
    backW = 150
    backH = 50
    backCo = [backX,backY,backW,backH]
    
    #1player
    oneCo = [x,y,w,w]
    twoCo = [x2,y,w,w]
    threeCo = [x,y2,w,w]
    fourCo = [x2,y2,w,w]
    
    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    textSize(30)
    
    
    
    text(str(playerNames[currentSpeler]),width/2,height/8)
    text("Select your empire: ", width/2, height / 5)
        
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
        
    fill(134,122,91,63)
    rect(*backCo)
    
        
    if 'eng' or 'nl' or 'spa' or 'otto' not in flagDict.keys():
            
        fill(255,0,0,63)
        rect(*oneCo)
        rect(*twoCo)
        rect(*threeCo)
        rect(*fourCo)
        fill(0)
        text("ENG",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
        text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
        text("SPA",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
        text("OTTO",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)  
        
    elif 'eng' in flagDict.keys():
        print("Triggered")
            #rect(*oneCo)
        rect(*twoCo)
        rect(*threeCo)
        rect(*fourCo)
        text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
        text("SPA",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
        text("OTTO",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)
        flagTaken = True
            
    elif 'nl' in flagDict:
        rect(*oneCo)
            #rect(*twoCo)
        rect(*threeCo)
        rect(*fourCo)
        
        text("ENG",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
        text("SPA",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
        text("OTTO",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2) 
            
    elif 'spa' in flagDict:
        rect(*oneCo)
        rect(*twoCo)
        #rect(*threeCo)
        rect(*fourCo)
        
        text("ENG",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
        text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
        text("OTTO",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2) 
            
            
    elif 'otto' in flagDict:
        rect(*oneCo)
        rect(*twoCo)
        rect(*threeCo)
        
        text("ENG",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
        text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
        text("SPA",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
            #rect(*fourCo)
    
    #if playerNames[currentSpeler] == "":
        #allPlayersChosen()
        
def isMouseInSpace(x, y, w, h):
    return(x < mouseX < x + w and y < mouseY < y + h)

def getCoordinates():
    return backCo

def getAllTaken():
    return s3.allTaken
    
def setAllTaken():
    s3.allTaken = True
    
def getCurrentPlayer():
    global p
    p = s3.getCurrentPlayer()
    return p

def setCurrentPlayer(currentPlayer):
    s3.setCurrentPlayer(currentPlayer)


def mousePressed(playerNames, players):
    global i 
    i = 0 
    #global posDict,flagDict
    #flagDict = {}
    
    currentSpeler = getCurrentPlayer()
    
    w = width/7          
    x = width/2-width/7-width/14
    y = height/3.5
    x2 = width/2 + width/14
    y2 = y + w + height/14

    #1player
    oneCo = [x,y,w,w]
    twoCo = [x2,y,w,w]
    threeCo = [x,y2,w,w]
    fourCo = [x2,y2,w,w]
    
    if isMouseInSpace(*oneCo) or isMouseInSpace(*twoCo) or isMouseInSpace(*threeCo) or isMouseInSpace(*fourCo):
        if isMouseInSpace(*oneCo):
            flagDict[playerNames[currentSpeler]] = "eng"
            flagTaken = True
            if currentSpeler != len(playerNames):
                setCurrentPlayer(currentSpeler + 1)
            #s3.setCurrentPlayer(currentPlayer + 1)
            #print(getCurrentPlayer())
            
        elif isMouseInSpace(*twoCo):
            flagDict[playerNames[currentSpeler]] = "nl"
            flagTaken = True
            if currentSpeler != len(playerNames):
                setCurrentPlayer(currentSpeler + 1)
            #print (str(flagDict[playerNames[currentPlayer]]))
        elif isMouseInSpace(*threeCo):
            flagDict[playerNames[currentSpeler]] = "spa"
            flagTaken = True
            if currentSpeler != len(playerNames):
                setCurrentPlayer(currentSpeler + 1)
        elif isMouseInSpace(*fourCo):
            flagDict[playerNames[currentSpeler]] = "otto"
            setCurrentPlayer(currentSpeler + 1)
        
            
    """

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
