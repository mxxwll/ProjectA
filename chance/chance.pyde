
def setup():
    global maincolor,secondcolor
    global frame
    global button1args
    fullScreen()
    frame = loadImage("frame.png")
    #colors
    maincolor = color(234,222,191)
    secondcolor = color(146,128,60)
    wid = width/8
    button1args = [width/2-wid,height/2,wid,wid]

def draw():
    background(maincolor)
    image(frame,0,0,width,height)
    button1 = rect(*button1args)
