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
    devotion_display = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (6*height)/11, width/4, height/11), 2)
    end_turn = pygame.draw.rect(DISPLAYSURF, YELLOW, ((3*width)/4, (5*height)/11, width/4, height/11))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, height/2), ((3*width)/4, height/2), 2)
    pygame.draw.line(DISPLAYSURF, GREY, (0, height/4), ((3*width)/4, height/4), 2)
    pygame.draw.line(DISPLAYSURF, GREY, (0, (3*height)/4), ((3*width)/4, (3*height)/4), 2)
    pygame.draw.line(DISPLAYSURF, BLACK, ((3*width)/4, 0), ((3*width)/4, height), 2)
    enemy_hero = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, 0, width/4, (4*height)/11), 2)
    player_hero = pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (7*height)/11, width/4, (4*height)/11), 2)
    pygame.draw.rect(DISPLAYSURF, BLACK, ((3*width)/4, (4*height)/11, width/4, height/11), 2)
    

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
attacker = None
defender = None
clicked = False
COUNTER = 0

    
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

def main():
    """Main game loop"""
    
    clicked =True
    COUNTER=0
    clicked_summon=True
    COUNTER_summon=0
    SUMMON_MINION=None
    gain_devotion = False
    display_screen() 
    
    while True:
        

                    
        if pygame.mouse.get_pressed()[0] == True:
            pos = pygame.mouse.get_pos()
            
            if field1.collidepoint(pos):
                """Select attacker if there isn't one or summon a minion if a card is selected"""

                if clicked_summon==False:
                    
                    if len(Player1.field) < 6:
                        playable = True
                        o = Player1.dev_val1
                        o2 = Player1.dev_val2
                        for i in SUMMON_MINION.devotion:
                            if i == Player1.devotion1:
                                x = 'dev_val1'
                            elif i == Player1.devotion2:
                                x = 'dev_val2'                                
                            z = getattr(Player1, x)
                            try:
                                y = getattr(SUMMON_MINION, i)
                            except:
                                continue
                            if z - y >= 0:
                                z = z - y
                                setattr(Player1, x, z)
                            else:
                                playable = False
                        if playable == True:
                            SUMMON_MINION.has_attacked = True 
                            Player1.field.append(SUMMON_MINION)
                            Player1.hand.remove(SUMMON_MINION)
                        else:
                            setattr(Player1, 'dev_val1', o)                            
                            setattr(Player1, 'dev_val2', o2)
                            print("You don't have enough devotion!")                             
                    else:
                        print("You can't summon 7 minions!")
                        
                    del list1[:]
                    del list2[:]
                    del hand_list[:]
                    del devotion_list[:]
                    COUNTER = 0
                    COUNTER_summon = 0
                    clicked_summon = True  
                    clicked = True
                    display_screen()
                    
                if clicked ==False and COUNTER==2:
                    COUNTER=0
                    clicked=True

                elif clicked ==False and COUNTER<2:
                    COUNTER+=1

                    
                if clicked==True:
                    for i in list1:
                            a = i[0]
                            b = i[1]
                            if a.get_rect(topleft = b).collidepoint(pos):
                                x = list1.index(i)
                                attacker = Player1.field[x]
                                print(attacker.name)
                                clicked=False
                                #print('friendly minion, name:', attacker.name+' damage: '+str(attacker.damage))
   
            elif enemy_hero.collidepoint(pos):
                if clicked == False:
                    if attacker.has_attacked == False:
                        Player2.health -= attacker.damage
                        attacker.has_attacked = True
                    else:
                        print("That minion can not attack!")
                        
                        del list1[:]
                        del list2[:]
                        del hand_list[:]
                        del devotion_list[:]
                        COUNTER = 0
                        COUNTER_summon = 0
                        clicked_summon = True
                        clicked = True
                        display_screen()

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
                            if clicked ==False:
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
                                if defender.health <= 0:
                                    Player2.field.remove(defender) 
                        else:
                            print("There's a taunt minion in the way!")

                        del list1[:]
                        del list2[:]
                        del hand_list[:]
                        del devotion_list[:]
                        COUNTER = 0
                        COUNTER_summon = 0
                        clicked_summon = True
                        clicked = True
                        display_screen()
                        
                        

            elif hand1.collidepoint(pos):
                """Select card from hand"""

                if clicked_summon==False and COUNTER_summon==2:
                    COUNTER_summon=0
                    clicked_summon=True
                  

                if clicked_summon==True and COUNTER_summon==0:
                    
                    for i in hand_list:
                        a = i[0]
                        b = i[1]
                        if a.get_rect(topleft = b).collidepoint(pos):
                            x = hand_list.index(i)
                            card = Player1.hand[x]
                            SUMMON_MINION=card
                            clicked_summon=False
                            print(card.name)

                if clicked==False and COUNTER_summon<2:
                    COUNTER_summon+=1

            elif devotion_display.collidepoint(pos):
                """Select which devotion to gain at the start of the turn"""

                if gain_devotion == False:

                    for i in devotion_list:
                        a = i[0]
                        b = i[1]                        
                        if a.get_rect(topleft = b).collidepoint(pos):
                            devt = devotion_list.index(i)
                            if devt == 0:
                                setattr(Player1, 'dev_val1', Player1.dev_val1 + 1)
                                setattr(Player1, 'dev_val_max1', Player1.dev_val_max1 + 1)
                            else:
                                setattr(Player1, 'dev_val2', Player1.dev_val2 + 1)
                                setattr(Player1, 'dev_val_max2', Player1.dev_val_max2 + 1)
                            del list1[:]
                            del list2[:]
                            del hand_list[:]
                            del devotion_list[:]
                            COUNTER = 0
                            COUNTER_summon = 0
                            clicked_summon = True
                            clicked = True
                            gain_devotion = True
                            display_screen()                    
                           
            while pygame.mouse.get_pressed()[0] == True:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        quit_everything()

                
            
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_everything()
              
            

main()


