class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def f(curr):
            if curr == len(s):
                res.append(temp_list.copy())
                return
            for i in range(curr, len(s)):
                substr = s[curr:i+1]
                if substr == substr[::-1]:
                    temp_list.append(substr)
                    f(i+1)
                    temp_list.pop()

        res = []
        temp_list = []
        f(0)
        return res