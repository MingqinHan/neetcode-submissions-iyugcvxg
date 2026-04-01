class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s=Counter(s)
        set_t=Counter(t)
        return (set_s==set_t)