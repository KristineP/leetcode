# since each element should only be used once, the second for loop should in a desc order.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1 == 1:
            return False
        s //=2
        n = len(nums)
        dp = [False for _ in range(s+1)]
        dp[0] = True
        for i in range(n):
            for j in range(s,0,-1):
                if j>=nums[i]:
                    dp[j] = dp[j] or dp[j-nums[i]]
        return dp[s]
