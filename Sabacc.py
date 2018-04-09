from Cards import *
from Variants import Rules

class Player:
    __name = ""
    __Score = 0
    __hand = []
    __handScore = 0
    __discardCount = 0
    def __init__(this, name):
        this.__name = name

    def getDiscardCount(this):
        return this.__discardCount

    def getName(this):
        return this.__name
    
    def getScore(this):
        return this.__Score
        
    def setScore(this, score):
        this.__Score = score
        
    def setHand(this, hand):
        this.__hand = hand
    
    def getHand(this):
        return this.__hand
    
    def getCard(this, index):
        return this.__hand[index]
    
    def AddCard(this, card):
        if len(this.__hand) == 4:
            print("Can't add any more cards to the hand")
        else:
            this.__hand.append(card)
    
    def removeCard(this, cardIndex):
        this.__hand.pop(cardIndex)

    def printHand(this):
        for i,d in enumerate(this.__hand):
            print(str(i)+") " + d.getName())

    def discardCard(this, index):
        if this.getCard(index).discard():
            this.__discardCount = this.__discardCount + 1
        else:
            this.__discardCount = this.__discardCount - 1

    def cleanHand(this):
        handCopy = this.__hand[:]
        for c in handCopy:
            if c.isDiscarded():
                this.__hand.remove(c)
        this.__discardCount = 0

    def hasSuit(this, suit):
        for c in this.__hand:
            if c.getSuit() == suit:
                return True
        return False
    
