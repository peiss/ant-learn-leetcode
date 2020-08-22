import numpy as np


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        min_coin = np.array(coins).min()
        dp = np.full(shape=amount + 1, fill_value=float('inf'))
        dp[0] = 0
        for i in range(min_coin, amount + 1):
            arr = []
            for coin in coins:
                if i - coin >= 0:
                    arr.append(dp[i - coin])
            dp[i] = np.array(arr).min() + 1
        return int(dp[amount]) if dp[amount] != float('inf') else -1


s = Solution()
# print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([2], 3))
#print(s.coinChange([1, 2147483647], 2))
