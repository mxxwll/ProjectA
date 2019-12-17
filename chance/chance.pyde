import s1char,s2char,s3char
def calcproc():
    
def setup():
    global maincolor,secondcolor
    global frame
    global button1args
    global mainFont
    fullScreen()
    frame = loadImage("frame.png")
    
    #colors
    maincolor = color(234,222,191)
    secondcolor = color(146,128,60)
    
    #fonts
    mainFont = createFont("harrington",100)
    
    #cards
    ctf = loadImage("Capture the flag.png")
    diplo = loadImage("diplomaat.png")
    embargo = loadImage("embargo.png")
    gehrout = loadImage("Geheime route.png")
    golf = loadImage("golfstroom.png")
    huur = loadImage("huurling.png")
    smeer = loadImage("smeergeld.png")
    smok = loadImage("smokkelaar.jpg")
    verl = loadImage("verlies.png")
    winst = loadImage("winst.png")
    
    cardarr = [ctf,diplo,embargo,gehrout,golf,huur,smeer,smok,verl,winst]
    

    wid = width/8
    button1args = [width/2-wid,height/2,wid,wid]

def draw():
    background(maincolor)
    fill(0)
    textFont(mainFont)
    textAlign(CENTER)
    text("Kanskaart",width/2,height/6)
    image(frame,0,0,width,height)
    if screen == 1:
        s1char.draw()
    elif screen ==2:
        s2char.draw()
    elif screen == 3:
        s3char.draw()
    
def inRect(x,y,w,h):
    return (x < mouseX < x+w) and (y<mouseY<y+h)

def mousePressed():
    screen == 1:
        if inRect(*button1args):
            calcproc()
            screen == 2
        
