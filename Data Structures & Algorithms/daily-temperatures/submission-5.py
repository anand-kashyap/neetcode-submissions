class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        lenn = len(temps)

        out = [0] * lenn
        stack = []

        for i,temp in enumerate(temps):
            # stack pushes/pops any element atmost once
            while stack and temp > stack[-1][1]: 
                stackI, stackT = stack.pop()
                out[stackI] = i - stackI

            stack.append((i, temp))

        return out

