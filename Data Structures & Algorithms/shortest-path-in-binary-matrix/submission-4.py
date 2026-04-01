class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[len(grid)-1][len(grid[0])-1]:
            return -1

        q=deque()
        visit=set()
        q.append((0,0))
        visit.add((0,0))

        length=0
        while q:
            for i in range(len(q)):

                r,c=q.popleft()
                
                if r==len(grid)-1 and c==len(grid[0])-1:
                    return length+1

                
                directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if nr<0 or nc<0 or nr>=len(grid) or nc>=len(grid[0]) or grid[nr][nc]==1 or (nr,nc) in visit:
                        continue
                    visit.add((nr,nc))
                    q.append((nr,nc))
            
            length+=1
        return -1    
                                   