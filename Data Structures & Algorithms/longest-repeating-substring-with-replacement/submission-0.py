class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        L=0

        window={}
        length=0
        for R in range(len(s)):
            if s[R] not in window:
                window[s[R]]=1
            else:
                window[s[R]]+=1

            while sum(window.values())-max(window.values())>k:
                window[s[L]]-=1
                L+=1

            length=max(length, R-L+1)
        return length