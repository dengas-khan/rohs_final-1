"""this brings everything together"""


import pygame
import sys
import write_deck
import chose_which_devotion_for_deck
import deck_building
from pygame.locals import *



with open('all_decks.txt', 'a+') as myFile:
    myFile.write('\n'+
                 write_deck.main()+','
                 +chose_which_devotion_for_deck.main())
    #initially writes the deck name to the file (comma is there for split)
        
    myFile.close()

with open('all_decks.txt', 'r') as file2:
    print(file2.read())
