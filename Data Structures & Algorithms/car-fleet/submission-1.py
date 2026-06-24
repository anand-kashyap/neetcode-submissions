class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getSteps(p, s):
            return (target - p)/s
        
        mapp = {}
        for i in range(len(position)):
            sp = speed[i]
            po = position[i]

            mapp[po] = sp
        
        sortedd = []
        for p in sorted(position):
            sortedd.append((p, mapp[p]))
        
        stack = []
        for car in sortedd[::-1]: # reverse loop
            p = car[0]
            s = car[1]

            stack.append(getSteps(p, s))
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

            

