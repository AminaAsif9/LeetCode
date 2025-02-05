class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if stack and stack[-1] == i: #stack[-1] = last entered element, and= true if both true
                stack.pop()
            else: 
                stack.append(i)
        return "".join(stack)