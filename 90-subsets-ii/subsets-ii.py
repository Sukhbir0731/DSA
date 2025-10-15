'''
    - input: nums (array)
        - contains duplicates

    - output: return all possibe subsets
        - must not contain duplicate subsets
        - any order is ok

    - Example
    - nums = [1,2,2]

    - pseudo code (DOESN'T WORK!!)
    - f(i, ds):
        - start with f(0, [])
        - base case:
            - if i==len(nums):
                - res.append(ds.copy())
        - pick nums[i]
                - ds.append(nums[i])
                - call f(i+1, ds)
        - not pick nums[i]
                - ds.pop()
                - call f(i+1, ds)

    - Correct approach to not consider duplicates is sort them in ascending order first
    - then call a function f(i, ds)
        - where i is index of what element is to be considered from sorted list
        - ds is the temp data structure to which you should append values, that will be itself appended to result
        - example: [1, 1, 2, 3, 3, 3]
        - you call firstly f(0, [])
            - that means you are on index 0 currently and your subset is []
        - then you take each number in the subset, while skipping duplicates
            - you append value to temp,
            - append temp's copy to res and then
            - you call f(1, [1]), f(3, [2]), f(4, [3])
        - and so on....
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def f(i, temp):
            if i>=len(nums):
                return
            if i==0:
                res.append(temp.copy())
            # res.append(temp)
            for j in range(i, len(nums)):
                if j<=len(nums)-1:
                    if j>i and nums[j]==nums[j-1]:
                        continue
                    temp.append(nums[j])
                    res.append(temp.copy())
                    f(j+1, temp)
                    temp.pop()
        nums.sort()
        res = []
        f(0, [])
        return res