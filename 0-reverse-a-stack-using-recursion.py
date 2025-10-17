'''
  Algorithm explanation for sorting a stack in descending order using recursion:
  
  The goal is to sort the stack so that the largest element ends up at the top.  
  We achieve this using two recursive functions — one to pop all elements (`popElements`)  
  and another to insert them back in the correct order (`insertElements`).
  
  1. First, recursively pop every element from the stack until it becomes empty.
  2. Once the base case is reached (empty stack), begin inserting each popped element
     back into the stack in sorted (descending) order.
  3. The `insertElements(temp)` function places `temp` at the correct position:
     - If the stack is empty or the top element is smaller than `temp`, push `temp`.
     - Otherwise, pop the top element, recursively call `insertElements(temp)`,
       and then push the temporarily removed element back.
  4. This ensures that after every insertion, the stack remains sorted in descending order.
  5. As recursion unwinds, the stack is rebuilt in sorted order.
  
  Example (top at right):
  Input: [5, 2, 4]
  Steps:
  - Pop 4, then 2, then 5 (stack becomes empty)
  - Insert 5 → [5]
  - Insert 2 → [5, 2]  (since 5 > 2)
  - Insert 4 → pop 2 → [5], insert 4 → [5, 4], push back 2 → [5, 4, 2]
  Final stack: [5, 4, 2]  (descending order top→bottom)
'''

class Solution:
    def sortStack(self, stack):
        def popElements():
            if len(stack) == 0:
                return
            temp = stack.pop()
            popElements()
            insertElements(temp)

        def insertElements(temp):
            if len(stack) == 0 or stack[-1]<temp:
                stack.append(temp)
                return
            element = stack.pop()
            insertElements(temp)
            stack.append(element)
            
        popElements()
        return stack

  
