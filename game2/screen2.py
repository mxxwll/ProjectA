
slist = []
s = ""
y = 1
shift = False
screenWidth = 1500
screenHeight = 800

backX = screenWidth/7
backY = screenHeight-screenHeight/4 
backW = 350
backH = 100
backCo = [backX,backY,backW,backH]
    
begin_ok_button = False
show_manual_display = False
show_empty_name_error = False

player1_box_selected = False
player2_box_selected = False
player3_box_selected = False
player4_box_selected = False
player5_box_selected = False
player6_box_selected = False

player1_name = ''
player2_name = ''
player3_name = ''
player4_name = ''
player5_name = ''
player6_name = ''

player_names = []
player_starting = 0

class screen2():
    def __init__(self):
        self.playerNames = []
        
    def setNames(self, y):
        self.playerNames = y
    
    def getNames(self):
        return self.playerNames
    
def backSpace(s):
    try:
        s = list(s)
        del s[-1]
    except:
        return ""
    else:
        s = "".join(s)
        return s
def endName():
    global s,slist,y
    if len(slist) < players-1:
        slist.append(s)
        s = ""
        if y != players:
            y += 1

def draw(players):
    name_input_screen(players)
    
        
    """
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    
    f = createFont("Harrington",32)
    global s
    textFont(f)
    textAlign(CENTER)             
    textSize(60)                           
    text("Spelers",width/2,height/8)
    textAlign(CENTER)
    text("Vul de namen in van de spelers:",width/2,height/8*2)
    textSize(40)
    textAlign(LEFT)
    for x in range(1,players+1):
        text("Speler " + str(x) + " :",width/3,height/4+(height/20*x))
    text(s,width/3+width/10,height/4+(height/20*y))
    
    fill(134,122,91,63)
    rect(*backCo)
    fill(0)
    textSize(75)
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    """
    
"""class Screen:
    def __init__(self, ):
        self.players
        
    def getPlayers(self):
        return self.players
    def setPlayers(self, amountOfPlayers):
        self.players = amountOfPlayers
    
"""

def name_input_screen(number_of_players):
    global name_input_screen_display, show_empty_name_error
    global player1_name, player2_name, player3_name, player4_name, player5_name, player6_name
    global s2, p
    
    
    
    backX = width/7
    backY = height-height/4
    backW = 350
    backH = 100
    backCo = [backX,backY,backW,backH]
    
    f = createFont("Harrington",32)
    #global s
    textFont(f)
    textAlign(CENTER)             
    #textSize(60)
    fill(0, 0, 0)
    text("Vul de namen in van de spelers:",width/2,height/8)
    
    
    #images[0].resize(width, height)
    #background(images[0])
    
    #font1 = createFont("Courier", 30)    
    #font2 = createFont("Courier", 35)
    
    #textFont(font1)
    #textAlign(CENTER)
    #fill(0)
    #text("Number of players: " + str(number_of_players), screenWidth/2, 100)
    
    x = number_of_players
    YPositionRect = 200
    YPositionText = 232
    y = player_number = 1
    
    while x > 0:        
        fill(255,255,255)
        rect(290, YPositionRect, 250, 40, 6)
        fill(0)
        text("Speler "+ str(y)+": ", 210, YPositionText)
        fill(255,255,255)
        x -= 1
        YPositionRect += 100
        YPositionText += 100
        y += 1
        
    """
    for x in range(1,number_of_players+1):     
        fill(0)
        text("Speler "+ str(y)+": ", 210, YPositionText)
        fill(255,255,255)
        #rect(290, YPositionRect, 250, 40, 8)
        x -= 1
        YPositionRect += 100
        YPositionText += 100
        y += 1
    """
    if player1_box_selected == True:
        fill(255)
        #rect(690, 200, 250, 40, 6)
    elif player2_box_selected == True:
        fill(230, 230, 230)
        #rect(690, 300, 250, 40, 6)
    elif player3_box_selected == True:
        fill(230, 230, 230)
        #rect(690, 400, 250, 40, 6)
    elif player4_box_selected == True:
        fill(230, 230, 230)
        #rect(690, 500, 250, 40, 6)
    #elif player5_box_selected == True:
        #fill(230, 230, 230)
        #rect(690, 600, 250, 40, 6)
    #elif player6_box_selected == True:
        #fill(230, 230, 230)
        #rect(690, 700, 250, 40, 6)

    fill(0, 0, 0)    
    textAlign(LEFT)
    text(player1_name, 300, 232)    
    text(player2_name, 300, 332)    
    text(player3_name, 300, 432)    
    text(player4_name, 300, 532)    
    text(player5_name, 300, 632)
    print(number_of_players)
    textAlign(CENTER)
    fill(255,255,255)
    #rect(720, 800, 60, 40, 6)   
     
    fill(0,0,0)
    text("OK", 760, 620)
    text("Terug",backCo[0]+backCo[2]/2,backCo[1]+backCo[3]*0.75)
    if number_of_players == 1:
        player_names = [player1_name]
    elif number_of_players == 2:
        player_names = [player1_name, player2_name]
    elif number_of_players == 3:
        player_names = [player1_name, player2_name, player3_name]
    elif number_of_players == 4:
        player_names = [player1_name, player2_name, player3_name, player4_name]
    elif number_of_players == 5:
        player_names = [player1_name, player2_name, player3_name, player4_name,player5_name]
                    

    
    s2 = screen2()
    s2.setNames(player_names)
   
        
    if show_empty_name_error == True:            
        fill(155, 155, 155) 
        rect(screenWidth/2 - 450, screenHeight/2 - 40, 900, 80, 6)
        fill(255,255,255)
        rect(screenWidth/2 + 360, screenHeight/2 - 20, 60, 40, 6)
        textAlign(CENTER)
        textFont(f) 
        fill(0,0,0)
        text("Voer voor alle spelers een naam in!", screenWidth/2 - 40, screenHeight/2 + 10)
        text("OK", screenWidth/2 + 390, screenHeight/2 + 10)
    
    
