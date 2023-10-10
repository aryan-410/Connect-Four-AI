import pygame
import math
import random
from copy import deepcopy

ROW_COUNT = 6
COLUMN_COUNT = 7

def findPossibleMoves(board):
    columnsTaken = []
    validMoves = []
    for x in reversed(range(len(board))):
        for y in range(len(board[0])):
            if board[x][y] == '--' and y not in columnsTaken:
                columnsTaken.append(y)
                validMoves.append((x, y))
    
    return validMoves

def simulateMove(board, move, piece):
    board[move[0]][move[1]] = piece
    return board

def isWon(board, piece):
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def evaluation(board):
    score = 0

    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == 'C' and board[r][c + 1] == 'C':
                score += 10
                if board[r][c + 2] == 'C' and board[c][c + 3] == '--': 
                    score += 500
    
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == 'C' and board[r + 1][c] == 'C':
                score += 10
                if board[r + 2][c] == 'C' and board[r + 3][c] == '--': 
                    score += 500
    
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == 'C' and board[r + 1][c + 1] == 'C':
                score += 10
                if board[r + 2][c + 2] == 'C' and board[r + 3][c + 3] == '--': 
                    score += 500
    
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == 'C' and board[r - 1][c + 1] == 'C':
                score += 10
                if board[r - 2][c + 2] == 'C' and board[r - 3][c + 3] == '--': 
                    score += 500
    
    return score

def ifBoardFull(board):
    full = True
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == '--': full = False
    
    return full

def minimax(board, depth , alpha, beta, maximizingPlayer):
    validMoves = findPossibleMoves(board)

    while validMoves != []:
        if depth == 0 or isWon(board, 'P') or isWon(board, 'C') or ifBoardFull(board):
            if isWon(board, 'P'):
                return (None, -10000000000000000000000000000000000)
            elif isWon(board, 'C'):
                return (None, 10000000000000000000000000000)
            else:
                return (None, evaluation(board))

        if maximizingPlayer:
            value = -math.inf
            column = random.choice(validMoves)
            for move in validMoves:
                bCopy = deepcopy(board)
                bCopy = simulateMove(bCopy, move, 'C')
                newScore = (minimax(bCopy, depth - 1, alpha, beta, False))[1]
                if newScore > value:
                    value = newScore
                    column = move
                alpha = max(alpha, value)       
                if alpha >= beta: 
                    break
            return (column, value)
        
        else:
            value = math.inf
            column = random.choice(validMoves)
            for move in validMoves:
                bCopy = deepcopy(board)
                bCopy = simulateMove(bCopy, move, 'P')
                newScore = (minimax(bCopy, depth - 1, alpha, beta, True))[1]
                if newScore < value:
                    value = newScore
                    column = move
                beta = min(beta, value)
                if beta <= alpha: 
                    break
            return (column, value)
