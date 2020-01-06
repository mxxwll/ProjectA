w = 90          
x = 860
y = 250
x2 = x+100
y2 = y+100
players = ""
import screen1,screen2

def setup():
    global f,screen,maincolor,frame,w
    fullScreen()
    f = createFont("Harrington",32)
    maincolor = color(234,222,191)
    screen = 1
    frame = loadImage("frame.png")
            

def draw():
    global f,w
    background(maincolor)
    textFont(f)
    image(frame,0,0,width,height)
    if screen == 1:
        screen1.draw()
    if screen == 2:
        screen2.draw(players)

def mousePressed():
    global players,screen,w
    if screen == 1:
        if x < mouseX < x+w and mouseY > y and mouseY < y+w:
            players = 1
            screen = 2
        elif mouseX > x2 and mouseX < x2+w and mouseY > y and mouseY < y+w:
            players = 2
            screen = 2
        elif mouseX > x and mouseX < x+w and mouseY > y2 and mouseY < y2+w:
            players = 3
            screen = 2
        elif mouseX > x2 and mouseX < x2+w and mouseY > y2 and mouseY < y2+w:
            players = 4
            screen = 2
    
        print(players)
        
def keyPressed():
    screen2.keyPressed()
        
        
        
