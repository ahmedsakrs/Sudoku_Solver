def validate(board: list[list[str]]) -> bool:
    """
    Checks if the entry puzzle is a valid Sudoku puzzle. A valid Sudoku does not imply a solution existence.\n
    :param board: The state of the puzzle.
    :return: True if the board is valid. False otherwise.
    """
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            if board[i][j].isdigit():
                row.append(board[i][j])
            if board[j][i].isdigit():
                col.append(board[j][i])
        if len(row) != len(set(row)) or len(col) != len(set(col)):
            return False

    for r in [0, 3, 6]:
        for c in [0, 3, 6]:
            square = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if board[i][j].isdigit():
                        square.append(board[i][j])
            if len(square) != len(set(square)):
                return False
    return True
