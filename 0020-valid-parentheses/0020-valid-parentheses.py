class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #A list is used as a stack to keep track of unmatched opening brackets.
        brackets = {')': '(', ']': '[', '}': '{'} #A dictionary mapping each closing bracket to its corresponding opening bracket.
        for c in s: #character c in string s
            if c in "[{(": #if c is an opening bracket,
                stack.append(c)
            else:
                if not stack or stack[-1] != brackets[c]:
                    return False
                stack.pop()
        return not stack