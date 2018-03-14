from minions import *
from player import *
        
setattr(Player1, 'water', 1)
setattr(Player2, 'water', 1)
Player1.field.append(Toxic_Guardshroom1)
Player1.field.append(Lily1)
Player1.field.append(Tree_cub1)
Player1.field.append(Tree_cub2)
Player1.hand.append(Tree_cub3)
Player1.hand.append(Lily2)
Player1.hand.append(Toxic_Guardshroom2)
Player2.field.append(Evil_Toxic_Guardshroom1)
Player2.field.append(Evil_Lily1)
Player2.field.append(Evil_Tree_cub1)
Player2.hand.append(Evil_Lily2)
Player2.hand.append(Evil_Toxic_Guardshroom2)

   
def return_stats(player, minion):
    if minion in player.field:
        a = player.field.index(minion)
        health = player.field[a].health
        damage = player.field[a].damage
    return [damage, health]    

