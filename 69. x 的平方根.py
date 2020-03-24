class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1

        left, right = 1, x
        while left <= right:
            mid = int(left + (right - left) / 2)

            if mid == int(x / mid):
                return mid
            elif mid < int(x / mid):
                left = mid + 1
            elif mid > int(x / mid):
                right = mid - 1
        return right


s = Solution()
print(s.mySqrt(4))
print(s.mySqrt(8))
