import rijkb,difb,questionb,answerb,check
import random

add_library('minim')
test = Minim(this)

def flashProc():
    global question,answer
    if rijk == "NEUT":
            question,answer = random.choice(list(neutdict.items()))
    else:
        if dif == "easy":
            if rijk == "EN":
                question,answer = random.choice(list(britmadict.items()))
            elif rijk == "NL":
                question,answer = random.choice(list(nlmadict.items()))
            elif rijk == "SP":
                question,answer = random.choice(list(spmadict.items()))
            elif rijk == "OT":
                question,answer = random.choice(list(otmadict.items()))
        elif dif == "hard":
            if rijk == "EN":
                question,answer = random.choice(list(britmodict.items()))
            elif rijk == "NL":
                question,answer = random.choice(list(nlmodict.items()))
            elif rijk == "SP":
                question,answer = random.choice(list(spmodict.items()))
            elif rijk == "OT":
                question,answer = random.choice(list(otmodict.items()))
def doneProc():
    global question,answer
    if rijk == "NEUT":
            del neutdict[question]
    else:
        if dif == "easy":
            if rijk == "EN":
                del britmadict[question]
            elif rijk == "NL":
                del nlmadict[question]
            elif rijk == "SP":
                del spmadict[question]
            elif rijk == "OT":
                del otmadict[question]
        elif dif == "hard":
            if rijk == "EN":
                del britmodict[question]
            elif rijk == "NL":
                del nlmodict[question]
            elif rijk == "SP":
                del spmodict[question]
            elif rijk == "OT":
                del otmodict[question]
        question = ""
        answer = ""
def txtToDict(ldstrings):
    r_dict = {}
    for line in ldstrings:

        tokens = line.split("=")
        tokens = [x.encode(encoding="utf-8", errors="strict") for x in tokens]
        r_dict[tokens[0]] = tokens[1]
        
    return r_dict

def setup():
    global scherm,sound,frame,pistol,pistol2
    global britmadict,britmodict,nlmadict,nlmodict,otmadict,otmodict,spmadict,spmodict,neutdict
    global wid,x1,x2,x3,x4,y,wid
    scherm = 1
    fullScreen()
    
    britmadict = txtToDict(loadStrings("vragen_brit_makkelijk.txt"))
    britmodict = txtToDict(loadStrings("vragen_brit_moeilijk.txt"))
    nlmadict = txtToDict(loadStrings("vragen_nl_makkelijk.txt"))
    nlmodict = txtToDict(loadStrings("vragen_nl_moeilijk.txt"))
    otmadict = txtToDict(loadStrings("vragen_otto_makkelijk.txt"))
    otmodict = txtToDict(loadStrings("vragen_otto_moeilijk.txt"))
    spmadict = txtToDict(loadStrings("vragen_sp_makkelijk.txt"))
    spmodict = txtToDict(loadStrings("vragen_sp_moeilijk.txt"))    
    neutdict = txtToDict(loadStrings("vragen_neutraal.txt"))
    
    #sounds
    sound = 'buttonsound6.mp3'
    sound = test.loadFile(sound,2048)
    
    #images
    frame = loadImage("frame.png")
    pistol = loadImage("pistol.png")
    pistoltwo = loadImage("pistoltwo.png")
    
    
    
    
def draw():
    global wid,x1,x2,x3,x4,y,wid,x21,x22,y21,y22,wid2,widcheck
    widcheck = width/10
    wid = width/6
    x1 = width/24
    x2 = x1 + (wid+wid/2)
    x3 = x2 + (wid+wid/2)
    x4 = x3 + (wid+wid/2) 
    x5 =  width/2-wid/2  
    y = height/4
    
    wid2 = width/5    
    x21 = width/3-wid2    
    x22 = width/3*2
    y21 = height/2
    #fonts
    standardfont = createFont("Harrington",25)
    
    #colors
    maincolor = color(234,222,191)
    secondcolor = color(146,128,60)
    c1 = color(0,0,255)
    c2 = color(0,255,0)
    c3 = color(255,255,0)
    c4 = color(255,0,0)
    c5 = secondcolor
    t1 = color(0,0,170)
    t2 = color(0,170,0)
    t3 = color(170,170,0)
    t4 = color(170,0,0)
    t5 = color(91, 79, 37)
    
    c21 = secondcolor
    c22 = color(109, 95, 44)
    t21 = color(119,105,49)
    t22 = color(81,71,36)
    filt = color(100)
    background(maincolor)
    textAlign(CENTER)
    textFont(standardfont)
    textSize(50)
    fill(0)
    image(frame,0-width/40,0-height/90,width+width/20,height+height/30)
    
    if scherm == 1:
        rijkb.draw()
    elif scherm == 2:
        difb.draw()
    elif scherm == 3:
        questionb.draw(question)
    elif scherm == 4:
        answerb.draw(answer)
    elif scherm == 5:
        check.draw()

#functie die een bool terugstuurd die aangeeft of de muis binnen een bepaald vierkant zit
def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)

def mouseClicked():
    global rijk,dif,scherm
    if scherm == 1:
        if mouseInSquare(x1,y,wid):
            sound.loop(0)
            print("NL")
            rijk = "NL"
            scherm = 2
        elif mouseInSquare(x2,y,wid):
            sound.loop(0)
            print("EN")
            rijk = "EN"
            scherm = 2
        elif mouseInSquare(x3,y,wid):
            sound.loop(0)
            print("SP")
            rijk = "SP"
            scherm = 2
        elif mouseInSquare(x4,y,wid):
            sound.loop(0)
            print("OT")
            rijk = "OT"
            scherm = 2
        elif mouseInSquare(width/2-wid/2,y*2,wid):
            sound.loop(0)
            print("NEUT")
            rijk = "NEUT"
            scherm = 2
    elif scherm == 2:
        if mouseInSquare(x21,y21,wid):
            sound.loop(0)
            scherm = 3
            dif = "easy"
            flashProc()
        elif mouseInSquare(x22,y21,wid):
            sound.loop(0)
            scherm = 3
            dif  = "hard"
            flashProc()
    elif scherm == 3:
        scherm = 4
    elif scherm == 4:
        doneProc()
        scherm = 5
    elif scherm == 5:
        if mouseInSquare(width/3-wid/2,height/2,widcheck):
            scherm = 1
        if mouseInSquare(width/3*2-wid/2,height/2,widcheck):
            scherm = 1
        
