# door game

#-----------imports-------------
import pygame
from pygwidgets import *
from pyghelpers import *
from pygame.locals import *
#-------window settings---------
WINDOW_LENGTH = 1280
WINDOW_HEIGHT = 720
FPS = 60

#-------window start------------
pygame.init()
window = pygame.display.set_mode([WINDOW_LENGTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

#--------colors----------
RED = (255,0,0)
ORANGE = (255,255,0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)                
BLACK = (0,0,0)
WHITE = (255,255,255)

#----------Image-----------
backGroundImage = pygame.image.load("map_1_door_game.jpg")
verticleClosed = pygame.image.load('closed_door_verticle.png')
verticleOpen = pygame.image.load('open_door_verticle.png')
#--------functions---------------



door1 = False
    









button1 = pygwidgets.TextButton(window, (460, 655), 'button')

inputTextB = pygwidgets.InputText(window, (20, 650), initialFocus=True,\
                                    textColor=(0, 0, 255),
                                    fontSize=28)

#--------loop--------------
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()  
            sys.exit()
        if button1.handleEvent(event):
            print("button clicked")
        if inputTextB.handleEvent(event):  # pressed Return or Enter
            theText = inputTextB.getValue()
            print('The text of inputTextB is: ' + theText)
            if theText == 'doorTesterInput':
                print('test')
            if theText == '2713 on':
                door1 = True
            elif theText == '2713 off':
                door1 = False
                
                

        
                




    
    window.blit(backGroundImage,(0,0))
    if door1 == True:
        window.blit(verticleClosed,(219,42))
    if door1 == False:
        window.blit(verticleOpen,(219,23))
    button1.draw()
    inputTextB.draw()
    #window.fill(BLACK)
    pygame.display.update()
    clock.tick(FPS)
