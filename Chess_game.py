import pygame
import sys
from pygame.locals import *
from piece_maker import *
############## 각 칸의 위치 만들기 ######################
#배치 좌우 633이라 72..?씩 움직이면 된다. 
#배치 -5 ~ 500인데 500이 끝부분  70 씩 움직이자.
Board_place=[[(65,-5),(137,-5),(206,-5),(273,-5),(353,-5),(425,-5),(497,-5),(572,-5)],
             [(65,66),(137,66),(206,66),(273,66),(353,66),(425,66),(497,66),(572,66)],
             [(65,140),(137,140),(206,140),(273,140),(353,140),(425,140),(497,140),(572,140)],
             [(65,216),(137,216),(206,216),(273,216),(353,216),(425,216),(497,216),(572,216)],
             [(65,286),(137,286),(206,286),(273,286),(353,286),(425,286),(497,286),(572,286)],
             [(65,360),(137,360),(206,360),(273,360),(353,360),(425,360),(497,360),(572,360)],
             [(65,430),(137,430),(206,430),(273,430),(353,430),(425,430),(497,430),(572,430)],
             [(65,500),(137,500),(206,500),(273,500),(353,500),(425,500),(497,500),(572,500)]]
#########################초기화 작업###########################
pygame.init()
# 이 부분의 리스트에 전에 게임에서 만들었던 것 처럼 정보들을 딕셔너리로 담아야 할듯 합니다.
# 어떤 정보를 담아야 할까.
# 이렇게 두개 넣는다.
#1.기물 이름 P, L, N, B, K, Q등
#2.기물 위치

BPs=[]
WPs=[]
width = 633
height = 640
black = (0,0,0)
start_page = 0
game_font = pygame.font.Font(None,100)
msg_txt = "let's play chess!!"
running = True
pygame.display.set_caption("let's play chess!!")
main_display = pygame.display.set_mode((width,height),0,32) 
board = pygame.image.load("./Chess_Board.gif")
#gulimfont = pygame.font.SysFont('굴림',70)
#start_chess = gulimfont.render("let's play chess!!",1,black)
#hellorect = start_chess.get_rect()
#hellorect.center = (width/2,height/2)
WP = pygame.image.load("./peices/WP.gif")
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        if start_page == 0:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    start_page = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    start_page = 1
            pygame.display.update()
            continue
    if start_page == 0:
        main_display.fill((0,0,0))
        msg = game_font.render(msg_txt,True,(255,255,255))
        msg_rect = msg.get_rect(center = (int(width/2),int(height/2)))
        main_display.blit(msg,msg_rect)
    else:
        main_display.fill((255,255,255))
        main_display.blit(board,(0,0))
        #main_display.blit(WP,(572,-5))
        
        pos_init(Board_place,BPs,WPs, main_display)
    
    pygame.display.update()
#/Users/hanyoungwook/chess-engine/peices

            
