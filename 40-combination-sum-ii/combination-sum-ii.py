class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(i, temp, total):
            if total == target:
                res.append(temp.copy())
                return
            if (total>target or i>=len(candidates)):
                return
            temp.append(candidates[i])
            f(i+1, temp, total+candidates[i])
            temp.pop()
            while i<len(candidates)-1 and candidates[i+1] == candidates[i]:
                i+=1
            f(i+1, temp, total)
        res = []
        candidates.sort()
        f(0, [], 0)
        return res