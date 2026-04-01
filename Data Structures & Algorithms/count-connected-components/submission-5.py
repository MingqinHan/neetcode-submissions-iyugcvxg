class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        par=[i for i in range(n)]
        rank=[0 for _ in range(n)]

        def find(x):
            p=par[x]
            while p!=par[p]:
                par[p]=par[par[p]]
                p=par[p]
            return p
        
        def union(n1,n2):
            p1, p2=find(n1),find(n2)

            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                par[p2]=p1
                rank[p1]+=rank[p2]
            else:
                par[p1]=p2
                rank[p2]+=rank[p1]
            return True
        comps = n
        for a, b in edges:
            if union(a, b):
                comps -= 1
        return comps