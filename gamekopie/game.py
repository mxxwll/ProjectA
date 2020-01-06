def draw():
    #stat box
    hollowRect(*statBox)
    for i in range(1,players+1):
        text("speler " + str(i) + ":",statBox[0]+statBox[2]/4,statBox[1]+statBox[3]/5+i*25)
        
