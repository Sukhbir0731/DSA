class Solution:
    def climbStairs(self, n: int) -> int:
        def f(n):
            if n<=2:
                return n
            if dp[n] != 0:
                return dp[n]
            dp[n] = f(n-1) + f(n-2)
            return dp[n]
        dp = [0]*(n+1)
        return f(n)