import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        counters = collections.Counter(s)
        print(counters)

        for idx, char in enumerate(s):
            if counters.get(char) == 1:
                return idx
        return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))
