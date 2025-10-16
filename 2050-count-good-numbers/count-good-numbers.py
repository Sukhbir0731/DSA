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