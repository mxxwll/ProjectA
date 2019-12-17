s = ''
def draw(players):
    f = createFont("Harrington",32)
    global s
    textFont(f)
    textAlign(CENTER)                                        
    text("Spelers",width/2,80)
    textAlign(CENTER)
    text("Vul de namen in van de spelers",width/2,120)
    
    for x in range(1,players+1):
        text("Speler " + str(x) + " :",width/3,100+(48*x))
    text(s,width/2.4,145)

def keyPressed():
    global s
    s += key
