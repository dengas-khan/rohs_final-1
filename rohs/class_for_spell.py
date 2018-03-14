class spell(object):
    def __init__(self, name, earth, fire, wind, water, lightning, atarget_list = None, gtarget_list = None, damage = None, heal=None, card_draw = None, minion_summon = None, buff = False, destroy = False, special_ability = None):
        self.name            = name
        self.earth           = earth
        self.fire            = fire
        self.wind            = wind
        self.water           = water
        self.lightning       = lightning        
        self.damage          = damage
        self.heal            = heal
        self.card_draw 	     = card_draw
        self.minion_summon   = minion_summon
        self.buff            = buff
        self.destroy         = destroy
        self.special_ability = special_ability
        self.is_played       = False 

        def deal_damage():
            if self.damage is not None:
                x = input('Who do you want to deal' + self.damage + 'to: ')
                if x in atarget_list:
                    x.health = x.health - self.damage
                    return x.health
                elif x == 'cancel':
                    pass
                else:
                    return deal_damage()

        def heal_damage():
            if self.heal is not None:
                x = input('Who do you want to heal' + self.damage + ': ')
                if x in btarget_list:
                    x.health = x.health + self.heal
                    return x.health
                elif x == 'cancel':
                    pass
                else:
                    return heal_damage()

        def card_draw():
            if self.card_draw is not None:
                for i in range(self.card_draw):
                    if Player1 in btarget_list:
                        draw_card(Player1)
                    elif Player2 in btarget_list:
                        draw_card(Player2)

        def buff():
            if self.buff is not None:
                x = input('Who do you want to give' + self.buff + 'to: ')
                if x in btarget_list():
                    return x
                else:
                    return buff()
            x.damage = x.damage + buff[0]
            x.health = x.health + buff[1]

        def destroy():
            if self.destroy is not None:
                if Player1 in atarget_list():
                    x = Player1
                elif Player2 in atarget_list():
                    x = Player2
                return x
            y = input('Which minion do you want to destroy: ')
            if y in atarget_list:
                return y
            else:
                return destroy()
            x.field.remove(y)
	
	
	
		
