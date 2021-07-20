# dp[i][j] only relies on dp[i-1][j] and dp[i][j-coins[i]]
# we can use 1d list to replace the 2d list
# remember the difinition and the order of outer loop and the inner loop: using first i coins to make up amount j
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount:
            return 1
        if not coins:
            return 0
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                dp[j] += dp[j-coins[i]] if j>=coins[i] else 0
        return dp[-1]
