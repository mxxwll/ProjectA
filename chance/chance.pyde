#chance program omegaluo
import s1char,s2char,s3char
import random
def calcproc():
    return random.randint(0,len(cardarr)-1)
    
def setup():
    global maincolor,secondcolor
    global frame,cardarr
    global button1args,screen
    global mainFont
    fullScreen()
    frame = loadImage("frame.png")
    
    #colors
    maincolor = color(234,222,191)
    secondcolor = color(146,128,60)
    
    screen = 1
    
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
        s2char.draw(card)
    elif screen == 3:
        s3char.draw()
    
def inRect(x,y,w,h):
    return (x < mouseX < x+w) and (y<mouseY<y+h)

def mousePressed():
    global card,screen
    if screen == 1:
        card = calcproc()
        s2char.setup()
        screen = 2
    elif screen == 2:
        screen = 1
    
        
