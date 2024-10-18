from PySide2.QtWidgets import QApplication, QPushButton, QGridLayout, QVBoxLayout, QWidget, QMessageBox
from PySide2.QtCore import Qt
from functools import partial

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("XOX Oyunu")
        self.setFixedSize(400, 400)  # Pencere boyutu
        
        # Dış layout: İçeriği dikeyde hizalayacağız
        outer_layout = QVBoxLayout(self)
        
        # İç layout: Butonlar için grid düzeni
        self.grid_layout = QGridLayout()
        
        # İçeriği merkeze hizalamak için alignment ekliyoruz
        outer_layout.addLayout(self.grid_layout, alignment=Qt.AlignCenter)
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_board()
    
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(partial(self.on_click, row, col))
                
                self.grid_layout.addWidget(button, row, col)
                self.buttons[row][col] = button
    
    def on_click(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            
            if self.check_winner():
                self.show_winner_message(f"'{self.current_player}' kazandı!")
                self.reset_game()
            elif self.check_draw():
                self.show_winner_message("Oyun berabere!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        
        return False
    
    def check_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return True
    
    def show_winner_message(self, message):
        msg_box = QMessageBox(self)
        msg_box.setText(message)
        msg_box.exec_()
    
    def reset_game(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")

if __name__ == "__main__":
    app = QApplication([])
    
    window = TicTacToe()
    window.show()
    
    app.exec_()
