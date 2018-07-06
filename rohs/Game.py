import pygame, sys
from pygame.locals import *
import random, tkinter
import player
from battle import *
import collections


def quit_everything():
    """Function: close the programme after the user has finished using it"""
    pygame.quit()
    sys.exit()
    

"""Variables: determine the dimensions of the screen"""    
root = tkinter.Tk()
root.withdraw()
width = root.winfo_screenwidth()
height = root.winfo_screenheight() - 45

def draw_card(player):
    """Function: add cards to players' hands""" 
    x = random.choice(player.deck)
    player.deck.remove(x)
    player.hand.append(x)
    
def player_first():
    """****************random.choice(players)*****************************"""
    players = ('Player1', 'Player2') 
    x = 'Player1'
    if x == 'Player1':
        player_turn = True
        for i in range(3):
            draw_card(Player1)
        for i in range(4):
            draw_card(Player2)
    else:
        player_turn = False        
        for i in range(3):
            draw_card(Player2)
        for i in range(4):
            draw_card(Player1)

pygame.init()


"""Initiates the game and creates the interface"""
DISPLAYSURF = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game')


"""Variables: colours"""
Color = collections.namedtuple('Color', ['r','g','b'])  #can I marry collections.namedtuple? No- Jenga <3 
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
GREY = Color(192, 192, 192)
YELLOW = Color(242, 242, 73)
RED = Color(234, 71, 54)

def make_screen():
    """will make the board"""

    global field1
    global field2
    global hand1
    global enemy_hero
    global devotion_display
    global end_turn
    
    DISPLAYSURF.fill(WHITE)
    
    field1 = pygame.draw.rect(DISPLAYSURF, YELLOW, (0, height/2, (3*width)/4, height/4))
    field2 = pygame.draw.rect(DISPLAYSURF, RED, (0, height/4, (3*width)/4, height/4))
    hand1 = pygame.draw.rect(DISPLAYSURF, WHITE, (0, (3*height)/4, (3*width)/4, height/4))    
    end_turn = pygame.draw.rect(DISPLAYSURF, YELLOW, ((3*width)/4, (5*height)/11, width/4, height/11))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, height/2), ((3*width)/4, height/2), 2)
    pygame.draw.line(DISPLAYSURF, GREY, (0, height/4), ((3*width)/4, height/4), 2)
    pygame.draw.line(DISPLAYSURF, GREY, (0, (3*height)/4), ((3*width)/4, (3*height)/4), 2)
    pygame.draw.line(DISPLAYSURF, BLACK, ((3*width)/4, 0), ((3*width)/4, height), 2)
    enemy_hero = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, 0, width/4, (4*height)/11), 2)
    player_hero = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (7*height)/11, width/4, (4*height)/11), 2)
    pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (4*height)/11, width/4, height/11), 2)
    if gain_devotion == True:
        devotion_display = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (6*height)/11, width/4, height/11), 2)
    else:
        devotion_display = pygame.draw.rect(DISPLAYSURF, RED, ((3*width)/4, (6*height)/11, width/4, height/11))
    

"""Variable: Setting the font"""
FONT=pygame.font.Font('freesansbold.ttf', 40)


def make_end_turn_button():
    """will display the end turn button
       (must be called after make screeen"""

    button = FONT.render('End Turn', True, BLACK)
    DISPLAYSURF.blit(button, ((7*width)/8 - 90, height/2 - 18))
    pygame.display.update()


