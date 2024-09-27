import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.current_player = "X"   #to start the player with X
        self.board = [["","",""],["","",""],["","",""]]   #To initialize the board
        self.window = tk.Tk()  #we are initializing the window from tkinter
        self.window.title("Tic Tac Toe")   #Giving title name to window

        self.buttonsGrid = []  #To create a buttons because to play the game we have to enter something so we use buttons

        #To create cells and insert into window
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window,text="",width=20,height=10,command= lambda i=i, j=j: self.make_move(i,j))
                button.grid(row = i,column = j)
                row.append(button)
            self.buttonsGrid.append(row)


    def make_move(self,row,col):     #To mark the position
        if self.board[row][col]== "":     #This is used to wheather the cell is filled or not ,if it is not filled means we have to add x or o according to current player
            self.board[row][col]= self.current_player
            self.buttonsGrid[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Congratulations !!!","The game won by"+  self.current_player)
                self.window.quit()
            elif self.is_draw():
                messagebox.showinfo('Game is Draw sorry!!!') #massege showinfo(title,body)
                self.window.quit()
            self.current_player= "O" if self.current_player=="X" else "X"   # To change the current_player(alter)
    


    #To check win or lose
    def check_winner(self,player):
        for i in range(3):
            #Normally in a matrix we have 00,01,02...etc, To win the game [01,02,00],[10,11,12],[20,21,22] according to rows
            if player == self.board[i][0] == self.board[i][1] == self.board[i][2] :   
                return True
            if player == self.board[0][i] == self.board[1][i] == self.board[2][i] :    
                return True
            
        #For diagonals checking
        if player == self.board[0][0] == self.board[1][1] == self.board[2][2] :    
            return True
        if player == self.board[0][2] == self.board[1][1] == self.board[2][0] :    
            return True
        return False
    

    #To check a draw or not
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False   #If there is one empty return false which means board is not yet filled
            return True

        
   
    #To run code ..
    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()



        