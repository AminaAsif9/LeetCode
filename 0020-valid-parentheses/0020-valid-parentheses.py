class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "{":
                stack.append("}")
            elif c == "[":
                stack.append("]")
            else:
            # Check if stack is empty or if the top element doesn't match
                if not stack or c != stack.pop():
                    return False

    # Check if the stack is empty at the end
        return not stack

        #  other approach
        # stack = [] #A list is used as a stack to keep track of unmatched opening brackets.
        # brackets = {')': '(', ']': '[', '}': '{'} #A dictionary mapping each closing bracket to its corresponding opening bracket.
        # for c in s: #character c in string s
        #     if c in "[{(": #if c is an opening bracket,
        #         stack.append(c)
        #     else:
        #         if not stack or stack[-1] != brackets[c]:
        #             return False
        #         stack.pop()
        # return not stack