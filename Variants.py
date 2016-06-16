import random
#####################
#Discard List format
#####################
#For each number of allowed discarded cards and required card for that value the format is
#(NumOfCards,FaceName)
#FaceName can be a wild card * = any card or no validation
#If you cannot discard more or less than 2 your list would be [(0,'*'),(2,'*')]
###################
#Array List format
###################
#value:suit
#Value can be a wild card # = any number, r = any face, * = any value
#Value can also be a specific value 1 - 15
#suit can be a wild card * = any suit, f = any face
#suit can also be a specific suit or face name
class Rules:
    def getRule(this, rule):
        r = rule.lower()
        if r == "old republic":
            return {'faces': {'Idiot':0,
                              'Rancor':9,
                              'Jedi Knight':3,
                              'Jedi Master':3,
                              'Dark Jedi':-14, 
                              'Lord of the Sith':10,
                              'Smuggler'10:, 
                              'Bounty Hunter':9
                             },
                    'discardList': [(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master')(4,'Jedi Master')]
                    'array':{'name':"Jedi's", 'cards':['*:Jedi Knight', '*:Jedi Master', '#:Saber']}
            }
        elif r == "rebel alliance"
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':3,
                              'Jedi Master':4,
                              'Dark Jedi':12, 
                              'Lord of the Sith':-10,
                              'Smuggler':5, 
                              'Bounty Hunter':9
                             },
                    'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'*')]
                    'array':{'name':'Force', 'cards':['*:Jedi Knight', '*:Jedi Knight', '15:*']}
            }
        elif r == "new republic"
            return {'faces': {'Idiot':0,
                              'Rancor':8,
                              'Jedi Knight':4,
                              'Jedi Master':3,
                              'Dark Jedi':12, 
                              'Lord of the Sith':-11,
                              'Smuggler':4, 
                              'Bounty Hunter':10
                             },
                    'discardList':[(0,'*'), (1,'*'), (3,'*')]
                    'array':{'name':"Republic's", 'cards':['*:Jedi Knight', '*:Jedi Master', '*:Smuggler']}
            }
        elif r == "imperial"
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':15,
                              'Jedi Master':-9,
                              'Dark Jedi':3, 
                              'Lord of the Sith':4,
                              'Smuggler':7, 
                              'Bounty Hunter':3
                             },
                    'discardList': [(0,'*'), (2,'*')]
                    'array':{'name':"Sith", 'cards':['*:Lord of the Sith', '*:Commander', '15:*']}
            }
        elif r == "cloud city casino"
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':4,
                              'Jedi Master':6,
                              'Dark Jedi':9, 
                              'Lord of the Sith':-8,
                              'Smuggler':5, 
                              'Bounty Hunter':7
                             },
                    'discardList':[(0,'*'), (2,'*'), (4,'*')]
                    'array':{'name':'Partnership', 'cards':['*:Jedi Knight', '*:Smuggler', '*:Smuggler']}
            }
        elif r == "mos eisley"
            return {'faces': {'Idiot':0,
                              'Rancor':5,
                              'Jedi Knight':7,
                              'Jedi Master':8,
                              'Dark Jedi':-11, 
                              'Lord of the Sith':10,
                              'Smuggler':6, 
                              'Bounty Hunter':5
                             },
                    'discardList':[(0,'*'), (1,'*'), (4,'Bounty Hunter'), (4,'Smuggler')]
                    'array':{'name':'Force', 'cards':['*:Smuggler', '*:Bounty Hunter', '#:Coin']}
            }        
        elif r == "corellian"
            return {'faces': {'Idiot':0,
                              'Rancor':4,
                              'Jedi Knight':10,
                              'Jedi Master':-13,
                              'Dark Jedi':11, 
                              'Lord of the Sith':11,
                              'Smuggler':4, 
                              'Bounty Hunter':3
                             },
                    'discardList':[(0,'*'), (2,'*'), (3,'*'), (4,'*')]
                    'array':{'name':"Smuggler's", 'cards':['*:Smuggler', '*:Smugler', '#:Coin']}
            }        
        elif r == "corporate sector"
            return {'faces': {'Idiot':0,
                              'Rancor':5,
                              'Jedi Knight':-7,
                              'Jedi Master':8,
                              'Dark Jedi':7, 
                              'Lord of the Sith':8,
                              'Smuggler':6, 
                              'Bounty Hunter'3:
                             },
                    'discardList':[(0,'*'), (3,'*')]
                    'array':{'name':"Hunter's", 'cards':['*:Bounty Hunter', '*:Bounty Hunter', '#:Coin']}
            }        
        elif r == "crseih station"
            return {'faces': {'Idiot':0,
                              'Rancor':7,
                              'Jedi Knight':8,
                              'Jedi Master':-6,
                              'Dark Jedi':5, 
                              'Lord of the Sith':4,
                              'Smuggler':6, 
                              'Bounty Hunter':6
                             },
                    'discardList':[(0,'*'), (1,'*'),(2,'*')]
                    'array':{'name':'Force', 'cards':['*:Flask', '*:Flask', '*:Flask', '*:Flask']}
            }        
        else:
            return {'faces': {'Idiot':0,
                              'Rancor':9,
                              'Jedi Knight':3,
                              'Jedi Master':3,
                              'Dark Jedi':-14, 
                              'Lord of the Sith':10,
                              'Smuggler'10:, 
                              'Bounty Hunter':9
                             },
                    'discardList':[(0,'*'), (1,'*'), (2,'*'), (3,'Jedi Master')(4,'Jedi Master')]
                    'array':{'name':"Idiot's", 'cards':['*:Idiot', '2:*', '3:*']}
            }       
