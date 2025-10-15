'''
    RECURSIVE SOLUTION - Maybe not optimal, just that I'm revising recursion topic 
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x, n):
            if x == 0: return 0
            if n == 0: return 1
            
            prod = f(x, n//2)
            prod = prod * prod
            return x * prod if n % 2 != 0 else prod
        res = f(x, abs(n))
        return res if n>=0 else 1/res