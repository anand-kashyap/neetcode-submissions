class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {'+', '-', '*', '/'}

        stack = []
        for token in tokens:
            if token in ops:
                if len(stack) >= 2:
                    r2 = int(stack.pop())
                    r = int(stack.pop())
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
                    return 0 # cant do ops
            else:
                stack.append(token)
        
        if len(stack) == 1:
            return int(stack[0])
        else:
            return 0 # stack not full empty

        