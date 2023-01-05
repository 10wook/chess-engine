import pygame
import sys
from pygame.locals import *


#board는 체스 메인 화면 보드를 말한다.
#P는 peice뜻이고
#place는Board_place[0][0]이런식으로 주면 원하는 곳으로 줄 수 있다. 

def pawn_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WP.png")
    else:
        P = pygame.image.load("./peices/BP.png")
    board.blit(P,place)
    return P
def Luke_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WL.png")
    else:
        P = pygame.image.load("./peices/BL.png")
    board.blit(P,place)
    return P
def Knight_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WN.png")
    else:
        P = pygame.image.load("./peices/BN.png")
    board.blit(P,place)
    return P
def Queen_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WQ.png")
    else:
        P = pygame.image.load("./peices/BQ.png")
    board.blit(P,place)
    return P
def King_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WK.png")
    else:
        P = pygame.image.load("./peices/BK.png")
    board.blit(P,place)
    return P
def Bishop_maker(board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./peices/WB.png")
    else:
        P = pygame.image.load("./peices/BB.png")
    board.blit(P,place)
    return P

def pos_init(pos_list,BP,WP,board):
    ##양측 폰 생성
    for i in range(8):
        bp = pawn_maker(board,0,pos_list[1][i])
        wp = pawn_maker(board,1,pos_list[6][i])

        BP.append(bp)
        WP.append(wp)
    ##양측 룩 생성
    luke = Luke_maker(board,0,pos_list[0][0])
    BP.append(luke)
    luke = Luke_maker(board,0,pos_list[0][7])
    BP.append(luke)
    luke = Luke_maker(board,1,pos_list[7][0])
    WP.append(luke)
    luke = Luke_maker(board,1,pos_list[7][7])
    WP.append(luke)
    ##양측 나이트 생성
    Knight = Knight_maker(board,0,pos_list[0][1])
    BP.append(Knight)
    Knight = Knight_maker(board,0,pos_list[0][6])
    BP.append(Knight)
    Knight = Knight_maker(board,1,pos_list[7][1])
    WP.append(Knight)
    Knight = Knight_maker(board,1,pos_list[7][6])
    WP.append(Knight)
    
    #양측 비숍 생성
    Bishop = Bishop_maker(board,0,pos_list[0][2])
    BP.append(Bishop)
    Bishop = Bishop_maker(board,0,pos_list[0][5])
    BP.append(Bishop)
    Bishop = Bishop_maker(board,1,pos_list[7][2])
    WP.append(Bishop)
    Bishop = Bishop_maker(board,1,pos_list[7][5])
    WP.append(Bishop)
    
    #양측 퀸 생성
    Queen = Queen_maker(board,0,pos_list[0][3])
    BP.append(Queen)
    Queen = Queen_maker(board,1,pos_list[7][3])
    WP.append(Queen)
    #양측 킹 생성
    
    King = King_maker(board,0,pos_list[0][4])
    BP.append(King)
    King = King_maker(board,1,pos_list[7][4])
    WP.append(King)
    return