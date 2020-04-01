from typing import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        datas = collections.defaultdict(list)
        for s in strs:
            #print(sorted(s))
            datas[tuple(sorted(s))].append(s)
        return list(datas.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
