import functions
import random
import time
import screen0,screen1, screen2, screen3, handleiding,functions,game
import os


add_library('minim')
test = Minim(this)
#menu varsz
#menu vars
#game vars
p1 = False
difb = False
quest = False
startb = False
main = True
flash = False
done = False
finish = False
chanceb = False
choice = None
choiceScreen = False
noCard = True
secrout = False
cp = False
acp = False
game = False
menu = True
cha = False
rolling = False


rolled = False
correct = None

q = True
a = False
c = False

cap = False
per = True
fla = False

chosenplayer = None
turn = 0
curEmp = ""
dif = ""
kaart = ""

question = ""
answer = ""



empDict = {"otto":"Ottomaanse Rijk","nl":"Nederlandse Rijk","spa":"Spaanse Rijk","eng":"Engelse Rijk"}



mainColor = color(234,222,191)

def txtToDict(ldstrings):
    r_dict = {}
    for line in ldstrings:
        tokens = line.split("=")
        tokens = [x for x in tokens]
        r_dict[tokens[0]] = tokens[1]
        
    return r_dict




\


mainBoard = functions.board()
#game vars

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
    
class dice:
    value = 1
    def __init__(self,x,y,w):
        self.x = x
        self.y = y
        self.w = w
        self.sides = 6
        
    def roll(self):
        self.value = random.randint(1,self.sides)
        
    def showdobbel(self,n):
        x = self.x
        y = self.y
        w = self.w
        roll = n
        hollowRect(x,y,w,w)
        fill(0)
        if roll == 1 or roll == 0:
            circle(x+w/2,y+w/2,10)
        elif roll == 2:
            circle(x+w - w/6,y+w/6,10)
            circle(x+w/6,y+w-w/6,10)
        elif roll == 3:
            circle(x+w/2,y+w/2,10)
            circle(x+w - w/6,y+w/6,10)
            circle(x+w/6,y+w-w/6,10)
        elif roll == 4:
            circle(x+w - w/6,y+w/6,10)
            circle(x+w/6,y+w-w/6,10)
            circle(x+w/6,y+w/6,10)
            circle(x+ w - w/6,y+w-w/6,10)
        elif roll == 5:
            circle(x+w/2,y+w/2,10)
            circle(x+w - w/6,y+w/6,10)
            circle(x+w/6,y+w-w/6,10)
            circle(x+w/6,y+w/6,10)
            circle(x+ w - w/6,y+w-w/6,10)
        elif roll == 6:
            circle(x+w - w/6,y+w/6,10)
            circle(x+w/6,y+w-w/6,10)
            circle(x+w/6,y+w/6,10)
            circle(x+ w - w/6,y+w-w/6,10)
            circle(x+w/6,y+w/2,10)
            circle(x+w -w/6,y+w/2,10)

def flashProc(rijk,dif):
    global question,answer
    if rijk == "NEUT":
            question,answer = random.choice(list(neutdict.items()))
    else:
        if dif == "easy":
            if rijk == "eng":
                question,answer = random.choice(list(britmadict.items()))
            elif rijk == "nl":
                question,answer = random.choice(list(nlmadict.items()))
            elif rijk == "spa":
                question,answer = random.choice(list(spmadict.items()))
            elif rijk == "otto":
                question,answer = random.choice(list(otmadict.items()))
        elif dif == "hard":
            if rijk == "eng":
                question,answer = random.choice(list(britmodict.items()))
            elif rijk == "nl":
                question,answer = random.choice(list(nlmodict.items()))
            elif rijk == "spa":
                question,answer = random.choice(list(spmodict.items()))
            elif rijk == "otto":
                question,answer = random.choice(list(otmodict.items()))
    time.sleep(0.5)

