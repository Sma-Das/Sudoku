from Board import SudokuPuzzle


class Solver:
    def __init__(self, puzzle: SudokuPuzzle):
        self.puzzle = puzzle

    def options(self, row: int, column: int) -> set:
        valid = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        valid -= self.puzzle.row(row)
        valid -= self.puzzle.column(column)
        valid -= self.puzzle.block(row, column)
        return valid
