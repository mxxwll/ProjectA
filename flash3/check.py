def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
def draw():
    widcheck = width/10
    text("Goed of Fout?",width/2,height/7)
    if mouseInSquare(width/3-widcheck/2,height/2,widcheck):
        fill(0,155,0)
    else:
        fill(0,255,0)
    square(width/3-widcheck/2,height/2,widcheck)
    fill(0)
    text("Goed",width/3,height/2+widcheck/2)
    if mouseInSquare(width/3*2-widcheck/2,height/2,widcheck):
        fill(155,0,0)
    else:
        fill(255,0,0)
    square(width/3*2-widcheck/2,height/2,widcheck)
    fill(0)
    text("Slecht",width/3*2,height/2+widcheck/2)
    
