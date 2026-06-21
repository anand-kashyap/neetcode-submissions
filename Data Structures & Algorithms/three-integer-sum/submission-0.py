class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        lenn = len(nums)
        out = []
        for i in range(lenn - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = lenn-1
            n = nums[i]

            while l < r:
                cur_sum = n + nums[l] + nums[r]

                if cur_sum == 0:
                    out.append([n, nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l<r and nums[l] == nums[l-1]: l+=1
                    while l<r and nums[r] == nums[r+1]: r-=1

                elif cur_sum > 0:
                    r-=1
                else:
                    l+=1
        return out
            
