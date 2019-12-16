#functie die een bool terugstuurd die aangeeft of de muis binnen een bepaald vierkant zit
def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
def draw(question): 
    textSize(70)
    text("Vraag:",width/2,height/3)
    textSize(40)
    text(question,width/20,height/2-height/10,width-width/10,height/2)
