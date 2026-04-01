class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        R=len(board)
        C=len(board[0])

        def dfs(r, c):

            if r<0 or r>=R or c<0 or c>=C or board[r][c]!='O':
                return

            if board[r][c]=='O':
                board[r][c]='T'
            # visited[r][c]=True
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        

        for i in range(R):
            dfs(i,0)
            dfs(i,C-1)

        for j in range(C):
            dfs(0,j)
            dfs(R-1,j)
        
        for i in range(R):
            for j in range(C):
                if board[i][j]=='T':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
            