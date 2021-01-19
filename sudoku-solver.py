def print_puzzle(points):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("---"*7)
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")
            if (row, column) in points:
                print(points[(row, column)], end=" ")
            else:
                print(" ", end=" ")
        print()


def get_options(row, column, points):
    ''' given a row and column of a point in the puzzle, it will return the valid options for it'''
    valid_options = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    if (row, column) in points:
        return None
    for r, c in points:
        # OPTIMIZE: need to check every value in points
        block = r//3 == row//3 and c//3 == column//3
        if r == row or c == column or block:
            valid_options.discard(points[(r, c)])
    return valid_options


def remaining_empty(points):
    for row in range(9):
        for col in range(9):
            if (row, col) not in points:
                yield row, col


def shallow_update(points, **history):
    for row, column in remaining_empty(points):
        options = get_options(row, column, points)

        if len(options) == 1:
            value = options.pop()
            points[(row, column)] = value
            history[f"{row}, {column}"] = value
            return shallow_update(points, **history)

    return points, history


def all_options(points):
    options = {
        (row, column): get_options(row, column, points)
        for row, column in remaining_empty(points)
    }
    return options


def update_system(points):
    options = all_options(points)
    if len(points) == 81:
        return True
    for row, column in options:
        for value in options[(row, column)]:
            points[(row, column)] = value
            if update_system(points):
                return True
            else:
                del points[(row, column)]
        return False


if __name__ == '__main__':
    p3 = {
        (0, 1): 3, (2, 0): 7, (2, 2): 8,
        (3, 0): 3, (5, 1): 1,
        (6, 1): 2, (7, 1): 9, (7, 2): 6,
        (1, 3): 8, (2, 4): 5,
        (4, 4): 8, (5, 3): 4, (5, 5): 6,
        (6, 4): 1, (8, 4): 9, (8, 5): 5,
        (0, 8): 5, (1, 6): 4, (1, 8): 3,
        (3, 7): 9, (3, 8): 6, (4, 8): 4,
        (7, 6): 1, (8, 7): 7,
    }
    p = {
        'medium': {
            (0, 1): 9, (2, 1): 1, (2, 2): 6,
            (3, 0): 7, (5, 0): 1, (5, 2): 3,
            (6, 2): 8, (8, 2): 5,
            (2, 4): 5,
            (3, 3): 3, (3, 4): 4, (4, 3): 9,
            (6, 5): 1, (7, 5): 6, (8, 4): 2, (8, 5): 4,
            (0, 6): 3, (0, 8): 5, (1, 6): 8,
            (5, 8): 4,
            (6, 7): 6, (6, 8): 9, (7, 7): 4, (8, 7): 8,
        },
    }
    update_system(p3)
