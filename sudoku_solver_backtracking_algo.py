def sudoku(puzzle):
    def is_pos_invalid(pos, num, bo):

        # Check grid
        row = pos[0]
        col = pos[1]

        for i in range(len(bo)):
            if bo[i][col] == num:  # if same number n on column
                return True
            if bo[row][i] == num:  # if same number n on row
                return True

        # Check box
        box_row = row // 3
        box_col = col // 3

        for i in range(box_row * 3, box_row * 3 + 3):
            for j in range(box_col * 3, box_col * 3 + 3):
                if bo[i][j] == num and (i, j) != (row, col):
                    return True
        return False

    def find_empty(bo):
        for row in range(len(bo)):
            for col in range(len(bo)):
                if bo[row][col] == 0:
                    return (row, col)
        return False

    def solve(bo):
        find = find_empty(bo)
        if not find:
            return True
        else:
            (row, col) = find

        for i in range(1, 10):
            if not is_pos_invalid(find, i, bo):
                bo[row][col] = i

                if solve(bo):
                    return True

                bo[row][col] = 0

        return False

    solve(puzzle)

    return puzzle