class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        lenn = len(temps)

        if lenn == 1: return [0]
        out = []
        for i in range(lenn - 1):
            temp = temps[i]
            j = i + 1
            while j < lenn and temp >= temps[j]:
                j+=1
            
            if j < lenn:
                out.append(j-i)
            else:
                out.append(0)
        
        out.append(0) # last el will always have zero val
        return out