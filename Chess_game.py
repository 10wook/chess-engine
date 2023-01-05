import pygame
import sys
from pygame.locals import *
from piece_maker import *
############## 각 칸의 위치 만들기 ######################
#배치 좌우 633이라 72..?씩 움직이면 된다. 
#배치 -5 ~ 500인데 500이 끝부분  70 씩 움직이자.
Board_place=[[(70,-5),(142,-5),(214,-5),(286,-5),(358,-5),(430,-5),(502,-5),(577,-5)],
             [(70,66),(142,66),(214,66),(286,66),(358,66),(430,66),(502,66),(577,66)],
             [(70,140),(142,140),(214,140),(286,140),(358,140),(430,140),(502,140),(577,140)],
             [(70,216),(142,216),(214,216),(286,216),(358,216),(430,216),(502,216),(577,216)],
             [(70,286),(142,286),(214,286),(286,286),(358,286),(430,286),(502,286),(577,286)],
             [(70,360),(142,360),(214,360),(286,360),(358,360),(430,360),(502,360),(577,360)],
             [(70,430),(142,430),(214,430),(286,430),(358,430),(430,430),(502,430),(577,430)],
             [(70,500),(142,500),(214,500),(286,500),(358,500),(430,500),(502,500),(577,500)]]
#########################초기화 작업###########################
BPs=[]
WPs=[]
width = 633
height = 640
black = (0,0,0)

pygame.display.set_caption("let's play chess!!")
main_display = pygame.display.set_mode((width,height),0,32) 
board = pygame.image.load("./Chess_Board.gif")
#gulimfont = pygame.font.SysFont('굴림',70)
#start_chess = gulimfont.render("let's play chess!!",1,black)
#hellorect = start_chess.get_rect()
#hellorect.center = (width/2,height/2)
WP = pygame.image.load("./peices/WP.gif")
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    main_display.fill((255,255,255))
    main_display.blit(board,(0,0))
    #main_display.blit(WP,(577,-5))
    
    pos_init(Board_place,BPs,WPs, main_display)
    pygame.display.update()
#/Users/hanyoungwook/chess-engine/peices

            
