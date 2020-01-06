def draw():
    f = createFont("Harrington",32)
    textFont(f,30) 
    w = 90          
    x = 860
    y = 250
    x2 = x+100
    y2 = y+100
    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    text("Spelers",width/2,80)
    
    text("Kies hoeveel spelers er meedoen: ",width/2,120)
    
    fill(255,0,0,63)
    rect(x,y,w,w)
    rect(x2,y,w,w)
    rect(x,y2,w,w)
    rect(x2,y2,w,w)
    fill(0)
    text("1",905,300)
    text("2",1005,300)
    text("3",905,400)
    text("4",1005,400)  
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
