from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        
        for s in strs:
            str_arr = [0]*26
            # char map
            for c in s:
                str_arr[ord(c)-ord('a')] += 1
            groups[tuple(str_arr)].append(s)
        return list(groups.values())

        