class Card:
    __suit = ""
    __value = ""
    __image = ""
    __discarded = False
    def __init__(this, suit, value):
        this.__suit = suit
        this.__value = value
        if suit in ['Staves', 'Sabers', 'Flasks', 'Coins']:
            this.__image = str(value) + suit + '.png'
        else:
            this.__image = suit + '.png'
    
    def getSuit(this):
        return this.__suit
        
    def getName(this):
        name = ""
        if this.__suit in ['Staves', 'Sabers', 'Flasks', 'Coins']:
            if this.__value == 12:
                name = "Commander of " + this.__suit
            elif this.__value == 13:
                name = "Mistress of " + this.__suit
            elif this.__value == 14:
                name = "Master of " + this.__suit
            elif this.__value == 15:
                name = "Ace of " + this.__suit
            else:
                name = str(this.__value) + " of "  + this.__suit
        else:
            name = this.__suit
            
        if this.__discarded:
            name = "(discarded) " + name
        return name
            
    def getValue(this):
        return this.__value
        
    def getImage(this):
        return this.__image
    
    def isDiscarded(this):
        return this.__discarded
        
    def discard(this, index):
        this.__discarded = !this.__discarded
        
class Deck():
    __faces = {}
    __cards = []
    __discardPile = []
    
    def shuffle(this):
        random.shuffle(this.__cards)
    
    def deal(this):
        list1 = []
        list2 = []
        for i in range(4):
            list1.append(this.draw(1))
            list2.append(this.draw(1))
        if len(this.__cards) < 16:
            this.shuffle()
        
        return (list1, list2)
    
    def draw(this, num):
        list1 = []
        for i in range(num):
            list1.append(this.__cards.pop(0))
        this.__discardPile = this.__discardPile + list1
        return list1
    
    def __init__(this,faces):
            this.__faces = faces
            suits = ['Staves', 'Sabers', 'Flasks', 'Coins']
            ranked = {'Commander':12, 'Mistress':13, 'Master':14, 'Ace':15}
            for suit in suits:
                for i in range(16):
                    this.__cards.append(Card(suit, i))
            for face,value in this.__faces.iteritems():
                this.__cards.append(Card(face,value))
                this.__cards.append(Card(face,value))
            this.shuffle()
            
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