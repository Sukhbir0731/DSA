'''
    Reverses a stack using recursion.

    Approach:
    1. Recursively pop all elements from the stack until it becomes empty.
    2. On the way back (while unwinding recursion), insert each popped element
    at the bottom of the stack using the helper function `insertElements`.
    3. This effectively reverses the stack in place.

    Time Complexity: O(n²)
    Space Complexity: O(n)   (due to recursion stack)
'''


class Solution:
    def reverseStack(self, stack):
        def popElements():
            if len(stack) == 0:
                return
            temp = stack.pop()
            popElements()
            insertElements(temp)

        def insertElements(temp):
            if len(stack) == 0:
                stack.append(temp)
                return
            element = stack.pop()
            insertElements(temp)
            stack.append(element)

        popElements()
        return stack