def doneProc():
    global question,answer,correct,done,main,rolled,q
    rijk = curEmp
    if rijk == "neut":
            del neutdict[question]
    else:
        if dif == "easy":
            if rijk == "en":
                del britmadict[question]
            elif rijk == "nl":
                del nlmadict[question]
            elif rijk == "spa":
                del spmadict[question]
            elif rijk == "ot":
                del otmadict[question]
        elif dif == "hard":
            if rijk == "en":
                del britmodict[question]
            elif rijk == "nl":
                del nlmodict[question]
            elif rijk == "spa":
                del spmodict[question]
            elif rijk == "otto":
                del otmodict[question]
    if correct:
        curplayer.addFlag(curEmp)
        correct = None
    done = False
    main = True
    rolled = False
    q = True
    question,answer = "",""
            
                        
                                    
                                                            
def setup():
    size(1080,720)
    #main menu setup
    global players, playerNames
    playerNames = []
    global mainColor
    mainColor = color(234,222,191)
    
    screen0.setup()

    global standardFont
    standardFont = createFont("Harrington",25)
    
    global phase
    phase = 0
    
    #phase 0
    global f, f1, f2
    global scherm, maincolor
    global schip, frame, handleiding1, handleiding2
    schip = loadImage("schip.png")
    frame = loadImage("frame.png")
    handleiding1 = loadImage("handleiding1.png")
    handleiding2 = loadImage("handleiding2.png")
    maincolor = color(234,222,191)
    f = createFont("Harrington",40)
    f1 = createFont("Harrington",80)
    f2 = createFont("Harrington",30)
    scherm = 0
    
    global backCo
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    global w,x,y,x2,y2,players
    w = 90          
    x = 860
    y = 250
    x2 = x+100
    y2 = y+100
    players = ""
    
    global backCo
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    global contCo
    contX = width/7
    contY = height/4-height/20
    contW = 350
    contH = 100
    contCo = [contX,contY,contW,contH]
    
    global okCo
    okCoX = 750
    okCoY = 600
    okCo = [okCoX, okCoY, backW,backH]
    
    global guideCo
    guideX = width/7
    guideY = contY + contH + height/40
    guideW = 350
    guideH = 100
    guideCo = [guideX,guideY,guideW,guideH]

    global slist,s,shift
    slist = []
    s = ""
    shift = False
    

    
    global twoCo,threeCo,fourCo,fiveCo
    ws1 = width/8          
    xs1 = width/2-width/7-width/14
    ys1 = height/3.5
    x2s1 = width/2 + width/14
    y2s1 = ys1 + ws1 + height/14
    
    twoCo = [xs1,ys1,ws1,ws1]
    threeCo = [x2s1,ys1,ws1,ws1]
    fourCo = [xs1,y2s1,ws1,ws1]
    fiveCo = [x2s1,y2s1,ws1,ws1]
    
    #main menu setup
    #game setup
    global mainDice,curplayer,frame
    mainDice = dice(width-350,height/2-100,200)
    frame = loadImage("frame.png")

    curplayer = checkTurn()
    
    global cardarr
    global ctf,diplo,embargo,gehrout,golf,huur,smeer,smok,verl,winst
    
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
    
    cardarr = [ctf,diplo,embargo,gehrout,golf,huur,smeer,verl,winst]
    
    
    
    
    global start,eind
    eind = 50
    start = eind
    
    global standardfont
    standardfont = createFont("Harrington",12)

    
    global britmadict,britmodict,nlmadict,nlmodict,otmadict,otmodict,spmadict,spmodict,neutdict
    britmadict = txtToDict(loadStrings("vragen_brit_makkelijk.txt"))
    britmodict = txtToDict(loadStrings("vragen_brit_moeilijk.txt"))
    nlmadict = txtToDict(loadStrings("vragen_nl_makkelijk.txt"))
    nlmodict = txtToDict(loadStrings("vragen_nl_moeilijk.txt"))
    otmadict = txtToDict(loadStrings("vragen_otto_makkelijk.txt"))
    otmodict = txtToDict(loadStrings("vragen_otto_moeilijk.txt"))
    spmadict = txtToDict(loadStrings("vragen_sp_makkelijk.txt"))
    spmodict = txtToDict(loadStrings("vragen_sp_moeilijk.txt"))    
    neutdict = txtToDict(loadStrings("vragen_neutraal.txt"))
    #game setup
    
