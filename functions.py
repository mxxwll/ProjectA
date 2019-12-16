otto = list(range(1,13))
eng = list(range(41,53))
spa = list(range(21, 33))
nl = list(range(61,73))
neu1 = list(range(34, 40)) 
neu2 = list(range(54, 60))
neu3 = list(range(74, 80))
neu = neu1 + neu2 + neu3

global player, flagDict, player_count, player_names
player = 1
playerNames = []
flagDict = {
    'otto': 0,
    'eng': 0,
    'spa': 0,
    'nl': 0
}


ottoStart =[7]
engStart = [47]
spaStart = [27]
nlStart = [67]

ottoCard = [2, 4, 6, 9, 11, 13]
engCard = [42, 44, 46, 49, 51, 53]
spaCard = [22, 24, 26, 29, 31, 33]
nlCard = [62, 64, 66, 69, 71, 73]

embargoCard = [1]
boycotCard = [14, 54]
allianceCard = [34,74]

eventCard = [5, 10, 16, 19, 25, 30, 36, 39, 45, 50, 56, 59, 65, 70, 76]


def belongsToEmpire(currentPosition):

    """ Checks if the new position of the player matches an empire
    If previous position is a new empire (condition: neutral, empire), 
    it should trigger a deduction of the balance (tol)"""
    try:
        if currentPosition in otto: 
            print("Ottomanian Empire")
            return "otto"
        elif currentPosition in eng:
            print("British Empire")
            return "eng"
        elif currentPosition in spa:
            print("Spanish Empire")
            return "spa"
        elif currentPosition in nl:
            print("Dutch Empire")
            return "nl"
        elif currentPosition in neu:
            print("Neutral Zone")
            return "neu"
    except:
        print("Position is not found in the board game")
        return 0

def requestEmpireCard (whichEmpire, currentPosition):
    """Requests a question card with as parameter the relevant empire"""
    try:
        if whichEmpire == "otto" and number in ottoCard:
                  askCard("otto")
                  return "Otto Question card"
        elif whichEmpire == "spa" and number in engCard:
                  askCard("spa")
                  return "Spanish Question card"
    
        elif whichEmpire == "eng" and number in spaCard:
                  askCard("eng")
                  return "English Question card"
        elif whichEmpire == "nl" and number in nlCard:
             askCard("nl")
             return "Dutch Question card"
        
        elif whichEmpire == "neu" and number in neuCard:
             askCard("neu")
             return "General Question card"
    

    except:
        print("Position of the player does not trigger a question card")
        return 0

def triggerEmpireCard(empireName):
    print("Empire card drawn")


def triggerEvent (newPosition):
    if newPosition in embargoCard:
        embargoEvent(player)
        print ("Embargo position")
        
    elif newPosition in boycotCard:
        boycotEvent(player)
        print ("Boycot position")
        
    elif newPosition in allianceCard:
        allianceEvent(player)
        print ("Alliance position")
        
    elif newPosition in eventCard:
        print ("Random event card")
        drawEventCard(player)
        
    else:
        print ("Alas, nothing happened.")
        

def nextPlayer():
    print("Next player")
    
def drawEventCard(player):
    """
    """
def boycotEvent(player):
    print("Boycot")

def allianceEvent(player):
    print("Alliance")

def embargoEvent(player):
    """Code: Player waits one turn and can't dice in the next round."""
    print("Embargo")

def inputPlayer():
    player_count = int(input("How many players? (2-6): "))
    for i in range(1, player_count + 1):
        spelerNaam = input("Input player " + str(i) + "'s name: ")
        playerNames.append(spelerNaam)

    return player_count

def assignEmpire(player_count):
    """ To do: make sure an empire is not already used by a player"""

    for i in range(player_count):
        empirePlayer = input(playerNames[i] + " , which Empire would you like to take: (otto, eng, spa, ned) " + "\n")
        if empirePlayer== 'otto':
            flagDict['otto'] = i
            print(str("Player " + playerNames[i]) + " claimed the Ottomanian empire and starts on " + str(ottoStart) + "\n")
        elif empirePlayer == 'eng':
            flagDict['eng'] = i
            print(str("Player " + playerNames[i]) + " claimed the empire of England and starts on " + str(engStart) + "\n")
        elif empirePlayer == 'spa':
            print(str("Player " + playerNames[i]) + " claimed the empire of Spain and starts on " + str(spaStart) + "\n")
            flagDict['spa'] = i
        elif empirePlayer == 'ned':
            print(str("Player " + playerNames[i]) + " claimed the empire of the Netherlands and starts on " + str(nlStart) )
            flagDict['ned'] = i
        else:
            print("Invalid input")
            assignEmpire(player_count)

    return player_count, flagDict

def empireToPlayer(empire):
    if empire  == flagDict.keys:
        
    else:
        return "Doesn't belong to any player"
        

def main():
    amountOfPlayers = inputPlayer()
    assignEmpire(amountOfPlayers)
    whichNumber = int(input("Position of the player (under 80): "))
    whichEmpire = belongsToEmpire(whichNumber)

    requestEmpireCard(whichNumber, whichNumber)
    triggerEvent(whichNumber)
    nextPlayer()
    print("\n")
    main()

if __name__ == "__main__":
        main()

