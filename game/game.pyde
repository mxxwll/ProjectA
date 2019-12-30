import functions
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)

def setup():
    fullScreen()
    global players
    players = 4
    global mainColor
    mainColor = color(234,222,191)
    global statBox
    statBox = [width-width/6, 1, width/6-2, height/3+height/7]
    
def draw():
    background(mainColor)
    fill(0)
    textAlign(CENTER)
    #stat box
    hollowRect(*statBox)
    for i in range(1,players+1):
        text("player " + str(i) + ":",statBox[0]+statBox[2]/4,statBox[1]+statBox[3]/5+i*20)    
    
