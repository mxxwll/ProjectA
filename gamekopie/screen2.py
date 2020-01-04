slist = []
s = ""
shift = False
def backSpace(s):
    try:
        s = list(s)
        del s[-1]
    except:
        return ""
    else:
        s = "".join(s)
        return s
def endName():
    global slist
    if len(slist) < players-1:
        slist.append(s)
        s = ""
def draw(players):
    f = createFont("Harrington",32)
    global s
    textFont(f)
    textAlign(CENTER)                                        
    text("Spelers",width/2,80)
    textAlign(CENTER)
    text("Vul de namen in van de spelers:",width/2,120)
    textAlign(LEFT)
    for x in range(1,players+1):
        text("Speler " + str(x) + " :",width/3,100+(48*x))
    text(s,width/2.4,145)

def keyPressed():
    global s,shift
    print(keyCode)
    if keyCode == 13:
        endName()
    else:
        if keyCode == 16:
            shift = True
        else:
            shift = False
            if len(s) < 12:
                if keyCode == 8:
                    s = backSpace(s)
                else:
                    if shift:
                        s += str(key).upper()
                    else:
                        s += str(key)
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
        
