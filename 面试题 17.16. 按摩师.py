import numpy as np


class Solution(object):
    def massage(self, nums):
        """
        arr[i, 0]代表第i次没有接单
        arr[i, 1]代表第i次接单了
        :type nums: List[int]
        :rtype: int
        """
        if len(nums==0):
            return 0
        n = len(nums)
        arr = np.zeros((n, 2))
        arr[0, 0] = 0
        arr[0, 1] = nums[0]
        for i in range(1, n):
            # 第i次不接单，等于第i-1不接单和第i-1次接单的最大值
            arr[i, 0] = max(arr[i-1, 0], arr[i-1, 1])
            # 第i次接单，那么第i-1次只能不接单
            arr[i, 1] = arr[i-1, 0] + nums[i]
        return int(max(arr[n-1, 0], arr[n-1, 1]))

s = Solution()
print(s.massage([2,1,4,5,3,1,1,3]))
