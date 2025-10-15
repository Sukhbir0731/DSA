'''
    - Ignore any leading whitespace (" ")
        - use .strip()

    - Determine the sign by checking if the next character is '-' or '+'
        - assuming positivity if neither present.
        - pushh into res whatever sign you encounter between - or +

    - Read the integer by skipping leading zeros
        - until a non-digit character is encountered
            check using isalpha()
        OR
        - end of the string is reached

    - If no digits were read, then the result is 0.
    -   s = "42"            OP: 42
    -   s = " -042"         OP: -42
    -   s = "1337c0d3"      OP: 1337
    -   s = "0-1"           OP: 0 
    -   s = "words and 987" OP: 0

'''
class Solution:
    def myAtoi(self, s: str) -> int:
        def f(i, num):
            if i>=len(s) or not s[i].isdigit():
                return sign*num
            
            num = num * 10 + int(s[i])

            if sign * num <= INT_MIN: return INT_MIN
            if sign * num >= INT_MAX: return INT_MAX

            return f(i+1, num)
        
        i = 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        while i < len(s) and s[i] == ' ': 
            i+=1

        sign = 1 # let it be by default +1
        if i<len(s) and (s[i] == '+' or s[i] == '-'): 
            sign = -1 if s[i]=="-" else 1
            i+=1
        
        return f(i, 0)
        