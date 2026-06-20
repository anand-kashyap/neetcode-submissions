from math import inf

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, [])
        self.data[key].append([timestamp, value])
# [[1, 'bar'], [4, 'bar2']]
    def get(self, key: str, timestamp: int) -> str:
        if not self.data.get(key): return ''

        l = 0
        r = len(self.data[key]) - 1
        
        maxx = [-inf, ""]
        while l <= r:
            mid = l + ((r-l)//2)
            
            midO = self.data[key][mid]
            midT = midO[0]
            midV = midO[1]

            if midT == timestamp: return midV
            if midT > timestamp:
                r = mid - 1
            else:
                if midT > maxx[0]:
                    maxx = midO
                l = mid + 1
        
        return maxx[1]

            

