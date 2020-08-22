from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = [0] * len(nums)

        result[0] = nums[0]
        for idx in range(1, len(nums)):
            result[idx] = max(result[idx - 1] + nums[idx], nums[idx])
        print(result)
        return max(result)


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
