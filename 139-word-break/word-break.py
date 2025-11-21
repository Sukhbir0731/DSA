class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def f(s):
            if s=="":
                return True
            if s in memo:
                return memo[s]
            for i in range(1,len(s)+1):
                if s[0:i] in wordSet and f(s[i:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False
        memo = {} # substr -> True/False
        wordSet = set(wordDict)
        return f(s)