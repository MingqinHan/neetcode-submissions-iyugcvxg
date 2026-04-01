class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L=0
        window_sum=0
        length=float('inf')

        for R in range(len(nums)):
            window_sum+=nums[R]   
            while window_sum>=target:
                
                window_sum-=nums[L]
                length=min(length, R-L+1)
                L+=1

        if length==float('inf'):
            return 0
        else:
            return length
            