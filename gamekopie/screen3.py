import screen2
from screen2 import *

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
    
class screen3():
    def __init__(self):
        self.currentPlayer = 0
        
    def setCurrentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
    
    def getCurrentPlayer(self):
        return self.currentPlayer

    
def draw(playerNames):
    global s3, currentSpeler, p
    
    s3 = screen3()
    currentSpeler = s3.getCurrentPlayer()
    
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
    
    fill(255,0,0,63)
    rect(*oneCo)
    rect(*twoCo)
    rect(*threeCo)
    rect(*fourCo)

    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    
    fill(134,122,91,63)
    rect(*backCo)

    fill(0)
    
    # To-do: code schrijven in mousePressed van gamekopie (scherm == 3) en zo functions.py aanroepen.
    text("ENG",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
    text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
    text("SPA",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
    text("OTTO",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)  
    
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    
    s3 = screen3()
    
def isMouseInSpace(x, y, w, h):
    return(x < mouseX < x + w and y < mouseY < y + h)

def getCoordinates():
    return backCo

def getCurrentPlayer():
    global s3
    s3 = screen3()
    p = s3.getCurrentPlayer()
    return p

def mousePressed(playerNames, players):
   
    global posDict,flagDict
    flagDict = {}
    
    currentPlayer = getCurrentPlayer()
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
    
    if isMouseInSpace(*oneCo):
        flagDict[playerNames[currentPlayer]] = "eng"
        print(flagDict)
        #s3.setCurrentPlayer(currentPlayer + 1)
        #print(getCurrentPlayer())
        
    elif isMouseInSpace(*twoCo):
        flagDict[playerNames[currentPlayer]] = "nl"
        print(flagDict)
        #print (str(flagDict[playerNames[currentPlayer]]))
    elif isMouseInSpace(*threeCo):
        flagDict[playerNames[currentPlayer]] = "spa"
        print(flagDict)
    elif isMouseInSpace(*fourCo):
        flagDict[playerNames[currentPlayer]] = "otto"
        print(flagDict)
        

    """

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
