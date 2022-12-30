import pygame
import sys
from pygame.locals import *
pygame.init()

width = 633
height = 640
black = (0,0,0)
pygame.display.set_caption("let's play chess!!")
main_display = pygame.display.set_mode((width,height),0,32) 
board = pygame.image.load("./Chess_Board.gif")
gulimfont = pygame.font.SysFont('굴림',70)
start_chess = gulimfont.render("let's play chess!!",1,black)
hellorect = start_chess.get_rect()
hellorect.center = (width/2,height/2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_display.fill((255,255,255))
    main_display.blit(board,(0,0))
    pygame.display.update()
    
            
