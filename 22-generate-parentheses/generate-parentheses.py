class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(temp, left, right):
            if left==n and right==n:
                res.append(temp)
                return
            if left<n:
                f(temp+"(", left+1, right)
            if left>right:
                f(temp+")", left, right+1)
        res = []
        f("", 0,0)
        return res