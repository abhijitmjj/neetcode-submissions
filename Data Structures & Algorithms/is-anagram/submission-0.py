class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c = Counter(s)
        d = Counter(t)
        return c == d
        