def getPlayerNames():
    p = s2.getNames()
    return p
        
        

    
def mousePressed(players):
    print(players)
    global number_of_players, name_input_screen_display, main_screen_display
    global player1_box_selected, player2_box_selected, player3_box_selected
    global player4_box_selected, player5_box_selected, player6_box_selected
    global player_starting
    global isMouseWithinSpace
    global show_empty_name_error
    number_of_players = players
    global s2
    
    if show_empty_name_error == True:
        if (mouseX >= screenWidth/2 + 360 and mouseX <= screenWidth/2 + 420) and (mouseY >= screenHeight/2 - 20 and mouseY <= screenHeight/2 + 20):
                show_empty_name_error = False
    #Checks if the user has clicked on a certain textbox to begin input
    else:
        if (mouseX >= 290 and mouseX <= 550) and (mouseY >= 200 and mouseY <= 240):
            player1_box_selected = True
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False        
        elif (mouseX >= 290 and mouseX <= 550) and (mouseY >= 300 and mouseY <= 340):
            player1_box_selected = False
            player2_box_selected = True
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False            
        elif (mouseX >= 290 and mouseX <= 550) and (mouseY >= 400 and mouseY <= 440):
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = True
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = False        
        elif ((mouseX >= 290 and mouseX <= 550) and (mouseY >= 500 and mouseY <= 540)) and number_of_players > 3:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = True
            player5_box_selected = False
            player6_box_selected = False        
        elif ((mouseX >= 290 and mouseX <= 550) and (mouseY >= 600 and mouseY <= 640)) and number_of_players > 4:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = True
            player6_box_selected = False            
        elif ((mouseX >= 290 and mouseX <= 550) and (mouseY >= 700 and mouseY <= 740)) and number_of_players > 5:
            player1_box_selected = False
            player2_box_selected = False
            player3_box_selected = False
            player4_box_selected = False
            player5_box_selected = False
            player6_box_selected = True
            
        #Detects wheter the OK button has been pressed
        elif (mouseX >= 620 and mouseX <= 680) and (mouseY >= 580 and mouseY <= 620):        
            if player1_name == '' or player2_name == '' or player3_name == '':
                show_empty_name_error = True
            elif number_of_players > 3 and player4_name == '':
                show_empty_name_error = True
            elif number_of_players > 4 and player5_name == '':
                show_empty_name_error = True
            elif number_of_players > 5 and player6_name == '':
                show_empty_name_error = True                                
            else:
                show_empty_name_error = False
                name_input_screen_display = False
                main_screen_display = True                        
                player1_box_selected = False
                player2_box_selected = False
                player3_box_selected = False
                player4_box_selected = False
                player5_box_selected = False
                player6_box_selected = False
                player_starting = int(random(0,number_of_players-1))
                if number_of_players == 1:
                    player_names = [player1_name]
                elif number_of_players > 1:
                    player_names = [player1_name, player2_name]
                elif number_of_players > 2:
                    player_names = [player1_name, player2_name, player3_name]
                elif number_of_players > 3:
                    player_names = [player1_name, player2_name, player3_name, player4_name]
                elif number_of_players > 4:
                    player_names = [player1_name, player2_name, player3_name, player4_name,player5_name]
                return player_names
                
            


