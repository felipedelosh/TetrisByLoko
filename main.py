"""
FelipedelosH
2023

"""


from tkinter import *
from threading import Thread
import time
import random


class Tetris:
    def __init__(self) -> None:
        self.screem = Tk()
        self.canvas = Canvas(self.screem, width=480, height=640, bg="white")
        self.logo = PhotoImage(file="resources\img\logo.gif")
        self.canvas.bind_all("<Key>", self.keyPressed)
        self.lbl_main_message_start_game = Label(self.canvas, text="¡¡Press Any Key to start Game :) !!")
        self.lbl_game_over_message = Label(self.canvas, text="Game Over")
        self.lbl_player_score = Label(self.canvas, text="High Score")
        self.lbl_seed_game = Label(self.canvas, text="Speed")
        self.lbl_level_game = Label(self.canvas, text="Level")
        self.lbl_pieces_to_fallen = Label(self.canvas, text="Pieces:")

        #This is control game
        # 0: the game not run
        # 1: The game is run
        # 2: The Game is over
        self.mode_game = 0
        self.game_is_paused = False

        self.current_piece = []
        self.current_piece_pos_x = 3
        self.current_piece_pos_y = 0
        self.current_piece_rotation = 0
        self.list_of_complete_rows = []
        self.all_pieces = []
        self.initPieces()
        self.board = [] # to paint a game 
        self.board_h = 18
        self.board_w = 10
        self.initBoard()
        self.miniBoard = [] # To Paint next piece
        self.miniBoardCurrentPiece = []
        self.initMiniBoard()
        self.player_score = 0
        self.speed = 1
        self.level = 1
        self.pieces_to_fallen = 0
        
        self.thread = Thread(target=self.run)
        self.thread.start()

        self.showInterface()
    

    def showInterface(self):
        self.screem.title("Tetris By Loko")
        self.screem.geometry("480x640")
        self.canvas.place(x=0, y=0) 
        self.lbl_player_score.place(x=360, y=80)
        self.lbl_seed_game.place(x=340, y=320)
        self.lbl_level_game.place(x=420, y=320)
        self.lbl_pieces_to_fallen.place(x=380, y=380)
        self.canvas.create_image(350,500,image=self.logo, anchor=NW)
        self.screem.after(0, self.refreshScreem)
        self.screem.mainloop()


    def refreshScreem(self):
        self.paintBaord()
        self.paintMiniBoard()
        self.screem.after(60, self.refreshScreem)


    def initBoard(self):
        self.board = []
        for i in range(0, self.board_h):
            self.board.append([])
            for _ in range(0, self.board_w):
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
        p7b = [[1,0],[1,1],[0,1]]
        pieceG = [p7a, p7b]
        self.all_pieces.append(pieceG)

    def resetGame(self):
        self.speed = 1
        self.level = 1
        self.initBoard()


    def getNewRandomPiece(self):
        """
        Setting a new Random piece
        """
        self.current_piece_rotation = 0
        self.current_piece_pos_x = 4
        k = random.randint(0, len(self.all_pieces)-1)
        self.current_piece = self.all_pieces[k]
        self.pieces_to_fallen = self.pieces_to_fallen + 1
        
        
    
    def getPieceRotation(self):
        return self.current_piece_rotation


    def rotatePieceR(self):
        total_rotations = len(self.current_piece)
        #print("Rotando R...")
        if self.canRotate(total_rotations):
            self.current_piece_rotation = (self.current_piece_rotation + 1) %  total_rotations


    def canRotate(self, total_piece_rotations):
        """
        Protect to underflow
        """
        if total_piece_rotations > 0:
            next_rotate = self.current_piece[(self.current_piece_rotation + 1) % total_piece_rotations]
            part_of_matrix = []
            
            # Underflow 
            if next_rotate == [[1],[1],[1],[1]]:
                
                for i in range(0, 4):
                    part_of_matrix.append(self.board[self.current_piece_pos_y+i][self.current_piece_pos_x])

                if 2 in part_of_matrix:
                    return False

                return self.current_piece_pos_y + 3 < len(self.board)

            elif next_rotate == [1,1,1,1]:
                part_of_matrix = self.board[self.current_piece_pos_y][self.current_piece_pos_x:self.current_piece_pos_x+4]
                if 2 in part_of_matrix:
                    return False

                return self.current_piece_pos_x + 3 < len(self.board[0])
            else:
                len_piece_w = len(self.current_piece[self.getPieceRotation()][0])

                count_x = 0
                count_y = 0
                for i in next_rotate:
                    count_x = 0
                    for j in i:
                        if j != 0:
                            part_of_matrix.append(self.board[self.current_piece_pos_y+count_y][self.current_piece_pos_x+count_x])
                        count_x = count_x + 1
                    count_y = count_y + 1

                if 2 in part_of_matrix:
                    return False
    

                return self.current_piece_pos_x + len_piece_w < len(self.board[0])

        else:
            return False


    def rotatePieceL(self):
        pass

    def restartCurrentPiece(self):
        self.current_piece_pos_x = 4
        self.current_piece_pos_y = 0
        self.current_piece = []

    def existsCurrentPiece(self):
        return self.current_piece != []


    def putCurrentPieceInScreem(self):
        height_current_piece = len(self.current_piece[self.getPieceRotation()])
        
        if height_current_piece == 2 or height_current_piece == 3: 
            _x = self.current_piece_pos_x
            _y = self.current_piece_pos_y
            for i in self.current_piece[self.getPieceRotation()]:
                _x = self.current_piece_pos_x
                for j in i:
                    # Rule to not erase put pieces
                    if self.board[_y][_x] == 0:
                        self.board[_y][_x] = j
                    _x = _x + 1
                _y = _y + 1

        if height_current_piece == 4:
            if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
                _x = self.current_piece_pos_x
                _y = self.current_piece_pos_y
                for i in self.current_piece[self.getPieceRotation()]:
                    self.board[_y][_x] = 1
                    _x = _x + 1
            else:
                _x = self.current_piece_pos_x
                _y = self.current_piece_pos_y
                for i in self.current_piece[self.getPieceRotation()]:
                    self.board[_y][_x] = 1
                    _y = _y + 1


    def eraseCurrentPiece(self):
        count_x = 0
        count_y = 0
        # Put anothers cases
        for i in self.board:
            count_x = 0
            for j in i:
                if j == 1:
                    self.board[count_y][count_x] = 0
                count_x = count_x + 1 
            count_y = count_y + 1


    def applyGravity(self):
        if self.canMouveDown():
            self.current_piece_pos_y = self.current_piece_pos_y + 1


    def canMouveDown(self):
        if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
            return self.current_piece_pos_y + 1 <  len(self.board)
        else:
            len_pice = len(self.current_piece[self.getPieceRotation()])
            return self.current_piece_pos_y + len_pice < len(self.board)


    def theGameIsOver(self):
        # Need more logic
        part_of_matrix = self.board[1][3:6]


        return 2 in part_of_matrix

    def theRowIsComplete(self):
        for i in self.board:
            if 0 not in i:
                return True

        return False

    def _eraseCompleteRow(self):
        bonus_score = 0
        count_y = 0
        count_x = 0
        for i in self.board:
            count_x = 0
            if 0 not in i:
                bonus_score = bonus_score + 1
                self.list_of_complete_rows.append(count_y)
                for j in i:
                    self.board[count_y][count_x] = 0 
                    count_x = count_x + 1
            count_y = count_y + 1

        self.player_score = bonus_score * 100

    def _applyGravityToCompleteRows(self):
        tempBoard = []

        # Add new Zeros Rows
        for i in range(0, len(self.list_of_complete_rows)):
            tempBoard.append([])
            for _ in range(0, self.board_w):
                tempBoard[i].append(0)
        
        # Add previuos rows 
        counter = 0
        for _ in range(0, self.board_h):
            if counter not in self.list_of_complete_rows:
                tempBoard.append(self.board[counter])

            counter = counter + 1

        # Asing new Board
        self.board = tempBoard

        self.list_of_complete_rows = []

    def thePieceTouchFloor(self):
        # Put the case ****
        if self.existsCurrentPiece():
            len_pice = len(self.current_piece[self.getPieceRotation()])

            if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
                len_pice = 1
                return self.current_piece_pos_y + len_pice == len(self.board)

        
            return self.current_piece_pos_y + len_pice == len(self.board)
        else:
            return False


    def putThePieceInFloor(self):
        if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
            for i in range(0, 4):
                self.board[self.current_piece_pos_y][self.current_piece_pos_x+i] = 2
        elif self.current_piece[self.getPieceRotation()] == [[1],[1],[1],[1]]:
            for i in range(0, 4):
                self.board[self.current_piece_pos_y+i][self.current_piece_pos_x] = 2
        else:
            count_x = 0
            count_y = 0
            for i in self.current_piece[self.getPieceRotation()]:
                count_x = 0
                for j in i:
                    if j == 1:
                        self.board[self.current_piece_pos_y+count_y][self.current_piece_pos_x+count_x] = 2
                    count_x = count_x + 1
                count_y = count_y + 1
        

    def thePieceTouchAnotherPiece(self):
        """
        Return if the current piece be touch another piece in future (y+1)
        """
        if self.current_piece_pos_y+1 < len(self.board):
            current_ocupated_space = []
            if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
                current_ocupated_space = self.board[self.current_piece_pos_y+1][self.current_piece_pos_x:self.current_piece_pos_x+4]
                return 2 in current_ocupated_space
            elif self.current_piece[self.getPieceRotation()] == [[1],[1],[1],[1]]:
                for i in range(0, 4):
                    current_ocupated_space.append(self.board[self.current_piece_pos_y+i+1][self.current_piece_pos_x])
                return 2 in current_ocupated_space
            else:
                count_x = 0
                count_y = 0
                for i in self.current_piece[self.getPieceRotation()]:
                    count_x = 0
                    for j in i:
                        if j != 0:
                            current_ocupated_space.append(self.board[self.current_piece_pos_y+1+count_y][self.current_piece_pos_x+count_x])
                        count_x = count_x + 1
                    count_y = count_y + 1 
                        
                return 2 in current_ocupated_space

        return False



    def mouvePieceR(self):
        if self.canMouveR():
            self.current_piece_pos_x = self.current_piece_pos_x + 1


    def canMouveR(self):
        if self.existsCurrentPiece():
            part_of_matrix = []
            if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
                len_piece_w = 4

                if self.current_piece_pos_x+4 < len(self.board[0]):
                    if self.board[self.current_piece_pos_y][self.current_piece_pos_x+4] == 2:
                        return False
                    #return  self.board[self.current_piece_pos_y][self.current_piece_pos_x+4] != 2
            elif self.current_piece[self.getPieceRotation()] == [[1],[1],[1],[1]]:
                if self.current_piece_pos_x+1 < len(self.board[0]):
                    
                    for i in range(0, 4):
                        part_of_matrix.append(self.board[self.current_piece_pos_y+i][self.current_piece_pos_x+1])

                    if 2 in part_of_matrix:
                        return False

                    #return 2 not in part_of_matrix
                len_piece_w = len(self.current_piece[self.getPieceRotation()][0])
            else:
                len_piece_w = len(self.current_piece[self.getPieceRotation()][0])

                count_x = 1
                count_y = 0
                for i in self.current_piece[self.getPieceRotation()]:
                    count_x = 1
                    for j in i:
                        if j != 0 and self.current_piece_pos_x+count_x < len(self.board[0]):
                            part_of_matrix.append(self.board[self.current_piece_pos_y+count_y][self.current_piece_pos_x+count_x])
                        count_x = count_x + 1
                    count_y = count_y + 1

                if 2 in part_of_matrix:
                    return False

            return self.current_piece_pos_x + len_piece_w < len(self.board[0])
        else:
            return False


    def mouvePïeceL(self):
        if self.canMouvePieceL():
            self.current_piece_pos_x = self.current_piece_pos_x - 1


    def canMouvePieceL(self):
        if self.existsCurrentPiece():
            if self.current_piece[self.getPieceRotation()] == [1,1,1,1]:
                if self.current_piece_pos_x-1 > 0:
                    return self.board[self.current_piece_pos_y][self.current_piece_pos_x-1] != 2

            if self.current_piece[self.getPieceRotation()] == [[1],[1],[1],[1]]:
                if self.current_piece_pos_x-1 > 0:
                    part_of_matrix = []
                    for i in range(0, 4):
                        part_of_matrix.append(self.board[self.current_piece_pos_y+i][self.current_piece_pos_x-1])

                    return 2 not in part_of_matrix



            return self.current_piece_pos_x - 1 >= 0
        else:
            return False

    def updateUserStatitics(self):
        self.updateScore()
        self.updateLevel()
        self.updateSpeed()
        self.updatePiecesFallen()


    def updateScore(self):
        self.lbl_player_score['text'] = "HighScore:\n"+str(self.player_score)


    def updateLevel(self):
        self.lbl_level_game['text'] = "Level:\n"+str(self.level)


    def updateSpeed(self):
        self.lbl_seed_game['text'] = "Speed:\n"+str(self.speed)

    def updatePiecesFallen(self):
        self.lbl_pieces_to_fallen['text'] = "Pieces:\n"+str(self.pieces_to_fallen)


    def showInitalAnimation(self):
        self.lbl_main_message_start_game.place(x=80, y=300)
        time.sleep(0.2)
        self.lbl_main_message_start_game.place_forget()
        time.sleep(0.2)

    def showGameOverAnimation(self):
        self.lbl_game_over_message.place(x=120, y=300)
        time.sleep(0.2)
        self.lbl_game_over_message.place_forget()
        time.sleep(0.2)


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
                if j == 1 or j == [1]:
                    self.canvas.create_rectangle((x0+(countx*30)),(y0+(county*30)),(x0+((countx+1)*30)),(y0+((county+1)*30)), fill="black", tag="board")
                if j == 2:
                    self.canvas.create_rectangle((x0+(countx*30)),(y0+(county*30)),(x0+((countx+1)*30)),(y0+((county+1)*30)), fill="gray", tag="board")
                
                countx = countx + 1


    def paintMiniBoard(self):
        countx = 0
        county = 0
        self.initMiniBoard()
        self.canvas.delete("miniboard")
        self._insertMiniPieceInMiniBoard()
        for i in self.miniBoard:
            countx = 0
            county = county + 1
            for j in i:
                x0 = 360
                y0 = 200
                if j == 0:
                    self.canvas.create_rectangle((x0+(countx*15)),(y0+(county*15)),(x0+((countx+1)*15)),(y0+((county+1)*15)), fill="snow", tag="miniboard")
                else:
                    self.canvas.create_rectangle((x0+(countx*15)),(y0+(county*15)),(x0+((countx+1)*15)),(y0+((county+1)*15)), fill="black", tag="miniboard")
                countx = countx + 1


    def _insertMiniPieceInMiniBoard(self):
        len_piece = len(self.current_piece)
        if len_piece > 0:
            if self.current_piece[self.getPieceRotation()] == [1,1,1,1] or self.current_piece[self.getPieceRotation()] == [[1],[1],[1],[1]]:
                for i in range(0, 4):
                    self.miniBoard[0][i] = 1
            else:
                _x = 1
                _y = 0
                for i in self.current_piece[0]:
                    _x = 1
                    _y = _y + 1
                    for j in i:
                        self.miniBoard[_y][_x] = j
                        _x = _x + 1

    def _printTheBoard(self):
        for i in self.board:
            print(i)
        print("=============")



    def keyPressed(self, Event):
        if Event.keysym == "Up":
            print("Up")
        if Event.keysym == "Down":
            print("Down")
        if Event.keysym == "Right":
            if self.mode_game == 1:
                self.mouvePieceR()
        if Event.keysym == "Left":
            if self.mode_game == 1:
                self.mouvePïeceL()

        if Event.keysym == "space":
            if self.mode_game == 1:
                self.rotatePieceR()

        if Event.keysym == "r":
            self.restartCurrentPiece()
            self.getNewRandomPiece()

        if Event.keysym == "p":
            self.game_is_paused = not self.game_is_paused

        if self.mode_game == 0:
                self.mode_game = 1

        if self.mode_game == 2:
            self.resetGame()
            self.mode_game = 0



    def run(self):
        while True:
            if self.mode_game == 0:
                self.showInitalAnimation()

            if self.mode_game == 1 and not self.game_is_paused:
                # Game over
                if self.theGameIsOver():
                    self.mode_game = 2
                # complete row?
                if self.theRowIsComplete():
                    self._eraseCompleteRow()
                    self._applyGravityToCompleteRows()
                else:
                    # Get rnd piece if not use
                    if self.current_piece == []:
                        self.getNewRandomPiece()
                        self.updateUserStatitics()
                    # Put Pïece in Screem
                    self.putCurrentPieceInScreem()
                    time.sleep(0.25)
                    self.eraseCurrentPiece()
                    self.applyGravity()

                    if self.thePieceTouchFloor() or self.thePieceTouchAnotherPiece():
                        self.putThePieceInFloor()
                        self.restartCurrentPiece()

            if self.mode_game == 2:
                self.showGameOverAnimation()


            time.sleep(0.08)
            
            

t = Tetris()
