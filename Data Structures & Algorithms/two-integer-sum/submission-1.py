class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a,b=0,0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    a,b=i,j
        if a<=b:
            return [a,b]
        else:
            return [b,a] 
        
        