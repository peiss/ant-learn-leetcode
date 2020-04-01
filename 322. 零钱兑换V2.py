from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 代表兑换amount=i的个数
        # min(dp[i-1], dp[i-2], dp[i-5])
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            methods = []
            for coin in coins:
                if i - coin >= 0:
                    methods.append(dp[i - coin])
            if methods:
                dp[i] = min(methods) + 1
        print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1



s = Solution()
# print(s.coinChange([1, 2, 5], 11))
print(s.coinChange([1,2], 2))
