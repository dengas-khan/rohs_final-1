from minions import minion
import pygame
import tkinter
import sys
import weakref
from pygame.locals import *

#tkinter is used to get the screen size (win32api is not universal
#hiehgt and width will have the same dimensions as 
ROOT                  = tkinter.Tk()
WIDTH                 = ROOT.winfo_screenwidth()
HEIGHT                = ROOT.winfo_screenheight() - 45  
DISPLAYSURF           = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
STARTLOOP             = int()
LINE_LIMIT            = 9
PAGE_LIMIT            = 18
HOW_MUCH_TO_TAKE_AWAY = 18
HOW_MUCH_TO_ADD       = 0

ROOT.withdraw()




def quit_everything():
    pygame.quit()
    sys.exit()


def get_all_instances_of_minions():
    """will return a list of all the instances of the
       minion class"""


    return minion.instances



class images(pygame.sprite.Sprite):
    """class for handling images"""

    
    alive = []
    def __init__(self, image_file, location):

        pygame.sprite.Sprite.__init__(self)
        self.image = image_file
        self.rect = self.image.get_rect()  #use this to get the image dimensions     
        self.rect.left, self.rect.top = location

def make_button_finish():
    """will make the 'finish making deck' button"""


    image   = pygame.image.load('graphics/finish_making_deck_button.png')
    image   = pygame.transform.scale(image, [WIDTH//6,HEIGHT//6])
    the_rect= images(image, [(WIDTH//2)-(WIDTH//12), (HEIGHT//2)+(HEIGHT//5)])
    DISPLAYSURF.blit(the_rect.image, the_rect.rect)

    return the_rect

def make_button_next():
    """will make the next page button."""


    image          = pygame.image.load('graphics/next_turn_button.png')
    image          = pygame.transform.scale(image, [WIDTH//6,HEIGHT//6])
    next_turn_rect = images(image, [(WIDTH-(WIDTH//6)), (HEIGHT//2+HEIGHT//5)])
    DISPLAYSURF.blit(next_turn_rect.image, next_turn_rect.rect)

    return next_turn_rect


def make_button_last():
    image          = pygame.image.load('graphics/last_page_button.png')
    image          = pygame.transform.scale(image , [WIDTH//6,HEIGHT//6])
    last_turn_rect = images(image, [0, (HEIGHT//2+HEIGHT//5)])
    DISPLAYSURF.blit(last_turn_rect.image, last_turn_rect.rect)

    return last_turn_rect

def show_all_minion_pictures(devotions : list):
    """willuse the minion instances list to make all
       their pictures"""

    ALL_OBJECTS      = list()
    list1            = list()
    list2            = list()
    UP_TO            = (WIDTH//((WIDTH//10)))-1
    POSITION_LIST    = [0,WIDTH//(256//4)]
    for i in range(STARTLOOP,STARTLOOP+PAGE_LIMIT):
        try:
            get_all_instances_of_minions()[i]
        except IndexError:
            return ALL_OBJECTS,list2        #remember this this is normally the actual return function

        #comment thisout for testing the feature that makes the pictures into different lists
        if get_all_instances_of_minions()[i].name in list1:
            continue
        elif (get_all_instances_of_minions()[i].devotion[0] not in devotions) and (get_all_instances_of_minions()[i].devotion[1] not in devotions):
            continue
                        
        else:
            list2.append(get_all_instances_of_minions()[i].name)
            print(list2)

        POSITION_LIST[0]       +=(WIDTH//10)+(WIDTH//256)
        if i==LINE_LIMIT:
            POSITION_LIST[1]   +=(HEIGHT//4)+(WIDTH//256)
            POSITION_LIST[0]    =(WIDTH//10)+(WIDTH//256)
        image                   = pygame.image.load('graphics/'+get_all_instances_of_minions()[i].card)
        image                   = pygame.transform.scale(image, (WIDTH//10, HEIGHT//4))
        picture                 = images(image, (POSITION_LIST[0], POSITION_LIST[1]))
        
        DISPLAYSURF.blit(picture.image, (picture.rect))
        list1.append(get_all_instances_of_minions()[i].name)
        ALL_OBJECTS.append([picture, get_all_instances_of_minions()[i]])


    return ALL_OBJECTS, list2


def decide_to_block_out_previous_turn(n,rect):
    """if n, which is startloop, is 0, end turn will be blocked out by
       a white rectangle"""
    global HOW_MUCH_TO_TAKE_AWAY
    
    if n==0:
        HOW_MUCH_TO_TAKE_AWAY=0
        pygame.draw.rect(DISPLAYSURF, (255,255,255), rect)
    else:
        HOW_MUCH_TO_TAKE_AWAY=18
        return make_button_last()


def decide_to_block_out_next_page(nonduplist, rect,n):
    """if startloop is bigger than the length of the nonduplicate list,
       then it will block out the next turn button."""

    global HOW_MUCH_TO_ADD
    
    
    if n+18>len(nonduplist):
        HOW_MUCH_TO_ADD=0
        pygame.draw.rect(DISPLAYSURF, (255,255,255), rect)

    else:
        HOW_MUCH_TO_ADD=18
        
        

def main():
    
    global STARTLOOP
    DISPLAYSURF.fill((255,255,255))
    all_picture_objects, list_of_nondupilicates = show_all_minion_pictures(['earth'
                                                                            ,None])
    next_page_button                            = make_button_next()
    last_page_button                            = make_button_last()
    finish_making_deck_button                   = make_button_finish()
    string_of_cards                             = ''
    pygame.display.update()
    while True:
    
        decide_to_block_out_next_page(list_of_nondupilicates, next_page_button.rect, STARTLOOP)
        decide_to_block_out_previous_turn(STARTLOOP, last_page_button.rect)
        #detect what minion the playter has pressed (if they have clicked the mouse)
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            
            if next_page_button.rect.collidepoint(pos):
                STARTLOOP+=HOW_MUCH_TO_ADD
                all_picture_objects=show_all_minion_pictures(['earth',None])

            elif last_page_button.rect.collidepoint(pos):
                STARTLOOP-=HOW_MUCH_TO_TAKE_AWAY
                all_picture_objects=show_all_minion_pictures(['earth',None])

            elif finish_making_deck_button.rect.collidepoint(pos):
                print('the player wants to finish making their deck')
            for i in all_picture_objects:
                if i[0].rect.collidepoint(pos):
                    print(i[1].name) #i[0] is the sprite object, i[1] is the minion object

                    
            while pygame.mouse.get_pressed()[0]:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        quit_everything()


        for event in pygame.event.get():
            if event.type==QUIT:
                quit_everything()
        pygame.display.update()

if __name__=='__main__':
    main()
