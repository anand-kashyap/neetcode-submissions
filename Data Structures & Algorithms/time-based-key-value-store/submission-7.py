from math import inf

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data.setdefault(key, [])
        self.data[key].append((timestamp, value)) # keep as list, because time stamps
        # although increasing, but will have gaps like set(1), set(2), set(5)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.data.get(key)
        if not arr: return ''

        l = 0
        r = len(arr) - 1
        
        ans = [-inf, ""]
        while l <= r:
            mid = l + ((r-l)//2)
            
            midO = arr[mid]
            midT = midO[0]
            midV = midO[1]

            if midT == timestamp: return midV
            if midT < timestamp:
                ans = midO
                l = mid + 1
            else:
                r = mid - 1
        
        return ans[1]

            

