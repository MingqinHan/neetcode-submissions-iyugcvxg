class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW=len(grid)
        COL=len(grid[0])
        directions=[[1,0],[-1,0],[0,1],[0,-1]]



        def dfs(r,c):

            if r<0 or c<0 or r>=ROW or c>=COL or grid[r][c]==0:
                return 0
            
            grid[r][c]=0
            area=1
            for dr, dc in directions:
                area+=dfs(r+dr,c+dc)
            return area
        maxArea=-1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curArea=dfs(i,j)
                maxArea=max(maxArea,curArea)
        return maxArea 
