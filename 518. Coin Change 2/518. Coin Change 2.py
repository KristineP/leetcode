# dynamic programming
# definition: using first i coins to get amount j = using first i-1 coins to get amount j + using first i coins to get amount j-coins[i]
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        if not coins:
            return 0
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j] + ((dp[i][j-coins[i-1]] if j>=coins[i-1] else 0))
        return dp[-1][-1]
