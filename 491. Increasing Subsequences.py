# use set() instead of list to avoid duplicate elements
# backtrack
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        self.result = set()
        self.backtrack(nums,0,[])
        return self.result
    def backtrack(self,nums,start,ans):
        if len(ans)>=2:
            self.result.add(tuple(ans[:]))
        for i in range(start,len(nums)):
            if ans == [] or nums[i] >= ans[-1]:
                ans.append(nums[i])
                self.backtrack(nums,i+1,ans)
                ans.remove(ans[-1])
