import pygame
import tkinter
import sys
from pygame.locals import *


ROOT                  = tkinter.Tk()
WIDTH                 = ROOT.winfo_screenwidth()
HEIGHT                = ROOT.winfo_screenheight() - 45
TEXTSIZE              = WIDTH//64
DISPLAYSURF           = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
ROOT.withdraw()


def quit_everything():
    """will quit the game"""
    
    pygame.quit()
    sys.exit()


#14 average length for each letter, 43 highest for the highest letter (h) at size of 30
#9 average length for each letter, 29 highest for the highest letter (h) at size of 20
#4 average length for each letter, 15 highest for the highest letter (h) at size of 10
"""this will go on going down by 5 lenght and 14 height for every ten 'size', this means that every 2 'size',
   the needed height for the highest letter goes up by one, and for every 1 'size', the length of every average letter
   goes up by 1.4
"""   
#10 should be the max length for deck names

#all the characters that the player is able to type
print(WIDTH)
print(HEIGHT)

def main():
    #all the characters that the player is able to type
    alphabet = 'abcdefghijklmnopqrstuvwxyz_-123456789 '
    DISPLAYSURF.fill((255,255,255))
    pygame.font.init()
    points = [WIDTH//9,200] #points[1] is used for nothing, but I can't be bothered to change it
    myFont = pygame.font.SysFont('Comic Sans MS', WIDTH//64)
    textsurface=myFont.render('hello', False, (0,0,0))
    has_typed_string = str()
    DISPLAYSURF.blit(myFont.render('please enter the name for your deck', False, (0,0,0)), [WIDTH//19,WIDTH//19])
    
    while True:
        
        for i in alphabet:
            
         #I do not break here, since the user may want to take away characters and add others
            mods = pygame.key.get_mods()

            
            if pygame.key.get_pressed()[ord(i)] and len(has_typed_string)<=11:
                if (mods & KMOD_LSHIFT) or (mods & KMOD_RSHIFT) or (mods & KMOD_CAPS):
                    print('here')
                    has_typed_string+=chr(ord(i)-32)
                else:
                    has_typed_string+=i
                DISPLAYSURF.fill((255,255,255))
                DISPLAYSURF.blit(myFont.render('please enter the name for your deck', False, (0,0,0)), [WIDTH//19,WIDTH//19])
                DISPLAYSURF.blit(myFont.render(has_typed_string, False, (0,0,0)), (points[0],200))
                

                
            elif pygame.key.get_pressed()[K_BACKSPACE]:
                    
                has_typed_string=has_typed_string[:-1] #delete the final character in he string
                DISPLAYSURF.fill((255,255,255))
                DISPLAYSURF.blit(myFont.render('please enter the name for your deck', False, (0,0,0)), [WIDTH//19,WIDTH//19])
                DISPLAYSURF.blit(myFont.render(has_typed_string, False, (0,0,0)), (points[0],200))

            elif pygame.key.get_pressed()[K_RETURN]:
                print(has_typed_string)
                return has_typed_string
            
            while pygame.key.get_pressed()[ord(i)] or pygame.key.get_pressed()[K_BACKSPACE]:    #make sure that only 1 key is registered
                for event in pygame.event.get():
                    if event.type==QUIT:
                        quit_everything()


        for event in pygame.event.get():
            if event.type==QUIT:
                quit_everything()
        

        pygame.display.update()
if __name__=='__main__':
    main()
