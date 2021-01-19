from Board import SudokuPuzzle
from collections import defaultdict


class Solver:
    def __init__(self, puzzle: SudokuPuzzle):
        self.puzzle = puzzle
        self.invalid_options = defaultdict(set)

    def options(self, row: int, column: int) -> set:
        valid = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        valid -= self.puzzle.row(row)
        valid -= self.puzzle.column(column)
        valid -= self.puzzle.block(row, column)
        if (row, column) in self.invalid_options:
            valid -= self.invalid_options[(row, column)]
        return valid

    @property
    def all_options(self) -> dict:
        _all_options = {}
        for row, column in self.puzzle.open_cells():
            opts = self.options(row, column)
            _all_options[(row, column)] = opts
        return _all_options

    def simple_elimination(self, history: dict = {}) -> dict:
        if self.puzzle.complete():
            print("done")
            return history
        for (row, column), options in self.all_options.items():
            print(row, column, options)
            if len(options) == 1:
                self.puzzle[row, column] = options.pop()
                history[(row, column)] = self.puzzle[row, column]
                return self.simple_elimination(history)
        return history

    def undo_history(self, history: dict, is_invalid: bool = False):
        for (row, column), value in history.items():
            self.puzzle[row, column] = 0
            if is_invalid:
                self.invalid_options[(row, column)] = value

    def brute_solve(self):
        quick_his = self.simple_elimination()
        if self.puzzle.complete():
            return self


if __name__ == '__main__':
    test_puzzle = SudokuPuzzle([
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ])
    temp = Solver(test_puzzle)
    print(temp.options(1, 3))
    # print(temp.all_options)
    temp.simple_elimination()
    # print(temp.all_options)
    temp.puzzle.print_puzzle()
