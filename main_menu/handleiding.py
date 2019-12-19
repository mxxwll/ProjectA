def setup():
    global handleiding1
    handleiding1 = loadImage("handleiding1.png")
    
    global backW,backH,backX,backY
    backX = width/6
    backY = height-height/6
    backW = 150
    backH = 40
def draw():
    
    background(234,222,191)
    image(handleiding1,0,0,width,height)
    
    hollowRect(backX,backY,backW,backH)
    text("Terug",backX+backW/2,backY+backH/1.5)
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
