class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}

        stack = []
        for token in tokens:
            if token in ops:
                r2 = stack.pop()
                r = stack.pop()
                if token == '+':
                    r += r2
                elif token == '-':
                    r-= r2
                elif token == '*':
                    r*=r2
                else:
                    r = int(r / r2)
                stack.append(r)
            else:
                stack.append(int(token))
        
        return stack[0]

        