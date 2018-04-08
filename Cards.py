import random
     
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
        
    def discard(this):
        this.__discarded = not this.__discarded
        return this.__discarded
        
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
            list1.append(this.draw(1)[0])
            list2.append(this.draw(1)[0])
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
                    this.__cards.append(Card(suit, i+1))
            for face,value in this.__faces.items():
                this.__cards.append(Card(face,value))
                this.__cards.append(Card(face,value))
            this.shuffle()
            
