class Player:
    __name = ""
    __Score = 0
    __hand = []
    __handScore = 0
    
    def __init__(this, name):
        this.__name = name

    def getName(this):
        return this.__name
    
    def getScore(this):
        return this.__Score
        
    def setScore(this, score):
        this.__Score = score
        
    def setHand(this, hand):
        this.__hand = hand
    
    def getHand(this, hand):
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
    
class Game:
    __discardList = []
    __player = None
    __computer = None
    __array = None
    __desk = None
    __idiotsArray = {'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}
    def printScores(this):
        Print(this.__player.getName + ":" + str(this.__player.getScore()))
        Print(this.__computer.getName + ":" + str(this.__computer.getScore()))
        
    def __init__(this, rule):
        rules = Rules()
        r = rules.getRule(rule)
        this.__deck = Deck(r['faces'])
        this.__player = Player(input('Enter your nae: '))
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
            this.declareWinner(1, this.__player.getHand(), this.__commputer.getHand())
        elif computerrank > playerrank:
            #Computer wins
            this.declareWinner(2, this.__player.getHand(), this.__commputer.getHand())
        elif computerrank == playerrank:
            if playerrank == 1:
                playerhand = getHandValue(this.__player.getHand())
                computerhand = getHandValue(this.__computer.getHand())
                if playerhand > 23:
                    playerhand = playerhand - 23
                if computerhand > 23:
                    computerhand = computerhand - 23
                    
                if  playerhand > computerhand:
                    #player wins
                    this.declareWinner(1, this.__player.getHand(), this.__commputer.getHand())
                elif computerhand > playerhand:
                    #computer wins
                else:
                    #Draw
        #If no winner, calculate score
        #If score > 23 then subtrac 23
        #Compare final scores, largest wins.
        #declare winner
        #Add score to final score for each player
        
    def discardAndDraw(this, playerid):
        if playerid == 1:
            #Loop until user quits and discard pile is verified
            #Start Loop
            #Print Hand
            #Request index # or letter q to finish
            #If letter q, check if discard pile is validation
            #If a number, check if index is valid, a repeated index will toggle the discard label
            #If index is valid, discard card
            #Loop

        else:
            #No AI for the computer at this point
            return
    
    def isArray(this, hand, arrayDef):
    
    def rankHand(this, hand):
        handvalue = getHandValue(hand)
        handrank = 0
        if handvalue == 23:
            handrank = 5
        elif handvalue == 46:
            handrank = 4
        elif isArray(hand, this.__idiotsArray):
            handrank = 3
        elif isArray(hand, this.__array):
            handrank = 2
        elif handvalue > 46:
            handrank = 0
        else:
            handrank = 1
            
        return handrank
    
    def getHandValue(this, hand):
        for c in hand:
            handvalue = handvalue + c.getValue()
            
g = Game('Standard')

print("Welcome to Sabacc.  The Poker game of the future")
print()
#Loop until use says "N"
print("Current Score")
g.printScores()
choice = input("Would you like to play a round? (Y/N)")
print()
g.play()
#end loop