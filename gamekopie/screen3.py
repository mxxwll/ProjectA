import screen2
from screen2 import *

def draw(playerNames):
    eersteSpeler = str(playerNames[0])
    
    f = createFont("Harrington",32)
    textFont(f,30) 
    w = width/7          
    x = width/2-width/7-width/14
    y = height/3
    x2 = width/2 + width/14
    y2 = y + w + height/14
    
    
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    #1player
    oneCo = [x,y,w,w]
    twoCo = [x2,y,w,w]
    threeCo = [x,y2,w,w]
    fourCo = [x2,y2,w,w]

    players = ""
    amountPlayers = False
    fill(0)   
    textFont(f)
    textSize(30)
    text(str(eersteSpeler) + ": Kies je rijk",width/2,height/8)
    
    fill(255,0,0,63)
    rect(*oneCo)
    rect(*twoCo)
    rect(*threeCo)
    rect(*fourCo)
    
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    
    fill(134,122,91,63)
    rect(*backCo)

    fill(0)
    
    # To-do: code schrijven in mousePressed van gamekopie (scherm == 3) en zo functions.py aanroepen.
    text("Groot-Brittanie",oneCo[0]+oneCo[2]/2,oneCo[1]+oneCo[3]/2)
    text("VOC",twoCo[0]+twoCo[2]/2,twoCo[1]+twoCo[3]/2)
    text("Spanje",threeCo[0]+threeCo[2]/2,threeCo[1]+threeCo[3]/2)
    text("Ottomaans Rijk",fourCo[0]+fourCo[2]/2,fourCo[1]+fourCo[3]/2)  
    
    
    
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    
    """

def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
