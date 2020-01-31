
def setup():
    global schip
    global f, f1, f2
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",60)
    f2 = createFont("Harrington",30)
    schip = loadImage("schip.png")

    global backCo
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    global contCo
    contX = width/7
    contY = height/4-height/20
    contW = 350
    contH = 100
    contCo = [contX,contY,contW,contH]
    
    global guideCo
    guideX = width/7
    guideY = contY + contH + height/40
    guideW = 350
    guideH = 100
    guideCo = [guideX,guideY,guideW,guideH]
    
    
    global mainColor,secondColor
    mainColor = color(234,222,191)
    secondColor = color(134,122,91)
    
def draw():
    image(schip,0,0,width,height)
    fill(0)
    textFont(f1)
    textAlign(LEFT)
    text("Vlaggenjacht",width/6,height/9)
    textAlign(CENTER)
    textFont(f)
    fill(secondColor,63)
    fill(134,122,91,63)

    rect(*contCo)
    rect(*guideCo)
    rect(*backCo)
    fill(0)
    textSize(55)
    text("Start Spel",contCo[0]+contCo[2]/2,contCo[1]+contCo[3]*0.75) 
    text("Handleiding",guideCo[0]+guideCo[2]/2,guideCo[1]+guideCo[3]*0.75)
    text("Verlaat Spel",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)

    
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
