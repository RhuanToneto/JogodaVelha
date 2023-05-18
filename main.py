import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.turn_label = tk.Label(master, text=f"{self.current_player} é a sua vez :", font=("Arial", 16))
        self.turn_label.grid(row=0, column=0, columnspan=3)

        self.buttons = [[tk.Button(master, text="", font=("Arial", 60), width=3, height=1, command=lambda row=row, col=col: self.click(row, col)) for col in range(3)] for row in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].grid(row=row+1, column=col)

        tk.Button(master, text="Reiniciar", font=("Arial", 16), command=self.restart).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(master, text="Sair", font=("Arial", 16), command=master.destroy).grid(row=4, column=2, columnspan=2, pady=10)

    def click(self, row, col):
        if self.board[row][col] == "":
            self.buttons[row][col].config(text=self.current_player)
            self.board[row][col] = self.current_player
            if self.check_win():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.current_player} venceu!")
                self.restart()
            elif self.check_tie():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.restart()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.turn_label.config(text=f"{self.current_player} é a sua vez")

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def restart(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.turn_label.config(text=f"{self.current_player} é a sua vez")

root = tk.Tk()
app = TicTacToe(root)
root.mainloop()
