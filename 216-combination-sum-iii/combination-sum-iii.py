class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def f(k, n, temp, last):
            if k == 0 and n == 0:
                res.append(temp.copy())
                return
            if k < 0 or n < 0:
                return
            for i in range(last, 10):
                temp.append(i)
                f(k-1, n-i, temp, i+1)
                temp.pop()
        res = []
        f(k, n, [], 1)
        return res