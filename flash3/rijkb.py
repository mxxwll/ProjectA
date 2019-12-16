#functie die een bool terugstuurd die aangeeft of de muis binnen een bepaald vierkant zit
def mouseInSquare(x,y,w):
    return (x < mouseX < x+w) and (y< mouseY < y+w)
def draw():
    global done,question,answer
    global flashproc,questionb,rijk
    global x1,x2,x3,x4,y,wid,rijk,dif
    global rijkb
    global c1,c2,c3,c4,c5,t1,t2,t3,t4,t5,filt
    #images
    frame = loadImage("frame.png")
    pistol = loadImage("pistol.png")
    pistoltwo = loadImage("pistoltwo.png")
    #colors
    maincolor = color(234,222,191)
    secondcolor = color(146,128,60)
    c1 = color(0,0,255)
    c2 = color(0,255,0)
    c3 = color(255,255,0)
    c4 = color(255,0,0)
    c5 = secondcolor
    t1 = color(0,0,170)
    t2 = color(0,170,0)
    t3 = color(170,170,0)
    t4 = color(170,0,0)
    t5 = color(91, 79, 37)
    
    c21 = secondcolor
    c22 = color(109, 95, 44)
    t21 = color(119,105,49)
    t22 = color(81,71,36)
    
    textSize(70)
    text("Welk Rijk?",width/2,height/7)
    textSize(50)
    wid = width/6
    x1 = width/24
    x2 = x1 + (wid+wid/2)
    x3 = x2 + (wid+wid/2)
    x4 = x3 + (wid+wid/2) 
    x5 =  width/2-wid/2  
    y = height/4
    
    if mouseInSquare(x1,y,wid):
        fill(t1)
    else:
        fill(c1)
    square(x1,y,wid)
    
    fill(0,0,0)
    text("Nederlandse\nRijk",x1+wid/2,y+wid/2.5)
    fill(255,255,255)
    
    if mouseInSquare(x2,y,wid):
        fill(t2)
    else:
        fill(c2)
    square(x2,y,wid)
    
    fill(0,0,0)
    text("Britse\nRijk",x2+wid/2,y+wid/2.5)
    fill(255,255,255)
    
    if mouseInSquare(x3,y,wid):
        fill(t3)
    else:
        fill(c3)
    square(x3,y,wid)
    
    fill(0,0,0)
    text("Spaanse\nRijk",x3+wid/2,y+wid/2.5)
    fill(255,255,255)
    
    if mouseInSquare(x4,y,wid):
        fill(t4)
    else:
        fill(c4)
    square(x4,y,wid)
    
    image(pistoltwo,width/2+width/4*0.5,height/2*1.3,width/4,width/7)
    
    fill(0,0,0)
    text("Ottomaanse\nRijk",x4+wid/2,y+wid/2.5)
    fill(255,255,255)
    
    if mouseInSquare(x5,y*2.5,wid):
        fill(t5)
    else:
        fill(c5)
    square(x5,y*2.5,wid)
    
    fill(0,0,0)
    text("Neutraal",width/2,y*2.5+wid/2)
    
    image(pistol,width/3-width/4*0.75,height/2*1.3,width/4,width/7)
