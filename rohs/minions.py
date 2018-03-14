import weakref


class minion(object):
    minion_list = list()
    instances   = list()
    def __init__(self, name, damage, health, devotion, devotioncost, race = None, image = None, card = None, stealth = False, poison = False, taunt = False, charge = False, rush = False, battlecry = None, deathrattle = None):
        self.instances.append(weakref.proxy(self))
        self.name 	          = name
        self.health               = health
        self.damage               = damage
        self.devotion             = devotion
        self.race                 = race
        self.image                = image
        self.card                 = card
        self.stealth              = stealth
        self.poison               = poison
        self.taunt                = taunt
        self.charge               = charge
        self.rush                 = rush
        self.battlery             = battlecry
        self.deathrattle          = deathrattle
        self.played               = False
        self.has_attacked         = False
        self.devotion             = devotion
        exec("global "+ devotion[0]+'; self.'+devotion[0]+'=+devotioncost[0]')
        if devotion[1]!=None:
            exec("global "+ devotion[1]+'; self.'+devotion[1]+'=+devotioncost[1]')            
     
            
        if self.played == True:
            if self.battlecry is not None:
                self.battlecry
                       
        def death(self):
            self.owner.field.remove(self)
            print('rip')
            if self.deathrattle is not None:
                return self.deathrattle


    def return_name_var(self):
        """used when adding a minion to the class"""

        return [k for k,v in globals().items() if k is self][0]

    

#Frostling = minion('Frostling', 1, 1, ['water'], [1], 'elemental')

Toxic_Guardshroom1 = minion('Toxic Guardshroom', 0, 7, ['earth', 'water'], [1, 2], 'plant', 'minion3.png', 'card3.png', False, True, True)
Toxic_Guardshroom2 = minion('Toxic Guardshroom', 0, 7, ['earth', 'water'], [1, 2], 'plant', 'minion3.png', 'card3.png', False, True, True)

Lily1 = minion('Lily, Green Gardener', 1, 3, ['earth',None], [2], None, 'minion1.png', 'card1.png')
Lily2 = minion('Lily, Green Gardener', 1, 3, ['earth',None], [2], None, 'minion1.png', 'card1.png')

Tree_cub1 = minion('Tree cub', 1, 2, ['earth',None], [1], 'beast', 'minion2.png', 'card2.png')
Tree_cub2 = minion('Tree cub', 1, 2, ['earth',None], [1], 'beast', 'minion2.png', 'card2.png')
Tree_cub3 = minion('Tree cub', 1, 2, ['earth',None], [1], 'beast', 'minion2.png', 'card2.png')



Evil_Toxic_Guardshroom1 = minion('Toxic Guardshroom', 0, 7, ['earth', 'water'], [1, 2], 'plant', 'minion3.png', 'card3.png', False, True, True)
Evil_Toxic_Guardshroom2 = minion('Toxic Guardshroom', 0, 7, ['earth', 'water'], [1, 2], 'plant', 'minion3.png', 'card3.png', False, True, True)

Evil_Lily1 = minion('Lily, Green Gardener', 1, 3, ['earth',None], [2], None, 'minion1.png', 'card1.png')
Evil_Lily2 = minion('Lily, Green Gardener', 1, 3, ['earth',None], [2], None, 'minion1.png', 'card1.png')

Evil_Tree_cub1 = minion('Tree cub', 1, 2, ['earth',None], [1], 'beast', 'minion2.png', 'card2.png')