class Game:
    __discardList = []
    __player = None
    __computer = None
    __array = None
    __desk = None
    __idiotsArray = {'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}
    __rules = None
    def getArray(this,type=0):
        if type == 0:
            return this.__idiotsArray
        else:
            return this.__array

    def printScores(this):
        print(this.__player.getName() + ":" + str(this.__player.getScore()))
        print(this.__computer.getName() + ":" + str(this.__computer.getScore()))
        
    def __init__(this, rule):
        this.__rules = Rules()
        r = this.__rules.getRule(rule)
        this.__deck = Deck(r['faces'])
        this.__player = Player(input('Enter your name: '))
        this.__computer = Player('Computer')
        this.__discardList = r['discardList']
        this.__array = r['array']
        
    def play(this):
        ph, ch = this.__deck.deal()
        this.__player.setHand(ph)
        this.__computer.setHand(ch)
        this.discardAndDraw(1)  #player
        this.discardAndDraw(2)  #computer
        playerrank = this.rankHand(this.__player.getHand())
        computerrank = this.rankHand(this.__computer.getHand())
        if playerrank > computerrank:
            #Player wins
            this.declareWinner(1, this.__player.getHand(), this.__computer.getHand())
        elif computerrank > playerrank:
            #Computer wins
            this.declareWinner(2, this.__player.getHand(), this.__computer.getHand())
        elif computerrank == playerrank:
            if playerrank == 1:
                playerhand = this.getHandValue(this.__player.getHand())
                computerhand = this.getHandValue(this.__computer.getHand())
                if playerhand > 23:
                    playerhand = playerhand - 23
                if computerhand > 23:
                    computerhand = computerhand - 23
                if  playerhand > computerhand:
                    #player wins
                    this.declareWinner(1, this.__player.getHand(), this.__computer.getHand())
                elif computerhand > playerhand:
                    #computer wins
                    this.declareWinner(2, this.__player.getHand(), this.__computer.getHand())
                    pass
                else:
                    #Draw
                    pass
        #If no winner, calculate score
        #If score > 23 then subtrac 23
        #Compare final scores, largest wins.
        #declare winner
        #Add score to final score for each player
        
    def discardAndDraw(this, playerid):
        print()
        if playerid == 1:
            print("Player's Turn")
            this.changeHand(this.__player)
            this.__player.printHand()
        else:
            print("Computer's Turn")
            this.changeHand(this.__computer)
            this.__computer.printHand()

    def changeHand(this, owner):
        loop = True
        draw = 0
        while(loop):
            owner.printHand()
            print("Discarded: " + str(owner.getDiscardCount()))
            index = input("Select Card to Discard (q to continue): #")

            if index == 'q':
                draw = owner.getDiscardCount()
                discardRules = this.__discardList
                if draw in discardRules.keys():
                    if discardRules[draw] == "*":
                        loop = False
                    else:
                        if owner.hasSuit(discardRules[draw]):
                            loop = False
                        else:
                            print("You need a " + discardRules[draw] + " to discard " + str(draw) + " cards")
                else:
                    message = "You can only discard "
                    for x in discardRules.keys():
                        message = message + str(x) + ", "
                    print(message + " cards using the current rules")
            elif this.isInt(index) and int(index) < 4:
                owner.discardCard(int(index))
        owner.cleanHand()
        newCards = this.__deck.draw(draw)
        for c in newCards:
            owner.AddCard(c)

    def isInt(this, v):
        try:     i = int(v)
        except:  return False
        return True

    def declareWinner(this, playerid, hand1, hand2):
        if playerid == 1:
            print("Player won")
        else:
            print("Computer won")
        playerscore = this.figureScore(hand1)
        computerscore = this.figureScore(hand2)
        this.__player.setScore(this.__player.getScore() + playerscore)
        this.__computer.setScore(this.__computer.getScore() + computerscore)

    def figureScore(this, playerhand):
        score = 0
        if this.isArray(playerhand, this.__idiotsArray) or this.isArray(playerhand, this.__array):
            score = 23
        else:
            score = this.getHandValue(playerhand)

        if score > 46:
            score = 46 - score #if over 46 decrease score by difference
        elif score > 23:
            score = score - 23
        return score
        

    def isArray(this, hand, arrayDef):
        ###################
        #Array List format
        ###################
        #value:suit
        #Value can be a wild card # = any number, r = any face, * = any value
        #Value can also be a specific value 1 - 15
        #suit can be a wild card * = any suit, f = any face
        #suit can also be a specific suit or face name
        #I'm using strings instead of dicts as they will share keys
        matchList = []
        arrayDef = arrayDef['cards']
        for j in arrayDef:
            value,suit = j.split(':')
            for i,c in enumerate(hand):
                if this.compareValues(value, c.getValue()): 
                    if this.compareSuits(suit, c.getSuit()):
                        if not i in matchList:
                            matchList.append(i)

        return len(matchList) >= len(arrayDef)

    def compareValues(this, value1, value2):
        if this.isInt(value1): value1 = int(value1)
        if value1 == "*":
            return True
        elif value1 == "#":
            return True
        else:
            if value1 == value2:
                return True
        return False

    def compareSuits(this, suit1, suit2):
        if suit1 == "*":
            if suit2 in ['Staves', 'Sabers', 'Flasks', 'Coins']:
                return True
        elif suit1 == "f":
            if suit2 in ['Idiot', 'Rancor','Jedi Knight','Jedi Master','Dark Jedi', 'Lord of the Sith', 'Smuggler', 'Bounty Hunter']:
                return True
        else:
            if suit1 == suit2:
                return True
        return False

    def rankHand(this, hand):
        handvalue = this.getHandValue(hand)
        handrank = 0
        if handvalue == 23:
            handrank = 5
        elif handvalue == 46:
            handrank = 4
        elif this.isArray(hand, this.__idiotsArray):
            handrank = 3
        elif this.isArray(hand, this.__array):
            handrank = 2
        elif handvalue > 46:
            handrank = 0
        else:
            handrank = 1
            
        return handrank
    
    def getHandValue(this, hand):
        handvalue = 0
        for c in hand:
            handvalue = handvalue + c.getValue()
        return handvalue
r = Rules().getRuleNames()
for i,rule in enumerate(r):
    print(str(i+1) + ") " + rule)
ruleSelection = input("Select a rule to play Sabacc: " )
if ruleSelection.isdigit():
    ruleSelection = int(ruleSelection) - 1
else:
    ruleSelection = 0 

g = Game(r[ruleSelection])
#g = Game('Old Republic')
print("Welcome to Sabacc.  The Poker game of the future")
print()
choice = "Y"
while(choice != "n"):
#Loop until user says "N"
    print("Current Score")
    g.printScores()
    g.play()
    choice = input("Would you like to play another round? (Y/N)").lower()
#end loop
print()
print("Final Scores")
print()
g.printScores()