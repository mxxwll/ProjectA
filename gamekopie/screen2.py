slist = []
s = ""
y = 1
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
    global s,slist,y
    if len(slist) < players-1:
        slist.append(s)
        s = ""
        if y != players:
            y += 1
def draw(players):
    f = createFont("Harrington",32)
    global s
    textFont(f)
    textAlign(CENTER)             
    textSize(60)                           
    text("Spelers",width/2,height/8)
    textAlign(CENTER)
    text("Vul de namen in van de spelers:",width/2,height/8*2)
    textSize(40)
    textAlign(LEFT)
    for x in range(1,players+1):
        text("Speler " + str(x) + " :",width/3,height/4+(height/20*x))
    text(s,width/3+width/10,height/4+(height/20*y))

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
        
