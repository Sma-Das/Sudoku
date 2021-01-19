

class Board(object):
    def __init__(self, puzzle: list[list]):
        self.puzzle = puzzle

    def print_puzzle(self):
        for row, row in enumerate(self.puzzle):
            if row % 3 == 0 and row != 0:
                line = "-"*6
                print(line+"+"+line+"-+"+line)
            for column, value in enumerate(row):
                if column % 3 == 0 and column != 0:
                    print("|", end=" ")
                if value == 0:
                    print(end="  ")
                else:
                    print(value, end=" ")
                if column == 8:
                    print()

    def complete(self):
        row_sum = 1+2+3+4+5+6+7+8+9
        for row in self.puzzle:
            if sum(row) != row_sum:
                return False
        return True

    def open_cells(self):
        for row in range(9):
            for column in range(9):
                if self.board[row][column] == 0:
                    yield row, column
