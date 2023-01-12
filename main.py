from tkinter import *
import time
import random

class Tetris:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, width=480, height=640, bg="white")
        self.canvas.bind_all("<Key>", self.keyPressed)

        self.board = [] # to paint a game
        self.initBoard()

        self.showInterface()
    



    def showInterface(self):
        self.screem.title("Tetris By Loko")
        self.screem.geometry("480x640")
        self.canvas.place(x=0, y=0)
        self.paintBaord()
        self.screem.after(0, self.refreshScreem)
        self.screem.mainloop()


    def refreshScreem(self):
        self.paintBaord()
        self.screem.after(30, self.refreshScreem)

    def initBoard(self):
        self.board = []
        for i in range(0, 18):
            self.board.append([])
            for _ in range(0, 10):
                self.board[i].append(0)



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
                self.canvas.create_rectangle((x0+(countx*30)),(y0+(county*30)),(x0+((countx+1)*30)),(y0+((county+1)*30)), tag="board")
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