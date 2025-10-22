class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def f(i, temp):
            if i == len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            f(i+1, temp)
            temp.pop()
            f(i+1, temp)
        
        res = []
        f(0, [])
        return res