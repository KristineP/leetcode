#backtrack, sorted and jump the same element
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        if not nums:
            return 0
        self.ans = 0
        self.backtrack(sorted(nums),[])
        return self.ans
    def backtrack(self,nums,path):
        if not nums:
            self.ans += 1
            return
        for i in range(len(nums)):
            if len(path)>0 and int(pow(nums[i]+path[-1],0.5))**2 != (path[-1]+nums[i]):
                continue
            if i>0 and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack(nums[:i]+nums[i+1:],path)
            path.pop(-1)  
