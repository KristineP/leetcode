'''
description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
'''

# similiar with 2sum
# add one more loop
# use sort and set to avoid duplication
# use dict: look up time O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3 :
            return []
        res = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            total = 0 - nums[i]
            dic = dict()
            for j in range(i+1,len(nums)):
                if total - nums[j] in dic:
                    res.add((nums[i], nums[j], total - nums[j]))
                else:
                    dic[nums[j]] = 1
        return list(res)