def display_devotion():
    """Displays current and max devotion"""

    dev1 = Player1.devotion1
    dev2 = Player1.devotion2    
    picture = pygame.image.load('graphics/' + str(dev1) + '.png')    
    picture = pygame.transform.scale(picture, (int(height/11 - 6), int(height/11 - 6)))
    DISPLAYSURF.blit(picture, (int((3*width)/4 + 3), int((6*height)/11 + 3)))
    tup = (picture, (int((3*width)/4 + 3), int((6*height)/11 + 3)))
    devotion_list.append(tup)
    picture = pygame.image.load('graphics/' + str(dev2) + '.png')    
    picture = pygame.transform.scale(picture, (int(height/11 - 6), int(height/11 - 6)))
    DISPLAYSURF.blit(picture, (int((7*width)/8 + 3), int((6*height)/11 + 3)))
    tup = (picture, (int((7*width)/8 + 3), int((6*height)/11 + 3)))
    devotion_list.append(tup)
    
    dev1 = FONT.render(str(Player1.dev_val1) + '/' + str(Player1.dev_val_max1), True, BLACK)
    DISPLAYSURF.blit(dev1, (int((3*width)/4 + int(height/11 - 6)), int((25*height)/44)))
    dev2 = FONT.render(str(Player1.dev_val2) + '/' + str(Player1.dev_val_max2), True, BLACK)
    DISPLAYSURF.blit(dev2, (int((7*width)/8 + int(height/11 - 6)), int((25*height)/44)))

    dev3 = Player2.devotion1
    dev4 = Player2.devotion2    
    picture = pygame.image.load('graphics/' + str(dev3) + '.png')    
    picture = pygame.transform.scale(picture, (int(height/11 - 6), int(height/11 - 6)))
    DISPLAYSURF.blit(picture, (int((3*width)/4 + 3), int((4*height)/11 + 3)))
    picture = pygame.image.load('graphics/' + str(dev4) + '.png')    
    picture = pygame.transform.scale(picture, (int(height/11 - 6), int(height/11 - 6)))
    DISPLAYSURF.blit(picture, (int((7*width)/8 + 3), int((4*height)/11 + 3)))

    dev3 = FONT.render(str(Player2.dev_val1) + '/' + str(Player2.dev_val_max1), True, BLACK)
    DISPLAYSURF.blit(dev3, (int((3*width)/4 + int(height/11 - 6)), int((25*height)/44 - (2*height)/11)))
    dev4 = FONT.render(str(Player2.dev_val2) + '/' + str(Player2.dev_val_max2), True, BLACK)
    DISPLAYSURF.blit(dev4, (int((7*width)/8 + int(height/11 - 6)), int((25*height)/44 - (2*height)/11)))
    pygame.display.update()


def display_hero():
    """Displays both heros' health"""
    pygame.draw.circle(DISPLAYSURF, RED, (width - 50, 50), 40)
    hea2 = FONT.render(str(Player2.health), True, WHITE)
    DISPLAYSURF.blit(hea2, (width - 72, 33))
    pygame.draw.circle(DISPLAYSURF, RED, (width - 50, height - 50), 40)
    hea1 = FONT.render(str(Player1.health), True, WHITE)
    DISPLAYSURF.blit(hea1, (width - 72, height - 66))
    pygame.display.update()
    
    
"""Variables: list(contains the minions in each players field)
   hand_list(contains the cards in player1s hand)
   devotion_list(contains which devotion player1 has)
   others(used for battle function)"""
list1 = list()
list2 = list()
hand_list = list()
devotion_list = list()
target_list = list()
    
def display_field(player):
    """will put the minions on the field"""

    x = 0
    hy = height/4 + 10
    h = height/4 - 20
    w = ((3*width)/4 - 10)/6 - 10
    hc = int(hy + (762*h)/1000)
    if player == Player1:
        hy += height/4
        hc += height/4  
    field_size = len(player.field)                          
        
    if field_size%2 == 0:
        start_display = int(3 - field_size/2)
    else:
        start_display = int(2.5 - field_size/2) 
    for i in range(start_display, start_display + len(player.field)):
        wx = 10+i*(((3*width)/4 - 10)/6)
        if field_size%2 != 0:
            wx += ((3*width)/4 - 10)/12
        wc = int(wx + (22*w)/238)
        wc2 = int(wx + (192*w)/238)
        minion = player.field[x]
        picture = pygame.image.load('graphics/' + str(minion.image))
        picture = pygame.transform.scale(picture, (int(w), int(h)))
        DISPLAYSURF.blit(picture, (int(wx), int(hy)))        
        x += 1
        tup = (picture, (wx, hy))
        
        if minion.taunt == True:
            picture = pygame.image.load('graphics/taunt.png')
            picture = pygame.transform.scale(picture, (int(w + 35), int(h + 55)))
            DISPLAYSURF.blit(picture, (int(wx - 17), int(hy - 27)))

        if minion.has_attacked == True:
            picture = pygame.image.load('graphics/dull.png')
            picture = pygame.transform.scale(picture, (int(w), int(h)))
            DISPLAYSURF.blit(picture, (int(wx), int(hy))) 
            
        if player == Player1:
            list1.append(tup)
        else:
            list2.append(tup)
            
        text1 = FONT.render(str(minion.damage), True, BLACK)
        text2 = FONT.render(str(minion.health), True, BLACK)
        DISPLAYSURF.blit(text1, (wc, hc))
        DISPLAYSURF.blit(text2, (wc2, hc))
    pygame.display.update()
       
    
