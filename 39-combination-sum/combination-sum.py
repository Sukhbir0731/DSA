class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def f(i, temp, total):
            if total == target:
                res.append(temp.copy())
                return
            if total > target or i >= len(candidates):
                return
            temp.append(candidates[i])
            f(i, temp, total+candidates[i])
            temp.pop()
            f(i+1, temp, total)
        res = []
        f(0, [], 0)
        return res