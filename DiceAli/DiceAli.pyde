import random
add_library('minim')
test = Minim(this)

def setup():
    global roll, w, x, y,a,s,c,h,g, maincolor, frame , sound ,roll1 , roll2, roll3, roll4, roll5, roll6, start , period, eind
    fullScreen()
    noCursor()
    frame = loadImage("frame.png")
    sound = 'dice.mp3'
    sound = test.loadFile(sound,2048)
    roll1 = loadImage('een')
    roll2 = loadImage('twee')
    roll3 = loadImage('drie')
    roll4 = loadImage('vier')
    roll5 = loadImage('vijf')
    roll6 = loadImage('zes')
    roll = random.randint(1,6)
    
    w = 100
    g = 120
    x = width/2-w/2
    y = height/2-w/2
    a = width/2-w/2
    s = height/2+height/6
    c = color(255)
    h = 100
    maincolor = color(234,222,191)
    eind = 50
    start  = eind
     
    

    
    
def mouseWithinSpace(x,y,g,h):
    check = (x < mouseX < x+w) and (y < mouseY < y+h)
    return check



def draw():
    global roll,c,h, randomimage, start, period, eind
    background(maincolor)
    textAlign(CENTER)
    textSize(15)
    image(frame,0-width/40,0-height/90,width+width/20,height+height/30)
    text(str(roll),width/2,height/2)
    fill(255)
    square(x,y,100)
    fill(c)
    rect(a,s,g,h)
    fill(0)
    textAlign(CENTER)
    text('Druk hier om te dobbelen',a+g/10,s+h/3,h,g)
    textAlign(CENTER)
    
    if mouseWithinSpace(a,s,g,w):
        c = color(188)
    else:
        c = color(255)
    
    if start < eind:
        roll = random.randint(1,6)
        start += 1
    showdobbel()
    

def showdobbel():
    global roll 
    
    
    
        
        
     
    if roll == 1:
        circle(x+w/2,y+w/2,10)
    if roll == 2:
        circle(x+w - w/6,y+w/6,10)
        circle(x+w/6,y+w-w/6,10)
    if roll == 3:
        circle(x+w/2,y+w/2,10)
        circle(x+w - w/6,y+w/6,10)
        circle(x+w/6,y+w-w/6,10)
    if roll == 4:
        circle(x+w - w/6,y+w/6,10)
        circle(x+w/6,y+w-w/6,10)
        circle(x+w/6,y+w/6,10)
        circle(x+ w - w/6,y+w-w/6,10)
    if roll == 5:
        circle(x+w/2,y+w/2,10)
        circle(x+w - w/6,y+w/6,10)
        circle(x+w/6,y+w-w/6,10)
        circle(x+w/6,y+w/6,10)
        circle(x+ w - w/6,y+w-w/6,10)
    if roll == 6:
        circle(x+w - w/6,y+w/6,10)
        circle(x+w/6,y+w-w/6,10)
        circle(x+w/6,y+w/6,10)
        circle(x+ w - w/6,y+w-w/6,10)
        circle(x+w/6,y+w/2,10)
        circle(x+w -w/6,y+w/2,10)
    
def mousePressed():
    global randomimage,ending, start
    if mouseWithinSpace(a,s,g,g):
        sound.loop(0)
        start = 0
       
    
    if (mousePressed):
        cursor()
    
