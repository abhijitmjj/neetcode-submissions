class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                a, b = stack.pop(), stack.pop()
                stack.append(int(a)+int(b))
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) - int(a))
            elif c == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(int(b) * int(a))
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / int(a)))
            else:
                stack.append(c)
        return int(stack[0])


        