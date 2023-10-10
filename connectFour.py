import pygame
from circleClass import *
from gameClass import *
from connect4Ai import *
import time

pygame.init()

WIDTH, HEIGHT = 700, 600

rowColor = (240, 0, 0)

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Connect 4')

# icon = pygame.image.load('Images/icon.png')6
# pygame.display.set_icon(icon)

g = Game()

def everyFrame():
    win.fill((170, 170, 170))
    g.update(win)
    pygame.display.flip()

if __name__ == '__main__':
    run = True
    while run:
        if not g.move:
            col, value = minimax(g.board, 6, -math.inf, math.inf, True)
            if col != None:
                g.addMove(True, col)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: g.addMove(False, 0)
        everyFrame()
