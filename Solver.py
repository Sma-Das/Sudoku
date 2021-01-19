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

    @property
    def all_options(self) -> dict:
        opts = {}
        for row, column in self.puzzle.open_cells():
            opts[(row, column)] = self.options(row, column)
        return opts

    def simple_elimination(self, history: dict = {}) -> dict:
        for row, column, options in self.all_options.items():
            if len(options) == 1:
                self.puzzle[row, column] = options.pop()
                history[(row, column)] = self.puzzle[row, column]
                return self.simple_elimination(history)
        return history
