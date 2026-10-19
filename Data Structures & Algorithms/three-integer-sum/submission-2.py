class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            while(l<r):
                cur = nums[i]+nums[l]+nums[r]
                if cur > 0:
                    r = r-1
                elif cur < 0:
                    l = l+1
                else:
                    res.add((nums[i],nums[l],nums[r]))
                    l = l+1
                    r = r-1                    
        return [list(t) for t in res]

                
