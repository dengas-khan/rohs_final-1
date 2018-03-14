import pygame
import tkinter
import sys
from pygame.locals import *


images                = ['fire.png', 'water.png', 'lightning.png', 'earth.png', 'wind.png']
ROOT                  = tkinter.Tk()
WIDTH                 = ROOT.winfo_screenwidth()
HEIGHT                = ROOT.winfo_screenheight() - 45  
DISPLAYSURF           = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
ROOT.withdraw()


def quit_everything():


    pygame.quit()
    sys.exit()

    
class Images(pygame.sprite.Sprite):
    """class for handling images"""


    def __init__(self, image_file, location):

        pygame.sprite.Sprite.__init__(self)
        self.image = image_file
        self.rect = self.image.get_rect()  #use this to get the image dimensions     
        self.rect.left, self.rect.top = location


def place_images_in_pentagon():


    image_list      = list()
    images          = ['fire.png', 'water.png', 'lightning.png', 'earth.png', 'wind.png']
    path            =  'graphics/'
    coordinate_list = [[                           ((WIDTH//2)-((WIDTH//25)//2)), (HEIGHT//7)],
                       [       ((WIDTH//4)-((WIDTH//25)//2)), ((HEIGHT//2)-((HEIGHT//13)//2))],
                       [          ((WIDTH//4)-((WIDTH//25)//2))+WIDTH//25, HEIGHT-(HEIGHT//7)],
                       [   WIDTH-(((WIDTH//4)-((WIDTH//25)//2))+WIDTH//25),HEIGHT-(HEIGHT//7)],
                       [WIDTH-((WIDTH//4)-((WIDTH//25)//2)), ((HEIGHT//2)-((HEIGHT//13)//2))]]
    
    for i in images:
        image       = pygame.image.load(path+i)
        image       = pygame.transform.scale(image, [WIDTH//12, HEIGHT//7])
        final_image = Images(image, [coordinate_list[images.index(i)][0],
                                     coordinate_list[images.index(i)][1]])

        DISPLAYSURF.blit(final_image.image, final_image.rect)
        image_list.append([final_image.rect, i])


    return image_list


def show_images_in_square(leave_out, nextBool):


    global images
    
    DISPLAYSURF.fill((255,255,255))
    object_list     = list()
    path            = 'graphics/'
    coordinate_list = [[             ((WIDTH//4)-((WIDTH//25)//2)), HEIGHT//4],
                       [       WIDTH-((WIDTH//4)-((WIDTH//25)//2)), HEIGHT//4],
                       [      ((WIDTH//4)-((WIDTH//25)//2)), HEIGHT-HEIGHT//4],
                       [WIDTH-((WIDTH//4)-((WIDTH//25)//2)), HEIGHT-HEIGHT//4]]

    if nextBool:
        images.remove(leave_out)
        
    
    for i in images:
        image       = pygame.image.load(path+i)
        image       = pygame.transform.scale(image, [WIDTH//12, HEIGHT//7])
        final_image = Images(image, [coordinate_list[images.index(i)][0],
                                     coordinate_list[images.index(i)][1]])
        DISPLAYSURF.blit(final_image.image, final_image.rect)
        object_list.append([final_image.rect, i])

    return object_list
                       
                       
def main():


    DISPLAYSURF.fill((255,255,255))
    NextBool                  = True   #don't change the picture if it is in the square
    elements_the_player_chose =  list()
    image_list = place_images_in_pentagon()
    while True:
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            
            for i in image_list:
                if i[0].collidepoint(pos):
                    image_list=show_images_in_square(i[1], NextBool)
                    NextBool=False
                    elements_the_player_chose.append(i[1][:-4]) #the [:-4] is to remove the '.png'
                    if len(elements_the_player_chose)==2:
                        return elements_the_player_chose[0]+','+elements_the_player_chose[1]

            while pygame.mouse.get_pressed()[0]:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        quit_everything()

    
        for event in pygame.event.get():
            if event.type==QUIT:
                quit_everything()
                
        pygame.display.update()
