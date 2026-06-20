class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for _, row in enumerate(matrix):
            print(row)
            lastEl = row[-1]
            if lastEl < target: continue

            l = 0
            r = len(row) - 1

            while l<=r:
                mid = (l+r)//2

                if row[mid] == target: return True

                if row[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