def draw():
    global menu,game
    if menu:
        global f, f1, f2, j
        j = []
        global scherm
        background(maincolor)
        global players

        textFont(f2)
        textAlign(CENTER)
        if scherm == 0:
            screen0.draw()
        elif scherm == 1:
            screen1.draw()
        elif scherm == 2:
            screen2.draw(players)
        elif scherm == 3:
            try:
                playerNames = screen2.getPlayerNames()
                screen3.draw(players, playerNames)
            except IndexError:
                flagDict = screen3.returnFlagDict()
                players = []
                for i in flagDict:
                    players.append(functions.player(i,flagDict[i]))
                                   
                menu = False
                game = True
        
        elif scherm == 100:
            handleiding.setup()
            handleiding.draw()
        image(frame,0,0,width,height)
    #actual game
    elif game:
        global main,curEmp,flash,q,a,rolled,finish,chanceb,noCard
        global curplayer,difb,quest,kaart,cardArr
        global mainDice,start,p1,turn,cp,chosenplayer,acp,secondcolor,rolling
        rolling = False
        secondcolor = color(146,128,60)

        background(mainColor)
        textAlign(CENTER)
        textFont(standardfont)
        image(frame,0,0,width,height)
        curplayer = checkTurn()
        
        print(rolling)
        print(turn)
        print(start,eind)
    
    
        try:
            prevEmp = curEmp
            curEmp = functions.isInEmpire(curplayer.getPos())
        except AttributeError:
            curEmp = None
        global rolCo,rolCoText
        rolCo = [width-350,height/2+150,100,50]
        rolCoText = [width-300,height/2+170]
        
        statBox(width/10,height/6,width/2,height/1.75)
        fill(mainColor)
        rect(*rolCo)
        textAlign(CENTER)
        fill(0)
        text("Rol",*rolCoText)
        if main:
            textAlign(CENTER)
            if not(rolled) or start >= eind:
                text("klik om te rollen",width/2,height/8)
        
                
            if start <= eind:
                mainDice.showdobbel(random.randint(1,6))
                rolling = True
                if start == eind and turn > 0:
                    mainDice.roll()
                    p1 = False
                    rolled = True
        
                start += 1
            else:
                if rolled:
                    rolling = False
                    if mousePressed:
                        curplayer.changePos(mainDice.value)
                        rolled = False


                        try:
                            if curEmp != prevEmp and curEmp != "neut":
                                if curplayer.notol:
                                    curplayer.notol = False
                                else:
                                    curplayer.enterEmp()
                            if mainBoard.checkQuestion(curplayer.getPos()):
                                curEmp = functions.isInEmpire(curplayer.getPos())
                                difb = True
                                main = False
                                    
                            elif mainBoard.checkEvent(curplayer.getPos()) and cha:
                                curEmp = functions.isInEmpire(curplayer.getPos())
                                noCard = True
                                chanceb = True
                                main = False

                        except AttributeError:
                            print("not yet")
                fill(0)
                mainDice.showdobbel(mainDice.value)
        if difb:
            chooseDif(width/2-350,height/4,700,height/2)
        elif flash:
            flashProc(curEmp,dif)
            flash = False
            quest = True
            
        elif quest:    
            drawQCard(width/2-350,height/4,700,height/1.5)    
    
        elif done:
            doneProc()
        if chanceb:
            drawECard(0,0,width,height)
        elif secrout:
            secRout(0,0,width,height)
        elif cp:
            choosePlayer(0,0,width,height)
        elif acp:
            #huur
            if kaart == 5:
                if curplayer.coins > 0:
                    curplayer.changeCoins(-1)
                    chosenplayer.addWait(1)
            if kaart == 6:
                if chosenplayer.coins > 0:
                    chosenplayer.changeCoins(-1)
                    curplayer.changeCoins(1)
            chosenplayer = None
            acp = False
            main = True
            kaart = None
            if turn == 1:
                turn += 1
        '''
        if cap:
            CTF(0,0,width,height)
        '''
        if checkWinner() != False:
            winner = checkWinner()
            finish = True
        if finish:
            winScreen(winner)
        
        print(kaart)
        
