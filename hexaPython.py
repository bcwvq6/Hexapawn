import copy
import numpy as np
import os
import time
from colorama import init
from termcolor import colored

init(convert=True)

def intro():
    print("""
    Welcome to,
     _   _                                           
    | | | |                                          
    | |_| | _____  ____ _ _ __   __ ___      ___ __  
    |  _  |/ _ \ \/ / _` | '_ \ / _` \ \ /\ / / '_ \ 
    | | | |  __/>  < (_| | |_) | (_| |\ V  V /| | | |
    \_| |_/\___/_/\_\__,_| .__/ \__,_| \_/\_/ |_| |_|
                         | |                         
                         |_|

    You may beat me at first, but I will always win in the end...

    The rules are simple
    Pawns can only move foward, and attack diagonally left or right.
    To win, you must do one of the following
    1. Get a pawn to the opposite side of the board
    2. Take out every opponent pawn
    3. Make your opponent unable to move

    Make your move:""")

## Keeps track of wins
compWins = 0
playerWins = 0

class game:
## The game board
    board = [['X','X','X'],
             ['O','O','O'],
             ['A','B','O']]
    
## Places pawns in their starting positions
    def fillBoard(self):
        players = ['A','B','C']
        for i in range(3):
            self.board[0][i] = 'X'
            self.board[1][i] = 'O'
            self.board[2][i] = players[i]
            
## Prints the current game board
    def drawBoard(self):
        print("\t---------")
        for i in range(3):
            print('\t', end='')
            for j in range(3):
                print('|', end='')
                if(self.board[i][j] == 'O'):
                    print(' ', end='')
                if(self.board[i][j] == 'X'):
                    print(colored(self.board[i][j], 'red'), end='')
                if(self.board[i][j] == 'A' or self.board[i][j] == 'B' or self.board[i][j] == 'C'):
                    print(colored(self.board[i][j], 'green'), end='')
                print('|', end='')
            print()
        print("\t---------")

## An object that holds the state of the game, and the possible moves        
class matchbox:
    boxIndex = 0
    gameState = ['a', 'b']
    moves = [0, 0, 0, 0]

    def __init__(self, Bnum, game, moves):
        self.boxIndex = Bnum
        self.gameState = game.copy()
        self.moves = moves

    def printState(self):
        print("---------")
        for i in range(3):
            for j in range(3):
                print('|', end=''), print(self.gameState[i][j], end=''), print('|', end='')
            print()
        print("---------")

## Tests if two matrices are equal
def isEqual(list1, list2):
    flag = True
    for i in range(3):
        for j in range(3):
            if(list1[i][j] == 'Y'):
                if(list2[i][j] != 'A' and list2[i][j] != 'B' and list2[i][j] != 'C'):
                    flag = False
            if(list1[i][j] == 'X'):
                if(list2[i][j] != 'X'):
                    flag = False
    return flag

## Determines if the game is won
def gameOver(game):
    Xcount = 0
    playerCount = 0
    for i in range(3):
        for j in range(3):
            if(game[i][j] == 'X'):
                Xcount = Xcount + 1
            if(game[i][j] == 'A' or game[i][j] == 'B' or game[i][j] == 'C'):
                playerCount = playerCount + 1
    if(Xcount == 0 or playerCount == 0):
        return True
    for i in range(3):
        if(game[2][i] == 'X' or (game[0][i] == 'A' or game[0][i] == 'B' or game[0][i] == 'C')):
            return True
    return False

class move:
    pos = [4, 4]
    num = 9
    def __init__(self, number, position):
        self.pos = position
        self.num = number
        
