import functions
import random
import time

add_library('minim')
test = Minim(this)
p1 = False
difb = False
quest = False
startb = False
main = True
flash = False
done = False
finish = False


rolled = False
correct = None

q = True
a = False
c = False

turn = 0
curEmp = ""
dif = ""


question = ""
answer = ""

playernames = ["Liam","Jaikishan","Ali","Tugkan"]
p1 = functions.player(playernames[0],"otto")
p2 = functions.player(playernames[1],"nl")
p3 = functions.player(playernames[2],"spa")
p4 = functions.player(playernames[3],"eng")

empDict = {"otto":"Ottomaanse Rijk","nl":"Nederlandse Rijk","spa":"Spaanse Rijk","eng":"Engelse Rijk"}

mainColor = color(234,222,191)

def txtToDict(ldstrings):
    r_dict = {}
    for line in ldstrings:
        tokens = line.split("=")
        tokens = [x for x in tokens]
        r_dict[tokens[0]] = tokens[1]
        
    return r_dict




players = [p1,p2,p3,p4]

roll1 = loadImage('een')
roll2 = loadImage('twee')
roll3 = loadImage('drie')
roll4 = loadImage('vier')
roll5 = loadImage('vijf')
roll6 = loadImage('zes')

mainBoard = functions.board()

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
            
def setup():
    size(1080,720)
    
    global mainDice,curplayer,frame
    mainDice = dice(width-350,height/2-100,200)
    frame = loadImage("frame.png")

    curplayer = checkTurn()
    
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
    
def draw():
    global main,curEmp,flash,q,a,rolled,finish
    global curplayer,difb,quest
    global mainDice,start,p1
    
    background(mainColor)
    textAlign(CENTER)
    textFont(standardfont)
    image(frame,0,0,width,height)
    curplayer = checkTurn()
    print(question,answer)
    print(turn,q)

    try:
        curEmp = functions.isInEmpire(curplayer.getPos())
    except AttributeError:
        curEmp = None
    statBox(width/10,height/6,width/2,height/1.75)
    if main:
        if start <= eind:
            mainDice.showdobbel(random.randint(1,6))
            if start == eind and turn > 0:
                mainDice.roll()
                curplayer.changePos(mainDice.value)
                p1 = False
                rolled = True
            start += 1
        else:
            if rolled:
                try:
                    if mainBoard.checkQuestion(curplayer.getPos()):
                        curEmp = functions.isInEmpire(curplayer.getPos())
                        difb = True
                        main = False
                            
                    elif mainBoard.checkEvent(curplayer.getPos()):
                        drawECard
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
        drawQCard(width/2-350,height/4,700,height/2)    

    elif done:
        doneProc()
    if checkWinner() != False:
        winner = checkWinner()
        finish = True
    if finish:
        winScreen(winner)
        
            
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
    global dif,difb,quest,flash
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
        text("Slecht",x+w/3*2,y+h/2+widcheck/2)
        
    
def drawECard(x,y,w):
    pass

def rollProcess1():
    global start,turn
    start = 0
    turn += 1
    
def changeTurn():
    global players,curplayer
    try:
        players[(players.index(curplayer)+1)%len(players)].startTurn()
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
        text(lis[i].name + ":",x+w/4,y+(60*(i+1)))
        textAlign(LEFT)
        text("positie: " + str(lis[i].curpos) + ", vlaggen: " + str(lis[i].count),x+w/4+w/10,y+(60*(i+1)))
        text(empDict[lis[i].empire],x+w/4+w/10,y+(60*(i+1.4)))
        
    textAlign(LEFT)
    try:
        text("Aan de beurt: "+curplayer.name,x+w/4,y+(70*5))
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
    if not startb:
        startFunc()
    elif not(difb or quest or done):
        if p1:
            rollProcess1()
        else:
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

def mouseInRect(x,y,w,h):
    return (x < mouseX < x+w) and (y< mouseY < y+h)
def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
