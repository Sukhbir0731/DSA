'''
    So instead of creating every number and checking, a better way is to just calculate possible solutions and return it

    - so if n is even, it is obvious that half numbers are even and half are primes, so return 5**n/2 * 4**n/2 in that case (as 4 are primes and 5 are evens)

    - for calculating powers, we impleted pow(x,n) in an iterative approach and that gives solution in optimal way

    - TC: O(log n) | Binary exponentiation halves exponent each iteration
    - SC: O(1) | Iterative; no recursion or extra data structures

'''

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def pow(x, y):
            # 4**10 | 4**11
            res = 1
            while y>0:
                if y%2==0:
                    y = y/2
                elif y%2!=0:
                    res = (res * x)%MOD
                    y = y//2
                x = (x*x)%MOD
            return res

            
        MOD = 10**9 + 7
        if n%2==0: return (pow(5, n/2)*pow(4, n/2))%MOD
        else: return (pow(5, ceil(n/2))*pow(4, n//2))%MOD