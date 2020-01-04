import screen0,screen1, screen2, handleiding,functions
import os


def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)

intro = True
game = False
def setup():
    fullScreen()
    global players
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
    
    global backW,backH,backX,backY
    backX = width/6
    backY = height-height/6
    backW = 150
    backH = 40
    
    global w,x,y,x2,y2,players
    w = 90          
    x = 860
    y = 250
    x2 = x+100
    y2 = y+100
    players = ""

    
def draw():
    background(mainColor)
    fill(0)
    textAlign(CENTER)
    textFont(standardFont)
    #main menu
    if phase == 0:
        global f, f1, f2
        global scherm
        background(maincolor)
        
        textFont(f2)
        textAlign(CENTER)
        if scherm == 0:
            screen0.setup()
            screen0.draw()
        elif scherm == 1:
            screen1.draw()
    
            textFont(f2)
            textAlign(CENTER)
            text("Terug",width/6,1000)
        elif scherm == 2:
            screen2.draw(players)
    
            textFont(f2)
            textAlign(CENTER)
            text("Terug",width/6,1000)
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
            
def isMouseInSpace(x, y, w, h):
    return(x < mouseX < x + w and y < mouseY < y + h)
def mousePressed():
    if phase == 0:
        global scherm
        global players
        if scherm == 0: 
            if isMouseInSpace(width/5 - 100,280,200,20):
                scherm = 1 
                #naar spel
            if isMouseInSpace(width/5 - 100,380,200,20):
                scherm = 100
                #naar handleiding
            if isMouseInSpace(width/5 - 100,480,200,20):
                exit()
                #verlaat spel
        if scherm == 1:
            if isMouseInSpace(width/6 - 100,80,200,20):
                scherm = 0
                #naar main menu
            if x < mouseX < x+w and mouseY > y and mouseY < y+w:
                players = 1
                scherm = 2
            elif mouseX > x2 and mouseX < x2+w and mouseY > y and mouseY < y+w:
                players = 2
                scherm = 2
            elif mouseX > x and mouseX < x+w and mouseY > y2 and mouseY < y2+w:
                players = 3
                scherm = 2
            elif mouseX > x2 and mouseX < x2+w and mouseY > y2 and mouseY < y2+w:
                players = 4
                scherm = 2
        if scherm == 2:
            if isMouseInSpace(width/6 - 100,80,200,20):
                scherm = 1
                #naar aantal spelers
        if scherm == 100:
            if isMouseInSpace(backX,backY,backW,backH):
                scherm = 0
                #naar main menu
def keyPressed():
    screen2.keyPressed()
