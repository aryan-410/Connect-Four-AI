import pygame
from circleClass import *
from connect4Ai import isWon

class Game:
    def __init__(self):
        self.move = True
        self.playerColor = (0, 128, 128)
        self.computerColor = (0, 64, 64)

        self.BASECOLOR = (255, 255, 255)

        self.rowColor = (127, 127, 127)
        self.listOfCircles = []
        self.soundToPlay = None

        self.playerCounter = 0
        self.board = [
            ['--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--'],
        ]
    
    def addMove(self, isComputer, computerPos):
        if not isComputer:
            self.color = 'P'
            for self.x in reversed(range(0, len(self.board))):
                self.posXInList = int(self.posX / 100)
                if self.board[self.x][(self.posXInList)] == '--':
                    self.board[self.x][(self.posXInList)] = self.color
                    break
            
        else:
            self.color = 'C'
            self.board[computerPos[0]][computerPos[1]] = self.color

        self.move = not self.move
    
    def updateBoard(self):
        for column in range(len(self.board)):
            for row in range(len(self.board[0])):
                if self.board[column][row] == '--': self.listOfCircles.append(Circle((100 * row) + 50, ((column * 100) + 50), self.BASECOLOR, 35, 0))
                elif self.board[column][row] == 'P': self.listOfCircles.append(Circle((100 * row) + 50, ((column * 100) + 50), self.playerColor, 35, 0))
                elif self.board[column][row] == 'C': self.listOfCircles.append(Circle((100 * row) + 50, ((column * 100) + 50), self.computerColor, 35, 0))\

    def whichRow(self, win):
        self.x, self.y = pygame.mouse.get_pos()

        self.posX = (self.x // 100) * 100

        rectangle = pygame.Rect(self.posX, 0, 100, 600)
        pygame.draw.rect(win, self.rowColor, rectangle)

    def winCheck(self):
        if isWon(self.board, 'P'):
            return (True,'P')
        
        if isWon(self.board, 'C'):
            return (True,'C')
        
        else:
            return(False, 'C')

    def update(self, win):
        self.whichRow(win)

        self.updateBoard()

        for circle in self.listOfCircles:
            circle.draw(win)
