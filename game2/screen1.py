def draw():
    f = createFont("Harrington",32)
    textFont(f,30) 
    ws1 = width/8          
    xs1 = width/2-width/7-width/14
    ys1 = height/3.5
    x2s1 = width/2 + width/14
    y2s1 = ys1 + ws1 + height/14
    
    twoCo = [xs1,ys1,ws1,ws1]
    threeCo = [x2s1,ys1,ws1,ws1]
    fourCo = [xs1,y2s1,ws1,ws1]
    fiveCo = [x2s1,y2s1,ws1,ws1]
    
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    #1player
    
    
    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    textSize(60)
    text("Spelers",width/2,height/8)
    textSize(50)
    text("Kies hoeveel spelers er meedoen: ",width/2,height/4.5)
    
    fill(255,0,0,63)
    rect(*twoCo)
    rect(*threeCo)
    rect(*fourCo)
    rect(*fiveCo)
    
    fill(134,122,91,63)
    rect(*backCo)

    fill(0)
    text("2",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
    text("3",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
    text("4",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)
    text("5",fiveCo[0]+fiveCo[2]/2,fiveCo[1]+fiveCo[3]/2)  
    
    
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
    
