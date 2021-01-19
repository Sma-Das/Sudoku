from Board import SudokuPuzzle


class Solver:
    def __init__(self, puzzle: SudokuPuzzle):
        self.puzzle = puzzle

    def options(self, row: int, column: int) -> set:
        valid = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
