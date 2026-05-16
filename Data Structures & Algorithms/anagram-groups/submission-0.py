from collections import Counter, defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for x in strs:
            # key = tuple(sorted(x))
            # ans[key].append(x)
            ans[tuple(sorted(Counter(x).elements()))].append(x)
        
        return list(ans.values())

    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)