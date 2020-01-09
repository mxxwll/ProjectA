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

global flagDict,flags
flagDict = {}
flags = ["otto","nl","eng","spa"]
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
    engCo = [x,y,w,w]
    nlCo = [x2,y,w,w]
    spaCo = [x,y2,w,w]
    ottoCo = [x2,y2,w,w]
    


    
def draw(players, playerNames):
    global flagDict,flags
    currentSpeler = s3.getCurrentPlayer()
    if currentSpeler == len(playerNames):
        setAllTaken()
    print(playerNames)    
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
    engCo = [x,y,w,w]
    nlCo = [x2,y,w,w]
    spaCo = [x,y2,w,w]
    ottoCo = [x2,y2,w,w]
    
    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    textSize(30)
    
    
    try:
        text(str(playerNames[currentSpeler]),width/2,height/8)
    except IndexError:
        print(flagDict)
        exit()
    text("Select your empire: ", width/2, height / 5)
        
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
        
    fill(134,122,91,63)
    rect(*backCo)
    fill(255,0,0,63)
    if "eng" in flags:
        rect(*engCo)
        text("ENG",engCo[0]+engCo[2]/2,engCo[1]+engCo[3]/2)
    if "nl" in flags:
        rect(*nlCo)
        text("VOC",nlCo[0]+nlCo[2]/2,nlCo[1]+nlCo[3]/2)
    if "spa" in flags:
        rect(*spaCo)
        text("SPA",spaCo[0]+spaCo[2]/2,spaCo[1]+spaCo[3]/2)
    if "otto" in flags:
        rect(*ottoCo)

        text("OTTO",ottoCo[0]+ottoCo[2]/2,ottoCo[1]+ottoCo[3]/2)  
    
    '''
    if 'eng' or 'nl' or 'spa' or 'otto' not in flagDict.keys():
            
        fill(255,0,0,63)
        rect(*engCo)
        rect(*nlCo)
        rect(*spaCo)
        rect(*ottoCo)
        fill(0)
        text("ENG",engCo[0]+engCo[2]/2,engCo[1]+engCo[3]/2)
        text("VOC",nlCo[0]+nlCo[2]/2,nlCo[1]+nlCo[3]/2)
        text("SPA",spaCo[0]+spaCo[2]/2,spaCo[1]+spaCo[3]/2)
        text("OTTO",ottoCo[0]+ottoCo[2]/2,ottoCo[1]+ottoCo[3]/2)  
        
    elif 'eng' in flagDict.keys():
        print("Triggered")
            #rect(*engCo)
        rect(*nlCo)
        rect(*spaCo)
        rect(*ottoCo)
        text("VOC",nlCo[0]+nlCo[2]/2,nlCo[1]+nlCo[3]/2)
        text("SPA",spaCo[0]+spaCo[2]/2,spaCo[1]+spaCo[3]/2)
        text("OTTO",ottoCo[0]+ottoCo[2]/2,ottoCo[1]+ottoCo[3]/2)
        flagTaken = True
            
    elif 'nl' in flagDict:
        rect(*engCo)
            #rect(*nlCo)
        rect(*spaCo)
        rect(*ottoCo)
        
        text("ENG",engCo[0]+engCo[2]/2,engCo[1]+engCo[3]/2)
        text("SPA",spaCo[0]+spaCo[2]/2,spaCo[1]+spaCo[3]/2)
        text("OTTO",ottoCo[0]+ottoCo[2]/2,ottoCo[1]+ottoCo[3]/2) 
            
    elif 'spa' in flagDict:
        rect(*engCo)
        rect(*nlCo)
        #rect(*spaCo)
        rect(*ottoCo)
        
        text("ENG",engCo[0]+engCo[2]/2,engCo[1]+engCo[3]/2)
        text("VOC",nlCo[0]+nlCo[2]/2,nlCo[1]+nlCo[3]/2)
        text("OTTO",ottoCo[0]+ottoCo[2]/2,ottoCo[1]+ottoCo[3]/2) 
            
            
    elif 'otto' in flagDict:
        rect(*engCo)
        rect(*nlCo)
        rect(*spaCo)
        
        text("ENG",engCo[0]+engCo[2]/2,engCo[1]+engCo[3]/2)
        text("VOC",nlCo[0]+nlCo[2]/2,nlCo[1]+nlCo[3]/2)
        text("SPA",spaCo[0]+spaCo[2]/2,spaCo[1]+spaCo[3]/2)
            #rect(*ottoCo)
    '''
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
    global i,flags,flagdict,posdict
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
    engCo = [x,y,w,w]
    nlCo = [x2,y,w,w]
    spaCo = [x,y2,w,w]
    ottoCo = [x2,y2,w,w]
    
    if isMouseInSpace(*engCo) or isMouseInSpace(*nlCo) or isMouseInSpace(*spaCo) or isMouseInSpace(*ottoCo):
        if "eng" in flags:
            if isMouseInSpace(*engCo):
                flagDict[playerNames[currentSpeler]] = "eng"
                s3.setCurrentPlayer(currentSpeler + 1)
                    
                #s3.setCurrentPlayer(currentPlayer + 1)
                #print(getCurrentPlayer())
                flags.remove("eng")
        if "nl" in  flags:    
            if isMouseInSpace(*nlCo):
                flagDict[playerNames[currentSpeler]] = "nl"
                s3.setCurrentPlayer(currentSpeler + 1)
                #print (str(flagDict[playerNames[currentPlayer]]))
                flags.remove("nl")
        if "spa" in flags:
            if isMouseInSpace(*spaCo):
                flagDict[playerNames[currentSpeler]] = "spa"
                s3.setCurrentPlayer(currentSpeler + 1)
                flags.remove("spa")
        if "otto" in flags:
            if isMouseInSpace(*ottoCo):
                flagDict[playerNames[currentSpeler]] = "otto"
                s3.setCurrentPlayer(currentSpeler + 1)
                flags.remove("otto")
        
            
    """

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
    """
