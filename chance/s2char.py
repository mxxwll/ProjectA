
def setup():
    fullScreen()
    global cardarr
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
def draw(card):
    wid = width/5
    hei = height/2
    image(cardarr[card],width/2-wid,height/6,wid,hei)
    
