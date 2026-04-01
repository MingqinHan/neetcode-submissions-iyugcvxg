class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # N=len(nums)
        # M=target

        # dp=[[0]*(M+1) for _ in range(N)]
        # # dp[i][j], before (including) the ith element, the possible solutions to get the sum of j
        # # skip: dp[i][j]=dp[i-1][j]
        # # include(add or subtract): dp[i][j]=dp[i-1][j]+1
        # # dp[i][j]=max(skip, include)
        # for i in range(M):
        #     if abs(nums[0])==i:
        #         dp[0][i]=1
        #         for j in range(i,M):
        #             dp[0][j]=1
        #         break
        

        # for i in range(1,N):
        #     for j in range(M):

        #         #skip

        #         if M-nums[i]==0 or M

        N=len(nums)
        dp=[defaultdict(int) for _ in range(N+1)]
        dp[0][0]=1

        for i in range(N):
            for total,count in dp[i].items():
                dp[i+1][total+nums[i]]+=count
                dp[i+1][total-nums[i]]+=count
        return dp[N][target]

