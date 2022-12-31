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
