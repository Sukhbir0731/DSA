class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        temp = [["."]*n for i in range(n)]
        posDiag = set() #(r+c)
        negDiag = set() #(r-c)
        col = set()
        res = []
        def f(r):
            if r == n:
                res.append(["".join(row) for row in temp])
                return
            for c in range(n):
                if (((r+c) in posDiag) or ((r-c) in negDiag) or (c in col)):
                    continue
                temp[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                f(r+1)
                temp[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
        f(0)
        return res