def display_hand(player):
    """will display the hand"""

    hand_size = len(player.hand)
    x = 0
    if player == Player2:
        y = 10
    else:
        y = int((3*height)/4) + 10
            
    if hand_size%2 == 0:
        start_display = int(5 - hand_size/2)
    else:
        start_display = int(4.5 - hand_size/2)
            
    for i in range(start_display, start_display + len(player.hand)):
        wx = i*((3*width)/40)
        if hand_size%2 != 0:
            wx += (3*width)/80
        minion = player.hand[x]
        picture = pygame.image.load('graphics/' + str(minion.card))
        picture = pygame.transform.scale(picture, (int((3*width)/40), int(height/4 - 20)))
        DISPLAYSURF.blit(picture, (int(wx), y))
        x += 1
        tup = (picture, (wx, y))
        if player == Player1:
            hand_list.append(tup)
    pygame.display.update()

def display_screen():
    """displays everything on the screen"""


    make_screen()
    make_end_turn_button()
    display_hand(Player1)
    display_field(Player1)
    display_hand(Player2)
    display_field(Player2)
    display_devotion()
    display_hero()

def refresh():
    del list1[:]
    del list2[:]
    del hand_list[:]
    del devotion_list[:]
    display_screen()
    print('refreshed', select_attack)

