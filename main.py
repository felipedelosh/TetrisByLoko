"""
FelipedelosH
2023

"""

from tkinter import *
import time
import random

class Tetris:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, width=480, height=640, bg="white")
        self.logo = PhotoImage(file="resources\img\logo.gif")
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.lbl_player_score = Label(self.canvas, text="High Score")
        self.lbl_seed_game = Label(self.canvas, text="Speed")
        self.lbl_level_game = Label(self.canvas, text="Level")


        self.current_piece = []
        self.all_pieces = []
        self.board = [] # to paint a game 
        self.initBoard()
        self.miniBoard = [] # To Paint next piece
        self.initMiniBoard()
        self.player_score = 0
        self.speed = 1
        self.level = 1

        


        self.showInterface()
    



    def showInterface(self):
        self.screem.title("Tetris By Loko")
        self.screem.geometry("480x640")
        self.canvas.place(x=0, y=0)
        self.paintBaord()
        self.lbl_player_score.place(x=360, y=80)
        self.lbl_seed_game.place(x=340, y=320)
        self.lbl_level_game.place(x=420, y=320)
        self.canvas.create_image(350,500,image=self.logo, anchor=NW)
        self.screem.after(0, self.refreshScreem)
        self.screem.mainloop()


    def refreshScreem(self):
        self.paintBaord()
        self.paintMiniBoard()
        self.updateScore()
        self.updateLevel()
        self.updateSpeed()
        self.screem.after(30, self.refreshScreem)

    def initBoard(self):
        self.board = []
        for i in range(0, 18):
            self.board.append([])
            for _ in range(0, 10):
                self.board[i].append(0)

    def initMiniBoard(self):
        self.miniBoard = []
        for i in range(0, 4):
            self.miniBoard.append([])
            for _ in range(0, 4):
                self.miniBoard[i].append(0)

    def initPieces(self):
        """
        1111
        """
        p1a = [1,1,1,1]
        p1b = [[1],[1],[1],[1]]
        pieceA = [p1a, p1b]
        self.all_pieces.append(pieceA)

        p2a = [[1,0,0],[1,1,1]]
        p2b = [[1,1],[1,0],[1,0]]
        p2c = [[1,1,1],[0,0,1]]
        p2d = [[0,1],[0,1],[1,1]]
        pieceB = [p2a, p2b, p2c, p2d]
        self.all_pieces.append(pieceB)

        p3a = [[0,0,1],[1,1,1]]
        p3b = [[1,0],[1,0],[1,1]]
        p3c = [[1,1,1],[1,0,0]]
        p3d = [[1,1],[0,1],[0,1]]
        pieceC = [p3a, p3b, p3c, p3d]
        self.all_pieces.append(pieceC)

        p4a = [[1,1],[1,1]]
        pieceD = [p4a]
        self.all_pieces.append(pieceD)

        p5a = [[0,1,1],[1,1,0]]
        p5b = [[1,0],[1,1],[0,1]]
        pieceE = [p5a, p5b]
        self.all_pieces.append(pieceE)

        p6a = [[0,1,0],[1,1,1]]
        p6b = [[1,0],[1,1],[1,0]]
        p6c = [[1,1,1],[0,1,0]]
        p6d = [[0,1],[1,1],[0,1]]
        pieceF = [p6a, p6b, p6c, p6d]
        self.all_pieces.append(pieceF)

        p7a = [[1,1,0],[0,1,1]]
        p7b = [[1,0],[1,1],[1,0]]
        pieceG = [p7a, p7b]
        self.all_pieces.append(pieceG)




    def updateScore(self):
        self.lbl_player_score['text'] = "HighScore:\n"+str(self.player_score)

    def updateLevel(self):
        self.lbl_level_game['text'] = "Level:\n"+str(self.level)

    def updateSpeed(self):
        self.lbl_seed_game['text'] = "Speed:\n"+str(self.speed)


    def paintBaord(self):
        countx = 0
        county = -1
        self.canvas.delete("board")
        for i in self.board:
            countx = 0
            county = county + 1
            for j in i:
                x0 = 20
                y0 = 50
                if j == 0:
                    self.canvas.create_rectangle((x0+(countx*30)),(y0+(county*30)),(x0+((countx+1)*30)),(y0+((county+1)*30)), fill="snow", tag="board")
                else:
                    self.canvas.create_rectangle((x0+(countx*30)),(y0+(county*30)),(x0+((countx+1)*30)),(y0+((county+1)*30)), fill="black", tag="board")
                countx = countx + 1

    def paintMiniBoard(self):
        countx = 0
        county = 0
        self.canvas.delete("miniboard")
        for i in self.miniBoard:
            countx = 0
            county = county + 1
            for j in i:
                x0 = 360
                y0 = 200
                self.canvas.create_rectangle((x0+(countx*15)),(y0+(county*15)),(x0+((countx+1)*15)),(y0+((county+1)*15)), fill="snow", tag="miniboard")
                countx = countx + 1
                

    def keyPressed(self, Event):
        if Event.keysym == "Up":
            print("Up")
        if Event.keysym == "Down":
            pass
        if Event.keysym == "Right":
            pass
        if Event.keysym == "Left":
            pass

        if Event.keysym == "space":
            print("Space")

        print(Event.keysym)

t = Tetris()