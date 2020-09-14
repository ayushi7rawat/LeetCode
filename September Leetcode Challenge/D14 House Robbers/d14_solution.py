class Solution:
'''
Problem Name: House Robber
Author: Ayushi Rawat
Date: 14-09-2020
'''
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) < 3:
            return max(nums)
        
        if (len(nums)> 2):
            nums[1] = max(nums[1], nums[0])
            
            nums[2] = max(nums[2]+nums[0], nums[1])
            
            return self.rob(nums[1:])
        