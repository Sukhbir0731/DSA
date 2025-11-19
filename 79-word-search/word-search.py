class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def f(curr, r, c):
            if curr == len(word):
                return True
            if (r<0 or r>=ROWS or
                c<0 or c>=COLS or
                (r,c) in seen or
                board[r][c] != word[curr]):
                return False
            seen.add((r,c))
            res = (f(curr+1, r+1, c) or
                    f(curr+1, r-1, c) or
                    f(curr+1, r, c-1) or
                    f(curr+1, r, c+1))
            seen.remove((r,c))
            return res

        seen = set()
        ROWS, COLS = len(board), len(board[0])
        for r in range(0, ROWS):
            for c in range(0, COLS):
                if f(0, r, c):
                    return True
        return False