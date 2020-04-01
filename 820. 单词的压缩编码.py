from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        result = set(words)
        for word in words:
            for i in range(1, len(word)):
                result.discard(word[i:])
        return len("#".join(result) + "#")


s = Solution()
print(s.minimumLengthEncoding(["time", "me", "bell"]))
