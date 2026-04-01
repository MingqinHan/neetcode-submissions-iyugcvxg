class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        R,C=len(grid), len(grid[0])


        q=deque()


        for i in range(R):
            for j in range(C):
                if grid[i][j]==0:
                    q.append((i,j))
        
        level=0
        while q:
            
            size=len(q)

            for i in range(size):

                r,c=q.popleft()

                directions=[(1,0),(0,1),(-1,0),(0,-1)]

                if grid[r][c]== 2147483647:
                    grid[r][c]=level

                # grid[r][c]=level

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc


                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]==2147483647:
                        # grid[nr][nc]=grid[r][c]+1
                        q.append((nr,nc))
            level+=1





            