## Gives player all options and performs chosen move
def playerTurn(game, moveNum):
    moveNum = 0
    moveChoices = []
    choice = 0

    for i in range(3):
        for j in range(3):
            if(game[i][j] == 'A'):
                if(game[i-1][j] == 'O'):
                    moveNum += 1
                    print(repr(moveNum) + ". Move A foward")
                    move1 = move(1, [i, j])
                    moveChoices.append(move1.num)
                if(j-1>=0):
                    if(game[i-1][j-1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". A attack to the left")
                        move2 = move(2, [i, j])
                        moveChoices.append(move2.num)
                if(j+1<3):
                    if(game[i-1][j+1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". A attack to the right")
                        move3 = move(3, [i, j])
                        moveChoices.append(move3.num)

            if(game[i][j] == 'B'):
                if(game[i-1][j] == 'O'):
                    moveNum += 1
                    print(repr(moveNum) + ". Move B foward")
                    move4 = move(4, [i, j])
                    moveChoices.append(move4.num)
                if(j-1>=0):
                    if(game[i-1][j-1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". B attack to the left")
                        move5 = move(5, [i, j])
                        moveChoices.append(move5.num)
                if(j+1<3):
                    if(game[i-1][j+1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". B attack to the right")
                        move6 = move(6, [i, j])
                        moveChoices.append(move6.num)

            if(game[i][j] == 'C'):
                if(game[i-1][j] == 'O'):
                    moveNum += 1
                    print(repr(moveNum) + ". Move C foward")
                    move7 = move(7, [i, j])
                    moveChoices.append(move7.num)
                if(j-1>=0):
                    if(game[i-1][j-1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". C attack to the left")
                        move8 = move(8, [i, j])
                        moveChoices.append(move8.num)
                if(j+1<3):
                    if(game[i-1][j+1] == 'X'):
                        moveNum += 1
                        print(repr(moveNum) + ". C attack to the right")
                        move9 = move(9, [i, j])
                        moveChoices.append(move9.num)

    if(moveNum == 0):
        #g.drawBoard()
        print("You lost!")
        global haveLost
        haveLost = True
        global compWins
        compWins +=1
        
        
## Gets input from player
    if(haveLost == False):
        print("Input your choice:")
        while True:
            while True:
                choice = input()
                try:
                    choice = int(choice)
                    break
                except:
                    print("Choose one of the options.")
            if(choice <= moveNum):
                break
            else:
                print("Choose one of the options.")
        
## Performs players move
    if(haveLost == False):
        for i in range(5):
            if(choice == i):
                if(moveChoices[i-1] == 1):
                    game[move1.pos[0]-1][move1.pos[1]] = game[move1.pos[0]][move1.pos[1]]
                    game[move1.pos[0]][move1.pos[1]] = 'O'

                elif(moveChoices[i-1] == 2):
                    game[move2.pos[0]-1][move2.pos[1]-1] = game[move2.pos[0]][move2.pos[1]]
                    game[move2.pos[0]][move2.pos[1]] = 'O'

                elif(moveChoices[i-1] == 3):
                    game[move3.pos[0]-1][move3.pos[1]+1] = game[move3.pos[0]][move3.pos[1]]
                    game[move3.pos[0]][move3.pos[1]] = 'O'

                elif(moveChoices[i-1] == 4):
                    game[move4.pos[0]-1][move4.pos[1]] = game[move4.pos[0]][move4.pos[1]]
                    game[move4.pos[0]][move4.pos[1]] = 'O'

                elif(moveChoices[i-1] == 5):
                    game[move5.pos[0]-1][move5.pos[1]-1] = game[move5.pos[0]][move5.pos[1]]
                    game[move5.pos[0]][move5.pos[1]] = 'O'

                elif(moveChoices[i-1] == 6):
                    game[move6.pos[0]-1][move6.pos[1]+1] = game[move6.pos[0]][move6.pos[1]]
                    game[move6.pos[0]][move6.pos[1]] = 'O'

                elif(moveChoices[i-1] == 7):
                    game[move7.pos[0]-1][move7.pos[1]] = game[move7.pos[0]][move7.pos[1]]
                    game[move7.pos[0]][move7.pos[1]] = 'O'

                elif(moveChoices[i-1] == 8):
                    game[move8.pos[0]-1][move8.pos[1]-1] = game[move8.pos[0]][move8.pos[1]]
                    game[move8.pos[0]][move8.pos[1]] = 'O'

                elif(moveChoices[i-1] == 9):
                    game[move9.pos[0]-1][move9.pos[1]+1] = game[move9.pos[0]][move9.pos[1]]
                    game[move9.pos[0]][move9.pos[1]] = 'O'

## Holds the last move made by the computer
class lastMove:
    index = 0
    def __init__(self, num, matchBox):
        self.index = num
        self.box = matchBox

## Creating 'matchboxes' with potential moves
m1 = matchbox(0, [['X','X','X'],['Y','O','O'],['O','Y','Y']], [ [[0,1],[1,1]], [[0,1],[1,0]], [[0,2],[1,2]] ])
m2 = matchbox(1, [['X','X','X'],['O','Y','O'],['Y','O','Y']], [ [[0,0],[1,0]], [[0,0],[1,1]], [[0,2],[1,2]], [[0,2],[1,1]] ])
m3 = matchbox(2, [['O','X','X'],['X','Y','Y'],['Y','O','O']], [ [[0,1],[1,2]], [[0,2],[1,1]] ])
m4 = matchbox(3, [['O','X','X'],['O','X','Y'],['Y','O','O']], [ [[1,1],[2,1]], [[0,1],[1,2]], [[1,1],[2,0]] ])
m5 = matchbox(4, [['X','X','O'],['Y','O','Y'],['O','O','Y']], [ [[0,1],[1,0]], [[0,1],[1,1]] ])
m6 = matchbox(5, [['X','O','X'],['Y','O','O'],['O','O','Y']], [ [[0,2],[1,2]] ])
m7 = matchbox(6, [['X','X','O'],['Y','Y','X'],['O','O','Y']], [ [[0,0],[1,1]], [[0,1],[1,0]] ])
m8 = matchbox(7, [['X','O','X'],['Y','Y','O'],['O','Y','O']], [ [[0,0],[1,1]], [[0,2],[1,2]], [[0,2],[1,1]] ])
m9 = matchbox(8, [['O','X','X'],['Y','X','O'],['O','O','Y']], [ [[0,1],[1,0]], [[0,2],[1,2]] ])
m10 = matchbox(9, [['O','X','X'],['O','Y','O'],['O','O','Y']], [ [[0,2],[1,1]], [[0,2],[1,2]] ])
m11 = matchbox(10, [['X','O','X'],['X','Y','O'],['O','O','Y']], [ [[0,0],[1,1]], [[1,0],[2,0]], [[0,2],[1,1]], [[0,2],[1,2]] ])
m12 = matchbox(11, [['X','O','X'],['X','O','Y'],['O','Y','O']], [ [[1,0],[2,0]], [[1,0],[2,1]] ])
m13 = matchbox(12, [['O','X','X'],['O','Y','O'],['Y','O','O']], [ [[0,2],[1,2]], [[0,2],[1,1]] ])
m14 = matchbox(13, [['O','X','O'],['X','Y','Y'],['O','O','O']], [ [[0,1],[1,2]], [[1,0],[2,0]] ])
m15 = matchbox(14, [['X','O','O'],['X','Y','O'],['O','O','O']], [ [[0,0],[1,1]], [[1,0],[2,0]] ])
m16 = matchbox(15, [['X','O','O'],['X','X','Y'],['O','O','O']], [ [[1,0],[2,0]], [[1,1],[1,2]] ])
m17 = matchbox(16, [['X','O','O'],['Y','Y','Y'],['O','O','O']], [ [[0,0],[1,1]] ])
m18 = matchbox(17, [['O','O','X'],['Y','X','X'],['O','O','O']], [ [[1,1],[2,1]], [[1,2],[2,2]] ])
m19 = matchbox(18, [['O','X','O'],['Y','X','O'],['O','O','O']], [ [[0,1],[1,0]], [[1,1],[2,1]] ])
m20 = matchbox(19, [['O','O','X'],['X','Y','O'],['O','O','O']], [ [[0,2],[1,1]], [[0,2],[1,2]], [[1,0],[2,0]] ])
m21 = matchbox(20, [['O','O','X'],['O','Y','X'],['O','O','O']], [ [[0,2],[1,1]], [[1,2],[2,2]] ])
m22 = matchbox(21, [['O','X','O'],['Y','Y','X'],['O','O','O']], [ [[0,1],[1,0]], [[1,2],[2,2]] ])
m23 = matchbox(22, [['O','O','X'],['X','X','Y'],['O','O','O']], [ [[1,0],[2,0]], [[1,1],[2,1]] ])
m24 = matchbox(23, [['O','X','O'],['O','X','Y'],['O','O','O']], [ [[0,1],[1,2]], [[1,1],[2,1]] ])

## Mirrored matchbox cases
m25 = matchbox(24, [['X','X','X'],['O','O','Y'],['Y','Y','O']], [ [[0,1],[1,1]], [[0,1],[1,2]], [[0,0],[1,0]] ])
m26 = matchbox(25, [['X','X','X'],['O','Y','O'],['Y','O','Y']], [ [[0,0],[1,0]], [[0,0],[1,1]], [[0,2],[1,2]], [[0,2],[1,1]] ])
m27 = matchbox(26, [['X','X','O'],['Y','Y','X'],['O','O','Y']], [ [[0,1],[1,0]], [[0,0],[1,1]] ])
m28 = matchbox(27, [['X','X','O'],['Y','X','O'],['O','O','Y']], [ [[1,1],[2,1]], [[0,1],[1,0]], [[1,1],[2,2]] ])
m29 = matchbox(28, [['O','X','X'],['Y','O','Y'],['Y','O','O']], [ [[0,1],[1,2]], [[0,1],[1,1]] ])
m30 = matchbox(29, [['X','O','X'],['O','O','Y'],['Y','O','O']], [ [[0,0],[1,0]] ])
m31 = matchbox(30, [['O','X','X'],['X','Y','Y'],['Y','O','O']], [ [[0,2],[1,1]], [[0,1],[1,2]] ])
m32 = matchbox(31, [['X','O','X'],['O','Y','Y'],['O','Y','O']], [ [[0,2],[1,1]], [[0,0],[1,0]], [[0,0],[1,1]] ])
m33 = matchbox(32, [['X','X','O'],['O','X','Y'],['Y','O','O']], [ [[0,1],[1,2]], [[0,0],[1,0]] ])
m34 = matchbox(33, [['X','X','O'],['O','Y','O'],['Y','O','O']], [ [[0,0],[1,1]], [[0,0],[1,0]] ])
m35 = matchbox(34, [['X','O','X'],['O','Y','X'],['Y','O','O']], [ [[0,2],[1,1]], [[1,2],[2,2]], [[0,0],[1,1]], [[0,0],[1,0]] ])
m36 = matchbox(35, [['X','O','X'],['Y','O','X'],['O','Y','O']], [ [[1,2],[2,2]], [[1,2],[2,1]] ])
m37 = matchbox(36, [['X','X','O'],['O','Y','O'],['O','O','Y']], [ [[0,0],[1,0]], [[0,0],[1,1]] ])
m38 = matchbox(37, [['O','X','O'],['Y','Y','X'],['O','O','O']], [ [[0,1],[1,0]], [[1,2],[2,2]] ])
m39 = matchbox(38, [['O','O','X'],['O','Y','X'],['O','O','O']], [ [[0,2],[1,1]], [[1,2],[2,2]] ])
m40 = matchbox(39, [['O','O','X'],['Y','X','X'],['O','O','O']], [ [[1,2],[2,2]], [[1,1],[1,2]] ])
m41 = matchbox(40, [['O','O','X'],['Y','Y','Y'],['O','O','O']], [ [[0,2],[1,1]] ])
m42 = matchbox(41, [['X','O','O'],['X','X','Y'],['O','O','O']], [ [[1,1],[2,1]], [[1,0],[2,0]] ])
m43 = matchbox(42, [['O','X','O'],['O','X','Y'],['O','O','O']], [ [[0,1],[1,2]], [[1,1],[2,1]] ])
m44 = matchbox(43, [['X','O','O'],['O','Y','X'],['O','O','O']], [ [[0,0],[1,1]], [[0,0],[1,0]], [[1,2],[2,2]] ])
m45 = matchbox(44, [['X','O','O'],['X','Y','O'],['O','O','O']], [ [[0,0],[1,1]], [[1,0],[2,0]] ])
m46 = matchbox(45, [['O','X','O'],['X','Y','Y'],['O','O','O']], [ [[0,1],[1,2]], [[1,0],[2,0]] ])
m47 = matchbox(46, [['X','O','O'],['Y','X','X'],['O','O','O']], [ [[1,2],[2,2]], [[1,1],[2,1]] ])
m48 = matchbox(47, [['O','X','O'],['Y','X','O'],['O','O','O']], [ [[0,1],[1,0]], [[1,1],[2,1]] ])
boxes = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32,m33,m34,m35,m36,m37,m38,m39,m40,m41,m42,m43,m44,m45,m46,m47,m48]

again = True
intro()
## The game itself
while again:
    g = game()
    g.fillBoard()
    LM = lastMove(0, m1)
    while True:
        haveWon = False
        haveLost = False
        moveNum = 0
        g.drawBoard()
        playerTurn(g.board, moveNum)
        if(haveLost):
            break
        g.drawBoard()
        if(gameOver(g.board)):
            print("You won!")
            del boxes[LM.box.boxIndex].moves[LM.index]
            if(LM.box.boxIndex < 24):
                del boxes[(LM.box.boxIndex+24)].moves[LM.index]
            else:
                del boxes[(LM.box.boxIndex-24)].moves[LM.index]
            haveWon = True
            playerWins += 1
            break
            
        print("Computer's turn:")
        for i in range(len(boxes)):
            compMoved = False
            rand = np.random.randint(0, len(boxes[i].moves))
            if(isEqual(boxes[i].gameState, g.board)):
                think = [".","..","..."]
                for j in range(3):
                    print("Thinking"+think[j], end="\r")
                    time.sleep(0.8)
                os.system('cls')
                g.board[boxes[i].moves[rand][1][0]][boxes[i].moves[rand][1][1]] = g.board[boxes[i].moves[rand][0][0]][boxes[i].moves[rand][0][1]]
                g.board[boxes[i].moves[rand][0][0]][boxes[i].moves[rand][0][1]] = 'O'
                compMoved = True
            if(compMoved == False and i == 47):
                print("You won!")
                del boxes[LM.box.boxIndex].moves[LM.index]
                if(LM.box.boxIndex < 24):
                    del boxes[(LM.box.boxIndex+24)].moves[LM.index]
                else:
                    del boxes[(LM.box.boxIndex-24)].moves[LM.index]
                haveWon = True
                playerWins += 1
                break
            if(compMoved):
                LM = lastMove(rand, boxes[i])
                break
            
        if(gameOver(g.board)):
            g.drawBoard()
            print("You lost!")
            haveLost = True
            compWins +=1
            break
        if(haveWon or haveLost):
            break
    print("You have ", end=''), print(playerWins, end='')
    if(playerWins == 1):
        print(" win"+"\n"+"I have ", end='')
    else:
        print(" wins"+"\n"+"I have ", end='')
    print(compWins, end='')
    if(compWins == 1):
        print(" win")
    else:
        print(" wins")
        
    print("I'm getting better! Want to play again?(1 for yes, 0 for no): ")
    while True:
        while True:
            again = input()
            try:
                again = int(again)
                break
            except:
                print("Please choose 1 or 0.")
        if(again == 1):
            again = True
            os.system('cls')
            break
        if(again == 0):
            again = False
            break
        else:
            print("Please choose 1 or 0")
