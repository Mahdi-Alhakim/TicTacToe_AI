from tkinter import *
import tkinter.messagebox
import random
from src.ai_bot import XO_bot

class Game:
    def __init__(self, root, activateBot):
        self.root = root
        self.root.title("Tic-Tac-Toe")

        self.turn = 'X'
        self.board = [['' for _ in range(3)] for i in range(3)]
        self.GUIboard = []
        self.winLine = None
        self.GameOver = False
        self.moves = 0
        
        self.activateBot = activateBot

        if self.activateBot:
            self.bot = XO_bot(self)
        
        self.setup(self.root)

        self.root.mainloop()


    # Function to set up the initial GUI
    def setup(self, root):
        self.root.geometry("300x300")
        self.cnvs = Canvas(self.root, width=300, height=300, bg="gray")
        self.cnvs.pack()
        for _ in range(1, 3):
            self.cnvs.create_line(0, _*100, 300, _*100, fill="black")
            self.cnvs.create_line(_*100, 0, _*100, 300, fill="black")

        self.root.bind("<Button-1>", self.click)

    # Function to refresh the game state
    def refresh(self, winner='X'):
        self.board = [['' for _ in range(3)] for i in range(3)]
        self.updateBoard()

        self.turn = winner
        self.GUIboard = []
        self.winLine = None
        self.moves = 0
        self.GameOver = False
        if self.activateBot:
            global bot
            self.bot.makeMove(self.cnvs, self.board, self.turn)

    # Function to update the GUI board
    def updateBoard(self, WinLst=None):

        for _ in self.GUIboard:
            self.cnvs.delete(_)
        self.GUIboard = []
        if self.winLine:
            self.cnvs.delete(self.winLine)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.GUIboard += [self.cnvs.create_text(i*100+50, j*100+50, text=self.board[j][i], font="Times 50")]
        if WinLst:
            X1, Y1 =  WinLst[0][1]*100+50, WinLst[0][0]*100+50
            X2, Y2 =  WinLst[-1][1]*100+50, WinLst[-1][0]*100+50
            dX = X2 - X1
            dY = Y2 - Y1
            if not dX:
                Y1 -= 20
                Y2 += 20
            elif not dY:
                X1 -= 20
                X2 += 20
            elif Y1 < Y2:
                X1 -= 15
                Y1 -= 15
                X2 += 15
                Y2 += 15
            else:
                X1 -= 15
                Y1 += 15
                X2 += 15
                Y2 -= 15
            self.winLine = self.cnvs.create_line(X1, Y1, X2, Y2, fill="blue", width=4)

    # Function to check the game board for a winner
    def checkBoard(self, _brd):
        ii = True
        ii_2 = True
        for i in range(3):
            ij = True
            ji = True
            for j in range(1, 3):
                if _brd[i][j] != _brd[i][j-1] or _brd[i][j]=='' or _brd[i][j-1]=='':
                    ij = False
                if _brd[j][i] != _brd[j-1][i] or _brd[j][i] == '' or _brd[j-1][i] == '':
                    ji = False
            if ij:
                return _brd[i][0], [(i, j) for j in range(3)]
            elif ji:
                return _brd[0][i], [(j, i) for j in range(3)]
            if i > 0:
                if _brd[i][i] != _brd[i-1][i-1] or _brd[i][i] == '' or _brd[i-1][i-1] == '':
                    ii = False
            if i < 2:
                if _brd[1-i][i+1] != _brd[2-i][i] or _brd[1-i][i+1] == '' or _brd[2-i][i] == '':
                    ii_2 = False
        if ii:
            return _brd[0][0], [(i, i) for i in range(3)]
        if ii_2:
            return _brd[2][0], [(2-i, i) for i in range(3)]
        return None, None

    # Function to handle user clicks on the board
    def click(self, e):
        if self.GameOver:
            return
        if not(0<e.x<300 and 0<e.y<300):
            return
        clmn, row = e.x//100, e.y//100
        print(e.x, e.y)
        if self.board[row][clmn] == '':
            self.board[row][clmn] = self.turn
            self.moves += 1
            self.updateBoard()
            winner, lst = self.checkBoard(self.board)
            if winner:
                print("winner: " + winner)
                self.updateBoard(lst)
                tkinter.messagebox.showinfo("Winner", "Player ['{}'] is the WINNER!!".format(winner))
                self.GameOver = True
                self.root.after(1500, lambda : self.refresh(winner))
            elif self.moves == 9:
                tkinter.messagebox.showinfo("Tie", "IT IS A TIE!!")
                self.GameOver = True
                self.root.after(1500, self.refresh)

            print(self.board)
            self.nextTurn()

            if self.activateBot:
                self.bot.makeMove(self.cnvs, self.board, self.turn)

    # Function to switch to the next player's turn
    def nextTurn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