def mouseClicked():
    global c,q,a,difb,flash,dif
    if quest:
        if mouseInRect(width/2-350,height/4,700,height/2) and q == True:
            q = False
            a = True
            time.sleep(0.1)
        elif mouseInRect(width/2-350,height/4,700,height/2) and a == True:
            c = True
            a = False
            time.sleep(0.1)
     
    

def chooseDif(x,y,w,h):
    global dif,difb,quest,flash,secondcolor
    textAlign(CENTER)
    hollowRect(x,y,w,h)
    fill(mainColor)
    rect(x,y,w,h)
    image(frame,x,y,w,h)
    fill(0)
    text("Kies moeilijkheid",x+w/2,y+h/4)
    #colors
    secondcolor = color(146,128,60)
    c21 = secondcolor
    c22 = color(109, 95, 44)
    t21 = color(119,105,49)
    t22 = color(81,71,36)
    
    wid2 = w/5    
    x21 = x+w/3-wid2    
    x22 = x+w/3*2
    y21 = y+h/2
    if mouseInSquare(x21,y21,wid2):
        fill(t21)
        if mousePressed:
            dif = "easy"
            difb = False
            flash = True
            time.sleep(0.5)
    else:
        fill(c21)
    square(x21,y21,wid2)
    
    fill(0)
    text("Makkelijk",x21+wid2/2,y21+wid2/2)
    if mouseInSquare(x22,y21,wid2):
        fill(t22)
        if mousePressed:
            dif = "hard"
            difb = False
            flash = True
            time.sleep(0.5)
    else:
        fill(c22)
    square(x22,y21,wid2)
    fill(0)
    text("Moeilijk",x22+wid2/2,y21+wid2/2)
    

    

def drawQCard(x,y,w,h):
    global question,answer,quest,done,correct,q,a,c
    
    hollowRect(x,y,w,h)
    if curEmp == "otto":
        fill(255,150,150)
    elif curEmp == "eng":
        fill(150,255,150)
    elif curEmp == "nl":
        fill(150,150,255)
    elif curEmp == "spa":
        fill(255,150,150)
    textAlign(CENTER)
    rect(x,y,w,h)
    fill(0)
    image(frame,x,y,w,h)
    text(curplayer.name,x+w-w/8,y+w/8)
    if q:
        textSize(30)
        text("Vraag:",x+w/2,y+h/6)
        textSize(30)
        text(question,x+w/8,y+h/3,w-w/4,y+h/2+h/10)
    elif a:
        textSize(30)
        text("Antwoord:",x+w/2,y+h/6)
        textSize(30)
        text(answer,x,y+h/3,w,y+h/2+h/10)
    elif c:
        widcheck = w/5
        text("Goed of Fout?",x+w/2,y+h/7)
        if mouseInSquare(x+w/3-widcheck/2,y+h/2,widcheck):
            fill(0,155,0)
            if mousePressed:
                correct = True
                c = False
                quest = False
                done = True
                time.sleep(0.1)
        else:
            fill(0,255,0)
        square(x+w/3-widcheck/2,y+h/2,widcheck)
        fill(0)
        text("Goed",x+w/3,y+h/2+widcheck/2)
        if mouseInSquare(x+w/3*2-widcheck/2,y+h/2,widcheck):
            fill(155,0,0)
            if mousePressed:
                correct = False
                c = False
                quest = False
                done = True
                time.sleep(0.1)
        else:
            fill(255,0,0)
        square(x+w/3*2-widcheck/2,y+h/2,widcheck)
        fill(0)
        text("Fout",x+w/3*2,y+h/2+widcheck/2)
        

