import time
import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

class Player(NamedTuple):
    label: str     #O lub X
    colour: str     

class Move(NamedTuple):
    row: int
    col: int
    label: str = ""   #Pamieta znak danego gracza

BOARD_SIZE=3
DEFAULT_PLAYERS = (
    Player(label="X", colour="blue"),
    Player(label="O", colour="green"),
)
class TicTacToeGame:
    def __init__(self, player=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self._players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _get_winnig_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def _setup_board(self):
        self._current_moves = [
            [Move(row,col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winnig_combos()


class Board(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic-Tac-Toe")
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

        
    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display=tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()
    def _create_board_grid(self):
        grid_frame=tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )

def main():
    """Create the game's board and run its main loop."""
    board = Board()
    board.mainloop()

if __name__ == "__main__":
    main()


