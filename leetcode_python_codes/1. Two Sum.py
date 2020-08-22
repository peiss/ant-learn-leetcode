from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 存储内容：当前元素的差值和下标
        my_dict = {}
        for idx, v in enumerate(nums):
            if v in my_dict:
                return [my_dict[v], idx]
            else:
                my_dict[target - v] = idx


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
