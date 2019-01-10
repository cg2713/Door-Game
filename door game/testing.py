import pygame
from pygame.locals import *
import random
import sys


#---------Start constants---------
fontName = pygame.font.match_font('Arial')
malfunction = random.randrange(1,11)
POWER_OUTPUT = 0.00
inventory = []
FRAME_RATE = 30
citySize = 0
BACKROUND_COLOR = (0,0,1)
YELLOW = (255,255,0)
WHITE = (255,255,255)
WIDTH = 1280
LENGTH = 720
BLACK = (0,0,0)

#generator = pygame.image.load("power generator1.jpg")



#---------end game function----------
#-------------load pic---------------
#generator = pygame.image.load("power generator1.jpg")


#def buyNewGenerator():
    #TODO
def boxes(color, cords1, cords2, size1, sizes2):
    pygame.draw.rect(window, color, [cords1,cords2,size1,sizes2])


window = pygame.display.set_mode([WIDTH,LENGTH])
window.fill(BACKROUND_COLOR)
window.fill(BLACK)









box1rect = pygame.Rect(100,10,250,100) #button placement
box1rect = pygame.Rect(550,600,250,100) #button placement
box_1 = pygame.draw.rect(window, YELLOW, box1rect) # these are the boxes i have placed
box_2 = pygame.draw.rect(window, YELLOW, [280,10,250,100])

box_3 = pygame.draw.rect(window, YELLOW, [550,10,250,100]) 
box_4 = pygame.draw.rect(window, YELLOW, [10,600,250,100]) 
box_5 = pygame.draw.rect(window, YELLOW, [280,600,250,100])
box1rect = pygame.Rect(100,10,250,100) #button placement

#texts('button', 30, WHITE, 100, 100)


box1rect = pygame.Rect(50,640,100,50)
box2rect = pygame.Rect(260,640,100,50)
box3rect = pygame.Rect(470,640,100,50)
box4rect = pygame.Rect(680,640,100,50)




clock = pygame.time.Clock()
pygame.display.update()
clock.tick(FRAME_RATE)



counter = 0

box2rect = pygame.Rect(0,0,0,0)
while True:

    for event in pygame.event.get():
            while True:
                box2 = boxes(WHITE,300,300,30,30)
                box2rect = pygame.Rect(300,300,30,30)
            if box2rect.collidepoint(event.pos):
                clearbox = boxes(BACKROUND_COLOR,300,300,30,30)
                clearbox = boxes(BLACK,300,300,30,30)
                print('second box was clicked')
                box2rect = pygame.Rect(0,0,0,0)
                window.blit(generator, (150, 250)) 
                window.blit(generator, (150, 250))
            
                
                

       
    
  

while True:
    #window.blit(generator, (150, 250)) 
    counter = counter + 1
    restartButton.draw()
    #texts('button', 60, WHITE, 100,10)
    #texts('button', 60, WHITE, 100,500)
    box_1 = pygame.draw.rect(window, YELLOW, [50,640,100,50])
    box_2 = pygame.draw.rect(window, YELLOW, [260,640,100,50])
    box_3 = pygame.draw.rect(window, YELLOW, [470,640,100,50])
    box_4 = pygame.draw.rect(window, YELLOW, [680,640,100,50])

    
    pygame.display.update()
    #window.blit(backgroundImage, (0, 0))
    clock.tick(FRAME_RATE)    
