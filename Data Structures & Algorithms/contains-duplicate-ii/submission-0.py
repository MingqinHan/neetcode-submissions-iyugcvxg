class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        L=0
        window=set()

        for R in range(len(nums)):

            #window size exceeded
            if R-L>k:
                window.remove(nums[L])
                L+=1

            if nums[R] in window:
                return True
            
            window.add(nums[R])
        
        return False

            #window size not matural