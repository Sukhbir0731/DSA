"""
    Generate Binary Strings Without Consecutive 1s
    
    Given an integer n, return all binary strings of length n that do not contain consecutive 1s. Return the result in lexicographically increasing order.
    
    
    A binary string is a string consisting only of characters '0' and '1'.
    
    
    Examples:
    Input: n = 3
    
    Output: ["000", "001", "010", "100", "101"]
    
    Explanation: All strings are of length 3 and do not contain consecutive 1s.
    
    Input: n = 2
    
    Output: ["00", "01", "10"]

"""

def generateBinaryStrings(n):
    def f(i, temp):
        if i==n:
            res.append(temp)
            return
        temp = temp+"0"
        f(i+1, temp)
        temp = temp[:-1]
        if not temp or temp[-1]!='1':
            temp = temp + "1"
            f(i+1,temp)
            temp = temp[:-1]
            
    temp = ""
    res = []
    f(0, "")
    return res

print(generateBinaryStrings(3))

'''
# Neater verion
def generateBinaryStrings(n):
    def backtrack(i, temp):
        # base case: full length reached
        if i == n:
            res.append(temp)
            return
        
        # always can add '0'
        backtrack(i + 1, temp + "0")
        
        # can only add '1' if previous char isn't '1'
        if not temp or temp[-1] != "1":
            backtrack(i + 1, temp + "1")
    
    res = []
    backtrack(0, "")
    return res


'''
