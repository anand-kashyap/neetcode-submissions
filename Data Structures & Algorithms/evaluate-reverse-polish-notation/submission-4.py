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
        
        if len(stack) == 1:
            return int(stack[0])
        else:
            return 0 # stack not full empty

        