def drawECard(x,y,w,h):
    
    global ctf,diplo,embargo,gehrout,golf,huur,smeer,verl,winst
    global players,curplayer,cardarr,choice,choiceScreen,kaart,noCard
    global chanceb,main,secrout,cp,cap,cha
    fill(mainColor)
    rect(x,y,w,h)
    fill(0)
    if noCard:
        kaart = random.randint(0,len(cardarr)-1)
        choice = None
        choiceScreen = False
        noCard = False
    
    hollowRect(x,y,w,h)
    textAlign(CENTER)
    image(frame,x,y,w,h)
    textSize(30)
    text("Kanskaart",x+w/2,y+h/8)
    image(cardarr[kaart],x+w/3,y+h/4,w/3,h/2)
    # cardarr = [ctf,diplo,embargo,gehrout,golf,huur,smeer,smok,verl,winst]
    #ctf
    if kaart == 0:
        kaart = 8
    if mousePressed:
        #ctf *
        if kaart == 0:
            if mousePressed:
                chanceb = False
                cap = True
        #diplo 
        elif kaart == 1:
            curplayer.diplom()
            if mousePressed: 
                curplayer.addWait(1)
                chanceb = False
                main = True
                cha = True
        #embargo
        elif kaart == 2:
            if mousePressed:    
                curplayer.addWait(1)
                chanceb = False
                main = True
                cha = True
        #gehrout
        elif kaart == 3:
            #keuze tussen brug gebruiken voor 2 goudstukken of niet
            if mousePressed:
                secrout = True
                chanceb = False
        #golf    
        elif kaart == 4:
            if mousePressed:
                curplayer.changePos(6)
                chanceb = False
                main = True
                cha = True
            
        #huur 
        elif kaart == 5:
            if mousePressed:

                chanceb = False
                cp = True
                time.sleep(1)

                
        #smok
        elif kaart == 6:
            if mousePressed:
                chanceb = False
                cp = True
        #verl
        elif kaart == 7:
            if mousePressed:
                curplayer.changeCoins(-1)

                chanceb = False
                main = True
                cha = True
        #winst
        elif kaart == 8:
            if mousePressed:
                curplayer.changeCoins(1)
                chanceb = False
                main = True
                cha = True
'''               
def CTF(x,y,w,h):
    global cap,main,curplayer,players,per,fla
    lis = list(filter(lambda i : i != curplayer,players))
    
    chosen = None
    other = functions.checkFlags(curplayer,lis)

    fill(mainColor)
    rect(x,y,w,h)
    image(frame,x,y,w,h)
    fill(0)
    textAlign(CENTER)
    
    if len(other.keys()) == 0:
        textSize(40)
        text("Geen vlaggen om te stelen",x+w/2,y+h/2)
        textSize(20)
        text("Klik om door te gaan",x+w/2,y+h/1,5)
        if mousePressed:
            main = True
            cap = False
    if fla:
        fill(mainColor)
        text(chosen.name + "'s flags")
        if k["otto"]:
            if mouseInSquare(35,y+w/2,200):
                fill(155,0,0)
                if mousePressed:
                    chosen.delFlag("otto")
                    curplayer.addFlag("otto")
                    main = True
                    cap = False
                    per = True
                    Fla = False
            else:
                fill(255,0,0)
            square(35,y+w/2,200)
        if k["spa"]:
            if mouseInSquare(270,y+w/2,200):
                fill(155,155,0)
                if mousePressed:
                    chosen.delFlag("spa")
                    curplayer.addFlag("spa")
                    main = True
                    cap = False
                    per = True
                    Fla = False
            else:
                fill(255,255,0)
            square(270,y+w/2,200)
        if k["eng"]:
            if mouseInSquare(575,y+w/2,200):
                fill(155,155,0)
                if mousePressed:
                    chosen.delFlag("eng")
                    curplayer.addFlag("eng")
                    main = True
                    cap = False
                    per = True
                    Fla = False
            else:
                fill(255,255,0)
            square(575,y+w/2,200)
        if k["nl"]:
            if mouseInSquare(845,y+w/2,200):
                fill(155,155,0)
                if mousePressed:
                    chosen.delFlag("nl")
                    curplayer.addFlag("nl")
                    main = True
                    cap = False
                    per = True
                    Fla = False
            else:
                fill(255,255,0)
            square(845,y+w/2,200)
    if per:
        if len(other.keys()) == 1:
            if mouseInSquare(440,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[0]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(440,y+h/2,200)
            text(other.keys()[0].name,540,y+h/2+100)
        elif len(other.keys()) == 2:
            if mouseInSquare(170,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[0]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(170,y+h/2,200)
            fill(0)
            text(other.keys()[0].name,270,y+h/2+100)
            if mouseInSquare(710,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[1]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(710,y+h/2,200)
            fill(0)
            text(other.keys()[1].name,810,y+h/2+100)
        else:
            if mouseInSquare(80,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[0]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(80,y+h/2,200)
            fill(0)
            text(other.keys()[0].name,180,y+h/2+100)
            if mouseInSquare(440,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[1]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(440,y+h/2,200)
            fill(0)
            text(other.keys()[1].name,540,y+h/2+100)
            if mouseInSquare(800,y+h/2,200):
                fill(secondcolor)
                if mousePressed:
                    chosen = other.keys()[2]
                    per = False
                    fla = True
            else:
                fill(mainColor)
            square(800,y+h/2,200)
            fill(0)
            text(other.keys()[2].name,900,y+h/2+100)

    
    '''            
            
                

            
        
    
        
        

