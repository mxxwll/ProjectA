w = 90          
x = 860
y = 250
x2 = x+100
y2 = y+100
players = ""


import screen1, screen2, handleiding


def setup():
    global f, f1
    global scherm, maincolor
    global schip, frame
    fullScreen()
    schip = loadImage("schip.png")
    frame = loadImage("frame.png")
    maincolor = color(234,222,191)
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",80)
    scherm = 0
    
    
def draw():
    global f, f1
    global scherm
    background(maincolor)
    if scherm == 0:
        image(schip,0,0,width,height)
        image(frame,0,0,width,height)
        textFont(f1)
        fill(0)
        textAlign(CENTER)
        text("Vlaggenjacht",width/4,150)
        textFont(f)
        textAlign(CENTER)
        hollowRect(width/7,260,230,50)
        text("Start spel",width/5,300) 
        textAlign(CENTER)
        hollowRect(width/7,360,230,50)
        text("Handleiding",width/5,400)
        textAlign(CENTER)
        hollowRect(width/7,460,230,50)
        text("Verlaat",width/5,500)
    if scherm == 1:
        screen1.draw()
        image(frame,0,0,width,height)
        textAlign(CENTER)
        text("Terug",width/6,100)
    if scherm == 2:
        screen2.draw(players)
        image(frame,0,0,width,height)
        textAlign(CENTER)
        text("Terug",width/6,100)
    if scherm == 100:
        handleiding.draw()
        image(frame,0,0,width,height)
        textAlign(CENTER)
        text("Terug",width/6,100)
        
        
def isMouseInSpace(x, y, w, h):
    return(x < mouseX < x + w and y < mouseY < y + h)
    
    
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)


def mousePressed():
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
        if isMouseInSpace(width/6 - 100,80,200,20):
            scherm = 0
            #naar main menu
            

def keyPressed():
    screen2.keyPressed()
