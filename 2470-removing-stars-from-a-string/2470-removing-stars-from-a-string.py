class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s: #character in string
            if stack and c == "*": #if char is star, remove last element
                stack.pop() 
            else:
                stack.append(c)
        return "".join(stack) #to convert list to string

        #O(N)