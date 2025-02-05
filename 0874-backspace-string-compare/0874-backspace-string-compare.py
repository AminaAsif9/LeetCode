class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = [] # create an empty stack
        for char in s: # chk for every char in s
            if char == "#": 
                if stack_s: # chk if stack_s exists, cuz if it's empty then pop will give error
                    stack_s.pop() # remove recent element
            
            else:
                stack_s.append(char) # append that character in stack_s

        # Process the second string
        stack_t = []
        for char in t: 
            if char == "#": 
                if stack_t: 
                    stack_t.pop()
            
            else:
                stack_t.append(char) 

        # Compare the two stacks
        return stack_s == stack_t