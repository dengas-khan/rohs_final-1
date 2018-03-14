"""
this is the file for the 
minions
"""


from class_for_minion import minion

'''
Earth = Ramp                             Control
Gain devotion quickly to play large minions

Fire = Burn                              Aggro
Damage spells and effects

Water = Spells                           Combo
Spells with uniue effects

Wind = Agressive                         Aggro
Small minions and windfury

Lightning = ??                           ??

Earth + Fire = Lava                      Midrange
AoE spells and big minions 

Earth + Water = Nature                   Contorl
Lots of ramping to play minions that can get more powerful with spells and effects
Unique: Blossom - use extra devotion to make minions gain better stats and abilities 

Earth + Wind =                           ??

Earth + Lightning = Explosion            Midrange
Lots of deathrattle effects and ways to activate and resummon them

Fire + Water = Boil                      Aggro
Lots of damage spells and effects to the face
Unique: Erupt - gain extra spell damage  

Fire + Wind = Scorch                     Tempo
Small rush and charge minions with damage spells and effects
Unique: phoenix - cards that can return after death  

Fire + Lightning =                       ??

Water + Wind = Ice                       Tempo
Tokens and buffing spells
Unique: Blizzard - whenever you play a spell effects 

Water + Lightning = Storm                Control / Combo
Lots of spells to build up to an op in condition  
Unique: Brood - cards' devotion costs can decrease with effects 

Wind + Lightning =                       ?? 
'''
Frostling = minion('Frostling', 2, 1, 0, 0, 0, 1, 0, 'elemental')
def test():
    print(Frostling.name)
    print(Frostling.damage)
    print(Frostling.health)
    print(Frostling.race)

Toxic_Guardshroom = ('Toxic Guardshroom', 7, 0, 2, 0, 0, 2, 0, 'plant', False, True, True)
