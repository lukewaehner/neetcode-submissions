class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                val1 = stack.pop()
                val2 = stack.pop()
                res = None
                if t == '+':
                    res = val2 + val1
                if t == '-':
                    res = val2 - val1
                if t == '*':
                    res = val2 * val1
                if t == '/':
                    res = int(val2 / val1)
                print(res)
                stack.append(res)
            else:
                stack.append(int(t))
            # print(stack)
        return stack.pop()
