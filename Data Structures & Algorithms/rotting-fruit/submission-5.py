class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q=deque()
        visit=set()
        ROWS=len(grid)
        COLS=len(grid[0])
        allzero=True
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==2:
                    q.append((i,j))
                    visit.add((i,j))
                if grid[i][j]==2 or grid[i][j]==1:
                    allzero=False
        
        if allzero:
            return 0
        length=0
        while q:

            for i in range(len(q)):

                r,c=q.popleft()
                
                
                directions=[[-1,0],[0,-1],[0,1],[1,0]]

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]==0 or (nr,nc) in visit:
                        continue
                    if grid[nr][nc]==1:
                        grid[nr][nc]=2
                    visit.add((nr,nc))
                    q.append((nr,nc))
                    
            
            length+=1
        length-=1
        for i in grid:
            if 1 in i:
                return -1
        return length    
                




# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]:
#             return -1

#         q=deque()
#         visit=set()
#         q.append((0,0))
#         visit.add((0,0))

#         length=0
#         while q:
#             for i in range(len(q)):

#                 r,c=q.popleft()
                
#                 if r==len(grid)-1 and c==len(grid[0])-1:
#                     return length+1

                
#                 directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

#                 for dr,dc in directions:
#                     nr=r+dr
#                     nc=c+dc
#                     if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]==1 or (nr,nc) in visit:
#                         continue
#                     visit.add((nr,nc))
#                     q.append((nr,nc))
            
#             length+=1
#         return -1    