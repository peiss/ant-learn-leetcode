import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = collections.Counter(nums)
        data = c.most_common(1)
        return data[0][0]


s = Solution()
print(s.majorityElement([3,2,3]))
print(s.majorityElement([2,2,1,1,1,2,2]))