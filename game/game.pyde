import functions


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
    players = 4
    global mainColor
    mainColor = color(234,222,191)
    global statBox
    statBox = [width-width/6, 1, width/6-2, height/3+height/7]
    
    global standardFont
    standardFont = createFont("Harrington",25)
    
    global game,menu
    game = False
    menu = True

    
def draw():
    background(mainColor)
    fill(0)
    textAlign(CENTER)
    textFont(standardFont)

    #stat box
    hollowRect(*statBox)
    for i in range(1,players+1):
        text("speler " + str(i) + ":",statBox[0]+statBox[2]/4,statBox[1]+statBox[3]/5+i*25)
    
