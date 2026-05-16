from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = defaultdict(int)
        for c in s:
            d[c] += 1
        for s in t:
            d[s] -= 1
        print(d)
        for v in d:
            if d[v] != 0:
                return False
        
        return True
        