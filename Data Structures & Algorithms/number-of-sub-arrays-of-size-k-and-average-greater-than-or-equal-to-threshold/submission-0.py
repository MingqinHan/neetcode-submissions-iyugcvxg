class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        L=0
        window=set()
        window_sum=0
        num=0

        for R in range(len(arr)):

            if R-L+1>k:
                window_sum-=arr[L]
                L+=1        
            window_sum+=arr[R]
            avg=window_sum/k
            if avg>=threshold and R>=k-1:
                num+=1
        return num