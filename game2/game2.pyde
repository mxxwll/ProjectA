import functions

playernames = ["Liam","Jaikishan","Jonas","Tugkan"]
p1 = functions.player(playernames[0],"otto")
p2 = functions.player(playernames[1],"nl")
p3 = functions.player(playernames[2],"spa")
p4 = functions.player(playernames[3],"eng")

mainColor = color(234,222,191)


players = [p1,p2,p3,p4]

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
    
def setup():
    size(1080,720)
    
    
    
    
def draw():
    background(mainColor)
    textAlign(CENTER)
    statBox(width-200,0,200,400)
def diceRoll():
    pass
def drawCard(empire):
    pass
def statBox(x,y,w,h):
    hollowRect(x,y,w,h)
    fill(0)
    textAlign(RIGHT)

    for i in range(len(players)):

        text(players[i].name + ":",x+w/3,y+(h/15*(i+1)))
        text(players[i].curpos + ,x+w-w/3,y+(h/15*(i+1)))