def keyPressed():
    global player1_name, player2_name, player3_name, player4_name, player5_name, player6_name
    global player1_box_selected, player2_box_selected, player3_box_selected
    global player4_box_ted, player6_box_selected
    
    #Checks if the key pressed is a letter and if so adds it to the player whose textbox is currently selected
    if (key == 'a' or key == 'A' 
        or key == 'b' or key == 'B' 
        or key == 'c' or key == 'C'
        or key == 'd' or key == 'D'
        or key == 'e' or key == 'E' 
        or key == 'f' or key == 'F' 
        or key == 'g' or key == 'G'
        or key == 'h' or key == 'H'
        or key == 'i' or key == 'I' 
        or key == 'j' or key == 'J' 
        or key == 'k' or key == 'K'
        or key == 'l' or key == 'L'
        or key == 'm' or key == 'M' 
        or key == 'n' or key == 'N' 
        or key == 'o' or key == 'O'
        or key == 'p' or key == 'P'
        or key == 'q' or key == 'Q' 
        or key == 'r' or key == 'R' 
        or key == 's' or key == 'S'
        or key == 't' or key == 'T'
        or key == 'u' or key == 'U' 
        or key == 'v' or key == 'V' 
        or key == 'w' or key == 'W'
        or key == 'x' or key == 'X' 
        or key == 'y' or key == 'Y' 
        or key == 'z' or key == 'Z' 
        or key =='\b' or keyCode == 32):
        
        if (player1_box_selected == True) and (key != '\b'):
            if len(player1_name) < 10:
                player1_name += key
                
        elif (player1_box_selected == True) and (key == '\b'):
            player1_name = player1_name[:-1]
        
        elif (player2_box_selected == True) and (key != '\b'):
            if len(player2_name) < 10:
                player2_name += key
        elif (player2_box_selected == True) and (key == '\b'):
            player2_name = player2_name[:-1]
        
        elif (player3_box_selected == True) and (key != '\b'):
            if len(player3_name) < 10:
                player3_name += key
        elif (player3_box_selected == True) and (key == '\b'):
            player3_name = player3_name[:-1]
        
        elif (player4_box_selected == True) and (key != '\b'):
            if len(player4_name) < 10:
                player4_name += key
        elif (player4_box_selected == True) and (key == '\b'):
            player4_name = player4_name[:-1]
        
        elif (player5_box_selected == True) and (key != '\b'):
            if len(player5_name) < 10:
                player5_name += key
        elif (player5_box_selected == True) and (key == '\b'):
            player5_name = player5_name[:-1]
        
        elif (player6_box_selected == True) and (key != '\b'):
            if len(player6_name) < 10:
                player6_name += key
        elif (player6_box_selected == True) and (key == '\b'):
            player6_name = player6_name[:-1]
            
def hollowRect(x,y,w,h):
    line(x,y,x+w,y)
    line(x,y,x,y+h)
    line(x,y+h,x+w,y+h)
    line(x+w,y,x+w,y+h)
        
