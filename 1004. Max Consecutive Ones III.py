# sliding window
# pay attention to the boundry conditions
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0
        left,right = 0,0
        n = 0 
        ans = 0
        while right<len(nums):
            while right <len(nums):
                if nums[right]==1:
                    right+=1
                else:
                    if n<k:
                        n+=1
                        right+=1
                    else:
                        break
            # print(right,left)
            ans = max(ans,right-left)
            while left<=right and right<len(nums):
                if nums[left]!=0:
                    left+=1
                else:
                    n-=1
                    left+=1
                    break
        return ans