def main():
    """Main game loop"""
    
    global gain_devotion
    global select_attack
       
    select_attack = False
    select_summon = False
    gain_devotion = False
    player_turn = True
    drawn_card = False
    SUMMON_MINION = None
    attacker = None
    defender = None
    display_screen()
    player_first()
        
    while True:
        
        if player_turn == False:
                draw_card(Player2)
                drawn_card = False
                player_turn = True
                for i in Player1.field:
                    setattr(i, 'has_attacked', False)
                gain_devotion = False    
                print('The enemy has ended their turn')
                display_screen()

        elif player_turn == True and drawn_card == False:
                draw_card(Player1)
                drawn_card = True
                display_screen()

           
                    
        if pygame.mouse.get_pressed()[0] == True and player_turn == True:
            pos = pygame.mouse.get_pos()


            if devotion_display.collidepoint(pos):
                """Select which devotion to gain at the start of the turn"""
                if gain_devotion == False:
                    for i in devotion_list:
                        a = i[0]
                        b = i[1]
                        if a.get_rect(topleft = b).collidepoint(pos):
                            devt = devotion_list.index(i)
                            if devt == 0:
                                setattr(Player1, 'dev_val_max1', Player1.dev_val_max1 + 1)
                                setattr(Player1, 'dev_val1', Player1.dev_val_max1)
                                setattr(Player1, 'dev_val2', Player1.dev_val_max2)
                            else:
                                setattr(Player1, 'dev_val_max2', Player1.dev_val_max2 + 1)
                                setattr(Player1, 'dev_val2', Player1.dev_val_max2)
                                setattr(Player1, 'dev_val1', Player1.dev_val_max1)
                            gain_devotion = True    
                            refresh()
                            
            if gain_devotion == True:                

                if field1.collidepoint(pos):
                    """Select attacker if there isn't one or summon a minion if a card is selected"""

                    if select_summon == True:
                    
                        if len(Player1.field) < 6:
                            playable = True
                            dev1 = Player1.dev_val1
                            dev2 = Player1.dev_val2
                            for i in SUMMON_MINION.devotion:
                                if i == Player1.devotion1:
                                    x = 'dev_val1'
                                elif i == Player1.devotion2:
                                    x = 'dev_val2'                                
                                player_devotion = getattr(Player1, x)                            
                                minion_cost = getattr(SUMMON_MINION, i)
                                if player_devotion - minion_cost >= 0:
                                    player_devotion = player_devotion - minion_cost
                                    setattr(Player1, x, player_devotion)
                                else:
                                    playable = False
                            if playable == True:
                                SUMMON_MINION.has_attacked = True
                                Player1.field.append(SUMMON_MINION)
                                Player1.hand.remove(SUMMON_MINION)
                                SUMMON_MINION.battlecry()
                                SUMMON_MINION = None
                                select_summon = False
                            else:
                                setattr(Player1, 'dev_val1', o)
                                setattr(Player1, 'dev_val2', o2)
                                print("You don't have enough devotion!")                        
                        else:
                            print("You can't summon 7 minions!")
                    
                    if select_attack == False:
                        for i in list1:
                            a = i[0]
                            b = i[1]
                            if a.get_rect(topleft = b).collidepoint(pos):
                                x = list1.index(i)
                                attacker = Player1.field[x]
                                print(attacker.name)
                                select_attack = True
                                #print('friendly minion, name:', attacker.name+' damage: '+str(attacker.damage))

                    elif select_attack == True:
                        select_attack = False
                        attacker = None
                        
                    refresh()
                   
                elif enemy_hero.collidepoint(pos):
                    taunt = False
                    if select_attack == True:
                        if attacker.has_attacked == False:
                            for i in Player2.field:
                                if getattr(i, 'taunt') == True:
                                    taunt = True
                            if taunt == False:
                                setattr(Player2, 'health', Player2.health - attacker.damage)
                                attacker.has_attacked = True
                            else:
                                print("There's a taunt minion in the way!")
                        else:
                            print("That minion can not attack!")
                            
                        select_attack = False
                        attacker = None
                        refresh()    

                elif field2.collidepoint(pos):
                    """Select battle target if attacker is selected"""
                    taunt = False
                    for i in list2:
                        a = i[0]
                        b = i[1]
                        if a.get_rect(topleft = b).collidepoint(pos):
                            x = list2.index(i)
                            defender = Player2.field[x]
                            print(defender.name)
                            for i in Player2.field:
                                if getattr(i, 'taunt') == True:
                                    taunt = True
                            if taunt == False or (taunt == True and getattr(defender, 'taunt') == True):
                                if getattr(defender, 'stealth') == False:
                                    if select_attack == True:
                                        if attacker.has_attacked == False:
                                            defender.health-=attacker.damage
                                            attacker.health-=defender.damage
                                            attacker.has_attacked = True
                                            attack_success = True
                                        elif attacker.has_attacked == True:
                                            print("This minion can not attack!")
                                            attack_success = False
                                        if getattr(attacker, 'poison') == True and attack_success == True:
                                            defender.health = 0
                                        if getattr(defender, 'poison') == True and attack_success == True:
                                            attacker.health = 0
                                        if attacker.health <= 0:
                                            Player1.field.remove(attacker)
                                            attacker.deathrattle()
                                        if defender.health <= 0:
                                            Player2.field.remove(defender)
                                            defender.deathrattle()
                                else:
                                    print('That minion has stealth!')
                            else:
                                print("There's a taunt minion in the way!")

                            select_attack = False
                            attacker = None
                            refresh()
                        
                        

                elif hand1.collidepoint(pos):
                    """Select card from hand"""

                    if select_summon==False:

                        for i in hand_list:
                            a = i[0]
                            b = i[1]
                            if a.get_rect(topleft = b).collidepoint(pos):
                                x = hand_list.index(i)
                                card = Player1.hand[x]
                                SUMMON_MINION=card
                                select_summon=True
                                print(card.name)

                    elif select_summon == True:

                        SUMMON_MINION = None
                        select_summon=False
                        

                        refresh()    

                elif end_turn.collidepoint(pos):
                    """End the player's turn"""

                    player_turn = False
                    refresh()
                    
            else:
                print('You need to select your devotion first!')
                                       
            while pygame.mouse.get_pressed()[0] == True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        quit_everything()
           
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_everything()
              
            

main()


