"""
因为是连续子序列和，所以每次从当前数出发，考察到该位置的最大和，该位置的数要么参与了和，要么就是它本身，如果当前数 + 前一个数能使得当前数的处境更好，则相加，否则不作为
"""

import numpy as np


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + dp[i - 1] > nums[i]:
                dp[i] = nums[i] + dp[i - 1]
            else:
                dp[i] = nums[i]
        return int(np.array(dp).max())


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
