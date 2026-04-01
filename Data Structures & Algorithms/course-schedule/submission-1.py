class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)

        for cur,pre in prerequisites:
            graph[cur].append(pre)
        
        status=[0 for _ in range(numCourses)]
        def dfs(c, status):
            if status[c]==1:
                return True
            if status[c]==2:
                return False

            status[c]=1
            for pre in graph[c]:
                if dfs(pre,status):
                    return True
            status[c]=2
            return False
        for i in range(len(graph)):
            if dfs(i,status):
                return False
        
        return True