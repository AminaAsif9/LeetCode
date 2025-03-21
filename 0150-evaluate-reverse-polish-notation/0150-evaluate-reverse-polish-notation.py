class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+","-","/","*"]:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    res = a+b
                elif token == "*":
                    res = a*b
                elif token == "/":
                    res = int(a/b)
                elif token == "-":
                    res = a-b
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]
        # stack = []
        # op = {
        #     '+': lambda a, b: a + b,
        #     '-': lambda a, b: a - b,
        #     '*': lambda a, b: a * b,
        #     '/': lambda a, b: int(a / b),
        # }
        # for token in tokens:
        #     if token in op:
        #         b = stack.pop()
        #         a = stack.pop()
        #         stack.append(op[token](a, b))
        #     else:
        #         stack.append(int(token))
        # return stack.pop()