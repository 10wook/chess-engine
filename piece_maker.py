import pygame
import sys
from pygame.locals import *


def pawn_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WP.gif")
    else:
        P = pygame.image.load("./BP.gif")
    board.blit(P,place)
    return P
def Luke_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WL.gif")
    else:
        P = pygame.image.load("./BL.gif")
    board.blit(P,place)
    return P
def Knight_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WN.gif")
    else:
        P = pygame.image.load("./BN.gif")
    board.blit(P,place)
    return P
def Queen_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WQ.gif")
    else:
        P = pygame.image.load("./BQ.gif")
    board.blit(P,place)
    return P
def King_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WK.gif")
    else:
        P = pygame.image.load("./BK.gif")
    board.blit(P,place)
    return P
def Bishop_maker(P,board,color,place):
    if color == 1:#하얀색이라는 뜻
        P = pygame.image.load("./WB.gif")
    else:
        P = pygame.image.load("./BB.gif")
    board.blit(P,place)
    return P

def pos_init():
    
                
    return