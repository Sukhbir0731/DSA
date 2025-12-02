class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def f(r,c):
            if r == 9: # last box
                return True
            if c == 9: # call next row
                return f(r+1, 0)
            if board[r][c] != ".": # skip if already filled
                return f(r, c+1)
            # check for 1-9
            for num in range(1,10):
                s = str(num)
                if (s in row_set[r] or
                    s in col_set[c] or
                    s in box_set[r//3][c//3]):
                    continue
                board[r][c] = s
                row_set[r].add(s)
                col_set[c].add(s)
                box_set[r//3][c//3].add(s)
                if f(r, c+1):
                    return True
                # undo/ backtrack
                board[r][c] = "."
                row_set[r].remove(s)
                col_set[c].remove(s)
                box_set[r//3][c//3].remove(s)
            return False

        ROWS, COLS = 9,9
        row_set = [set() for i in range(9)]
        col_set = [set() for i in range(9)]
        box_set = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".":
                    continue
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                box_set[r//3][c//3].add(board[r][c])
        f(0,0)
        