def choosePlayer(x,y,w,h):
    global chosenplayer,curplayer,players,cp,acp
    lis = list(filter(lambda i : i != curplayer,players))
    textAlign(CENTER)
    image(frame,x,y,w,h)
    fill(mainColor)
    rect(x,y,w,h)
    fill(0)
    text("Kies speler:",w/2,h/8)
    for i in range(len(lis)):
        if mouseInRect(x+w/2-w/8,y+h/5*(i+1),w/4,h/8):
            if mousePressed:
                chosenplayer = players[i]
                cp = False
                acp = True
        fill(255)
        rect(x+w/2-w/8,y+h/5*(i+1),w/4,h/8)
        fill(0)
        text(lis[i].name,x+w/2,y+h/5*(i+1)+h/16)
                    
            
def secRout(x,y,w,h):
    global choice,secrout,turn,main,players,curplayer,curEmp
    if choice == None:
        fill(mainColor)
        rect(x,y,w,h)
        textAlign(CENTER)
        textSize(20)
        
        if mouseInSquare(x+w/8,y+h/2,w/4):
            fill(0,150,0)
            if mousePressed:
                choice = True
        else:
            fill(0,255,0)
        square(x+w/8,y+h/2,w/4)
        fill(0)
        text("Ja",x+w/4,y+h/2+w/8)
        
        if mouseInSquare(x+w-w/4-w/8,y+h/2,w/4):
            fill(150,0,0)
            if mousePressed:
                choice = False
        else:
            fill(255,0,0)
        square(x+w-w/4-w/8,y+h/2,w/4)
        fill(0)
        text("Nee",x+w-w/4,y+h/2+w/8)
    else:
        if choice == False:
            print("g")
        elif choice == True:
            choiceScreen = False
            if curEmp == "otto":
                while curplayer.getPos() != 46:
                    curplayer.changePos(1)
                
            elif curEmp == "nl":
                while curplayer.getPos() != 26:
                    curplayer.changePos(1)
            elif curEmp == "eng":
                while curplayer.getPos() != 6:
                    curplayer.changePos(1)
            elif curEmp == "spa":
                while curplayer.getPos() != 66:
                    curplayer.changePos(1)
        curplayer.changeCoins(-2)

        
        if mousePressed:    
            secrout = False
            chanceb = False
            main = True
            choice = None
            if turn == 1:
                turn += 1
    
def rollProcess1():
    global start,turn
    start = 0
    turn += 1
    
