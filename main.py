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



        self.board = [] # to paint a game 
        self.initBoard()
        self.miniBoard = [] # To Paint next piece
        self.initMiniBoard()
        self.player_score = 0

        


        self.showInterface()
    



    def showInterface(self):
        self.screem.title("Tetris By Loko")
        self.screem.geometry("480x640")
        self.canvas.place(x=0, y=0)
        self.paintBaord()
        self.lbl_player_score.place(x=360, y=80)
        self.canvas.create_image(360,500,image=self.logo, anchor=NW)
        self.screem.after(0, self.refreshScreem)
        self.screem.mainloop()


    def refreshScreem(self):
        self.paintBaord()
        self.updateScore()
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

    def updateScore(self):
        self.lbl_player_score['text'] = "HighScore:\n"+str(self.player_score)


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