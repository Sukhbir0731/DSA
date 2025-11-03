'''
    Solution in notebook
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def f(i, temp):
            if i==len(nums):
                res.append(temp.copy())
                return
            temp.append(nums[i])
            f(i+1, temp)
            temp.pop()
            while(i<len(nums)-1 and nums[i+1]==nums[i]):
                i+=1
            f(i+1, temp)
        nums.sort()
        res = []
        f(0, [])
        return res