class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closes = [')', '}', ']']
        opens = ['(', '[', '{']
        for c in s:
            if c in opens:
                stack.append(c)
                continue
            if not stack:
                return False
            curr = stack[-1]
            if c == ')' and curr == '(':
                stack.pop()
            elif c == '}' and curr == '{':
                stack.pop()
            elif c == ']' and curr == '[':
                stack.pop()
            else:
                return False
        if not stack:
            return True
        else:
            return False