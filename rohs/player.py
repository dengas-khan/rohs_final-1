class Hero(object):
    def __init__(self, name, deck):
        self.name = name
        self.health = 30
        def get_devotion1():
            x = input('Enter your primary devotion ' + self.name + ': ')
            elements = ['earth', 'fire', 'water', 'wind', 'lightning']
            if x in elements:
                return x
            else:
                return get_devotion1()
        def get_devotion2():
            y = input('Enter your second devotion ' + self.name + ': ')
            elements = ['earth', 'fire', 'water', 'wind', 'lightning']
            if y in elements and y != self.devotion1:
                return y
            elif y == 'none':
                return None
            else:
                return get_devotion2()
            
        self.devotion1 = None
        self.devotion2 = None
        self.dev_val1 = 0
        self.dev_val2 = 0
        self.dev_val_max1 = 0
        self.dev_val_max2 = 0
        self.field = list()
        self.hand = list()
        self.deck = deck

Player1 = Hero('Player1', [])
Player2 = Hero('Player2', [])

def test():
    print(Player1.name)
    print(Player1.health)
    print(Player1.devotion1)
    print(Player1.devotion2)

setattr(Player1, 'devotion1', 'earth')
setattr(Player1, 'devotion2', 'water')
setattr(Player2, 'devotion1', 'fire')
setattr(Player2, 'devotion2', 'wind')
