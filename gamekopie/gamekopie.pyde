import screen0,screen1, screen2, screen3, handleiding,functions,game
import os


def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)

intro = True
game = False


def backSpace(s):
    try:
        s = list(s)
        del s[-1]
    except:
        return ""
    else:
        s = "".join(s)
        return s
    


def setup():
    size(1080,720)
    global players, playerNames
    playerNames = []
    global mainColor
    mainColor = color(234,222,191)
    global statBox
    statBox = [width-width/6, 1, width/6-2, height/3+height/7]
    
    global standardFont
    standardFont = createFont("Harrington",25)
    
    global phase
    phase = 0
    
    #phase 0
    global f, f1, f2
    global scherm, maincolor
    global schip, frame, handleiding1, handleiding2
    schip = loadImage("schip.png")
    frame = loadImage("frame.png")
    handleiding1 = loadImage("handleiding1.png")
    handleiding2 = loadImage("handleiding2.png")
    maincolor = color(234,222,191)
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",80)
    f2 = createFont("Harrington",30)
    scherm = 0
    
    global backCo
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    global w,x,y,x2,y2,players
    w = 90          
    x = 860
    y = 250
    x2 = x+100
    y2 = y+100
    players = ""
    
    global backCo
    backX = width/7
    backY = height-height/4
    backW = 250
    backH = 50
    backCo = [backX,backY,backW,backH]
    
    global contCo
    contX = width/7
    contY = height/4-height/20
    contW = 350
    contH = 100
    contCo = [contX,contY,contW,contH]
    
    global okCo
    okCoX = 750
    okCoY = 600
    okCo = [okCoX, okCoY, backW,backH]
    
    global guideCo
    guideX = width/7
    guideY = contY + contH + height/40
    guideW = 350
    guideH = 100
    guideCo = [guideX,guideY,guideW,guideH]

    global slist,s,shift
    slist = []
    s = ""
    shift = False
    
    #coords1
    ws1 = width/7          
    xs1 = width/2-width/7-width/14
    ys1 = height/3
    x2s1 = width/2 + width/14
    y2s1 = y + w + height/14
    
    global oneCo,twoCo,threeCo,fourCo
    oneCo = [xs1,ys1,ws1,ws1]
    twoCo = [x2s1,ys1,ws1,ws1]
    threeCo = [xs1,y2s1,ws1,ws1]
    fourCo = [x2s1,y2s1,ws1,ws1]
    
def draw():
    global playerNames, eersteSpeler
    background(mainColor)
    fill(0)
    textAlign(CENTER)
    textFont(standardFont)
    #main menu
    if phase == 0:
        global f, f1, f2, j
        j = []
        global scherm
        background(maincolor)
        
        textFont(f2)
        textAlign(CENTER)
        if scherm == 0:
            screen0.setup()
            screen0.draw()
        elif scherm == 1:
            screen1.draw()
        elif scherm == 2:
            screen2.draw(players)
        elif scherm == 3:
            playerNames = screen2.getPlayerNames()
            screen3.draw(players, playerNames)
            if screen3.getAllTaken() == True:
                scherm = 0
        elif scherm == 100:
            handleiding.setup()
            handleiding.draw()
        image(frame,0,0,width,height)
    
    #game
    elif phase == 1:
        #stat box
        hollowRect(*statBox)
        for i in range(1,players+1):
            text("speler " + str(i) + ":",statBox[0]+statBox[2]/4,statBox[1]+statBox[3]/5+i*25)
            
def mouseInRect(x, y, w, h):
    return(x < mouseX < x + w and y < mouseY < y + h)

def mousePressed():
    global playerNames, empirePlayer
    global posDict,flagDict
    flagDict = {}
    playerNames = []
    
    if phase == 0:
        global scherm
        global players
        if scherm == 0: 
            if mouseInRect(*contCo):
                scherm = 1 
                #naar spel
            if mouseInRect(*guideCo):
                scherm = 100
                #naar handleiding
            if mouseInRect(*backCo):
                exit()
                #verlaat spel
        if scherm == 1:
            if mouseInRect(*backCo):
                scherm = 0
                #naar main menu
            elif mouseInRect(*oneCo):
                players = 1
                scherm = 2
            elif mouseInRect(*twoCo):
                players = 2
                scherm = 2
            elif mouseInRect(*threeCo):
                players = 3
                scherm = 2
            elif mouseInRect(*fourCo):
                players = 4
                scherm = 2    
        if scherm == 2:
            playerNames = screen2.mousePressed(players)
            if mouseInRect(*backCo):
                scherm = 1
                players = 0
            if mouseInRect(*okCo):
                scherm = 3
                #naar aantal spelers
        if scherm == 100:
            global backW,backH,backX,backY
            backX = width/6
            backY = height-height/6
            backW = 150
            backH = 40
            backCoHand = [backX, backY, backW, backH]
            if mouseInRect(*backCoHand):
                scherm = 0
                #naar main menu
        if scherm == 3:
            playerNames = screen2.getPlayerNames()
            screen3.mousePressed(playerNames, players)
            newBackGo = screen3.getCoordinates()
            if mouseInRect(*newBackGo):
                scherm = scherm - 1
                #naar main menu
            
            
def keyPressed():
    if scherm == 2:
        screen2.keyPressed()
