
'''
    Count all subsequences with sum K
    
    Problem Statement: Given an array nums and an integer k.Return the number of non-empty subsequences of nums such that the sum of all elements in the subsequence is equal to k.
    
    Examples
    Example 1:
    Input : nums = [4, 9, 2, 5, 1] , k = 10
    Output : 2
    Explanation : The possible subsets with sum k are [9, 1] , [4, 5, 1].
    
    Example 2:
    Input : nums = [4, 2, 10, 5, 1, 3] , k = 5
    Output : 3
    Explanation : The possible subsets with sum k are [4, 1] , [2, 3] , [5].

'''

def f(i, summ):
    nonlocal res
    if summ > k:
        return
    if i==len(nums):
        if summ == k:
            res += 1
        return
    f(i+1, summ + nums[i])
    f(i+1, summ)
    
res = 0
k = 10
nums = [4, 9, 2, 5, 1]
f(0,0)
print(res)
