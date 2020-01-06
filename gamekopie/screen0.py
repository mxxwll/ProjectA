def setup():
    global schip
    global f, f1, f2
    schip = loadImage("schip.png")
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",80)
    f2 = createFont("Harrington",30)
    
    global backCo
    backX = width/6
    backY = height-height/6
    backW = 150
    backH = 40
    backCo = [backX,backY,backW,backH]
    
    global guideCo
    guideX = width/7
    guideY = height/4
    guideW = 230
    guideH = 50
    guideCo = [guideX,guideY,guideW,guideH]
    
    global contCo
    contX = width/7
    contY = height/4-height/20
    contW = 230
    contH = 50
    contCo = [contX,contY,contW,contH]
    global mainColor,secondColor
    mainColor = color(234,222,191)
    secondColor = color(134,122,91)
    
def draw():
    image(schip,0,0,width,height)
    fill(0)
    textFont(f1)
    text("Vlaggenjacht",width/4,150)
    textFont(f)
    fill(secondColor,63)
    rect(*contCo)
    rect(*guideCo)
    rect(*backCo)
    fill(0)
    text("Start Spel",contCo[0]+contCo[2]/2,contCo[1]+contCo[3]*0.75) 
    text("Handleiding",guideCo[0]+guideCo[2]/2,guideCo[1]+guideCo[3]*0.75)
    text("Verlaat Spel",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)

    
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
