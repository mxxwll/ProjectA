def draw():
    f = createFont("Harrington",32)
    textFont(f,30) 
    w = width/7          
    x = width/2-width/7-width/14
    y = height/3
    x2 = width/2 + width/14
    y2 = y + w + height/14
    
    #1player
    oneCo = [x,y,w,w]
    twoCo = [x2,y,w,w]
    threeCo = [x,y2,w,w]
    fourCo = [x2,y2,w,w]
    
    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    textSize(75)
    text("Spelers",width/2,height/8)
    
    text("Kies hoeveel spelers er meedoen: ",width/2,height/5)
    
    fill(255,0,0,63)
    rect(*oneCo)
    rect(*twoCo)
    rect(*threeCo)
    rect(*fourCo)
    fill(0)
    text("1",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
    text("2",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
    text("3",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
    text("4",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)  
    
    
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
