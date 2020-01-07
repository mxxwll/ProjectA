import functions
import random
add_library('minim')
test = Minim(this)

start = False


playernames = ["Liam","Jaikishan","Ali","Tugkan"]
p1 = functions.player(playernames[0],"otto")
p2 = functions.player(playernames[1],"nl")
p3 = functions.player(playernames[2],"spa")
p4 = functions.player(playernames[3],"eng")

empDict = {"otto":"Ottomaanse Rijk","nl":"Nederlandse Rijk","spa":"Spaanse Rijk","eng":"Engelse Rijk"}

mainColor = color(234,222,191)


players = [p1,p2,p3,p4]

roll1 = loadImage('een')
roll2 = loadImage('twee')
roll3 = loadImage('drie')
roll4 = loadImage('vier')
roll5 = loadImage('vijf')
roll6 = loadImage('zes')



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
    
    global mainDice
    mainDice = dice(width/2-100,height/2-100,200)
    
    global start,eind
    eind = 50
    start = eind
    
def draw():
    global mainDice,start
    
    background(mainColor)
    textAlign(CENTER)
    
    statBox(width-300,0,300,200)
    
    if start <= eind:
        mainDice.showdobbel(random.randint(1,6))
        start += 1
    else:
        mainDice.roll()
        fill(0)
        mainDice.showdobbel(mainDice.value)

    
def drawCard(empire):
    pass

def rollProcess():
    global start
    start = 0
def statBox(x,y,w,h):
    hollowRect(x,y,w,h)
    fill(0)
    textAlign(RIGHT)
    lis = [i for i in players]
    for i in range(len(players)):
        textAlign(RIGHT)
        text(players[i].name + ":",x+w/3,y+(40*(i+1)))
        text(players[i].curpos,x+w/2,y+(40*(i+1)))
        textAlign(LEFT)
        text(empDict[players[i].empire],x+w-w/3,y+(40*(i+1)))
        
def mousePressed():
    rollProcess()
