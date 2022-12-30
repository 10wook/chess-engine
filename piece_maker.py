import pygame
import sys
from pygame.locals import *


def pawn_maker(P,board,color,place):
    P = pygame.image.load("./WP.gif")
    board.blit(P,place)
    return P