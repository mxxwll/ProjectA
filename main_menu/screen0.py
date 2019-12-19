def setup():
    global schip
    global f, f1, f2
    schip = loadImage("schip.png")
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",80)
    f2 = createFont("Harrington",30)
    
    global backW,backH,backX,backY
    backX = width/6
    backY = height-height/6
    backW = 150
    backH = 40
    
def draw():
    image(schip,0,0,width,height)
    fill(0)
    textFont(f1)
    text("Vlaggenjacht",width/4,150)
    textFont(f)
    hollowRect(width/7,260,230,50)
    text("Start Spel",width/5,300) 
    hollowRect(width/7,360,230,50)
    text("Handleiding",width/5,400)
    hollowRect(backX,backY,backW,backH)
    text("Verlaat Spel",width/5,500)

    
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
