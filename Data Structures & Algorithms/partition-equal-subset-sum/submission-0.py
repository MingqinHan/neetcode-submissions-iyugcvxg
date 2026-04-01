class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     totalSum=sum(nums)
    #     N=len(nums)
    #     M=len(nums[0])

    #     dp=[[0]*(M+1) for _ in range(N)]

    #     for i in range(N):
    #         dp[i][0]=0
        
    #     for i in range(M):
    #         dp[0][i]=nums[0]

    #     for i in range(1, N):
    #         for c in range(1, M + 1):
    #             skip = dp[i-1][c]
    #             include = 0
    #             if c - weight[i] >= 0:
    #                 include = nums[i] + dp[i-1][c - weight[i]]
    #             dp[i][c] = max(include, skip)
    #     return dp[N-1][M]
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        # 1. 奇数直接排除
        if totalSum % 2 != 0:
            return False
        
        target = totalSum // 2
        N = len(nums)
        
        # 2. 初始化 DP 表：行数为 N，列数为 target + 1
        # dp[i][c] 为 True 表示前 i 个数字能凑出和 c
        dp = [[False] * (target + 1) for _ in range(N)]
        
        # 3. 填充第一列：和为 0 永远是 True（什么都不选即可）
        for i in range(N):
            dp[i][0] = True
            
        # 4. 填充第一行：只能凑出 nums[0] 这一个数
        if nums[0] <= target:
            dp[0][nums[0]] = True

        # 5. 填表逻辑（套用模板）
        for i in range(1, N):
            for c in range(1, target + 1):
                # 选项 A：不选当前的数字，看前面能不能凑出来
                skip = dp[i-1][c]
                
                # 选项 B：选当前的数字
                include = False
                if c - nums[i] >= 0:
                    include = dp[i-1][c - nums[i]]
                
                # 只要有一种方案能成，就是 True
                dp[i][c] = skip or include
                
            # 优化：如果这一行已经凑出了 target，可以直接返回
            if dp[i][target]:
                return True

        return dp[N-1][target]