def changeTurn():
    global players,curplayer
    
    try:
        players[(players.index(curplayer)+1)%len(players)].startTurn()
        curplayer.endTurn()
    
    except ValueError:
        try:
            players[0].startTurn()
            curplayer.endTurn()
        except AttributeError:
            pass
    
    
def statBox(x,y,w,h):
    hollowRect(x,y,w,h)
    fill(0)
    textAlign(RIGHT)
    fill(mainColor)
    rect(x,y,w,h)
    fill(0)
    image(frame,x,y,w,h)
    textSize(25)
    lis = sorted(players,key=lambda x:x.startpos,reverse=False)
    for i in range(len(lis)):
        textAlign(RIGHT)
        text(lis[i].name + ":",x+w/4,y+(70*(i+1)))
        textAlign(LEFT)
        text("positie: " + str(lis[i].curpos) + ", vlaggen: " + str(lis[i].count),x+w/4+w/10,y+(70*(i+1)))
        text(empDict[lis[i].empire] + ", munten: " + str(lis[i].getCoins()),x+w/4+w/10,y+(70*(i+1.45)))
        
    textAlign(LEFT)
    try:
        text("Aan de beurt: "+curplayer.name,x+w/4,y+(70*(len(players)+1)))
    except AttributeError:
        text("Aan de beurt: ",x+w/4,y+(70*5))
        
def startFunc():
    global startb,players
    startb = True
    players[0].startTurn()

def hasName(s,player):
    if player.name == s:
        return True
    else:
        return False
def mousePressed():
    global p1
    if menu:
        global playerNames, empirePlayer
        global posDict,flagDict
        flagDict = {}
        playerNames = []
        
        global scherm
        global players
        if scherm == 0: 
            if mouseInRect(*contCo):
                scherm = 1 
                #naar spel
            if mouseInRect(*guideCo):
                scherm = 100
                #naar handleiding
            if mouseInRect(*backCo):
                exit()
                #verlaat spel
        if scherm == 1:
            if mouseInRect(*backCo):
                scherm = 0
                #naar main menu
            elif mouseInRect(*twoCo):
                players = 2
                scherm = 2
            elif mouseInRect(*threeCo):
                players = 3
                scherm = 2
            elif mouseInRect(*fourCo):
                players = 4
                scherm = 2
            elif mouseInRect(*fiveCo):
                players = 5
                scherm = 2    
        if scherm == 2:
            playerNames = screen2.mousePressed(players)
            if mouseInRect(*backCo):
                scherm = 1
                players = 0
                playerNames = []
            if mouseInRect(*okCo):
                scherm = 3
                #naar aantal spelers
        if scherm == 100:
            global backW,backH,backX,backY
            backX = width/6
            backY = height-height/6
            backW = 150
            backH = 40
            backCoHand = [backX, backY, backW, backH]
            if mouseInRect(*backCoHand):
                scherm = 0
                #naar main menu
        if scherm == 3:
            playerNames = screen2.getPlayerNames()
            screen3.mousePressed(playerNames, players)
            newBackGo = screen3.getCoordinates()
            if mouseInRect(*newBackGo):
                scherm = scherm - 1
                
                #naar main menu
    else:
        if not startb:
            startFunc()
        elif main:
            if not(rolling) and p1 and start >= eind and mouseInRect(*rolCo):
                rollProcess1()
            else:
                if not(rolling) and mouseInRect(*rolCo):
                    changeTurn()
                    while curplayer.getWait() > 0:
                        changeTurn()
                    p1 = True

def checkTurn():
    global curplayer
    for i in players:
        if i.hasturn:
            return i
    return None

def winScreen(winner):
    textSize(50)
    text("Winner is:\n "+winner.name,width/2,height/2)
    if mousePressed:
        exit()
def checkWinner():
    for i in players:
        if i.count == 4:
            return i
    return False

def keyPressed():
    if scherm == 2:
        screen2.keyPressed()
        
def mouseInRect(x,y,w,h):
    return (x < mouseX < x+w) and (y< mouseY < y+h)
def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
