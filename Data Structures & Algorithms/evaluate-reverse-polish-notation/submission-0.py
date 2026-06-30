class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+':lambda a, b: int(a + b),
            '-':lambda a, b: int(a - b),
            '*':lambda a, b: int(a * b),
            '/':lambda a, b: int(a / b)
        }
        output = 0

        for i in range(len(tokens)):
            if tokens[i] in operator:
                b = int(stack.pop())
                a = int(stack.pop())
                output = operator[tokens[i]](a,b)
                stack.append(output)
            else:
                stack.append(tokens[i])
        
        return int(stack[0])