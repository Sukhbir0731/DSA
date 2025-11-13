class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def f(i, temp):
            if i == len(digits):
                res.append(temp)
                return
            for digit in hash_list[int(digits[i])]:
                f(i+1, temp+digit)
        hash_list = ['','','abc','def','ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        res = []
        f(0,'')
        return res

