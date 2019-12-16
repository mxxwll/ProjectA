def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
def draw():
    text("Kies moeilijkheid",width/2,height/4)
    #colors
    secondcolor = color(146,128,60)
    c21 = secondcolor
    c22 = color(109, 95, 44)
    t21 = color(119,105,49)
    t22 = color(81,71,36)
    
    wid2 = width/5    
    x21 = width/3-wid2    
    x22 = width/3*2
    y21 = height/2
    if mouseInSquare(x21,y21,wid2):
        fill(t21)
    else:
        fill(c21)
    square(x21,y21,wid2)
    
    fill(0)
    text("Makkelijk",x21+wid2/2,y21+wid2/2)
    if mouseInSquare(x22,y21,wid2):
        fill(t22)
    else:
        fill(c22)
    square(x22,y21,wid2)
    fill(0)
    text("Moeilijk",x22+wid2/2,y21+wid2/2)
