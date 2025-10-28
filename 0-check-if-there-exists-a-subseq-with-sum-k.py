'''

Check if there exists a subsequence with sum K


Problem Statement: Given an array nums and an integer k. Return true if there exist subsequences such that the sum of all elements in subsequences is equal to k else false.

Examples
Example 1:
Input : nums = [1, 2, 3, 4, 5] , k = 8
Output : Yes
Explanation : The subsequences like [1, 2, 5] , [1, 3, 4] , [3, 5] sum up to 8.

Example 2:
Input : nums = [4, 3, 9, 2] , k = 10
Output : No
Explanation : No subsequence can sum up to 10.
'''

def f(i, temp):
    if i == len(nums):
        if temp == k:
            return True
        return False
    if f(i+1, temp) or f(i+1, temp+nums[i]):
        return True
    return False

nums = [4, 3, 9, 2]
k = 10
if f(0,0):
    print("Exists")
else:
    print("DNE!")


