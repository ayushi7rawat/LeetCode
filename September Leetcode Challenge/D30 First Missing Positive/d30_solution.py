class Solution:
'''
Problem Name: First Missing Positive
Author: Ayushi Rawat
Date: 30-09-2020
'''
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums:
            res = max(nums) 
        else:
            return 1
        
        if res < 0:
            res = 1
            
        for i in range(1, res + 2):
            if i not in nums:
                return i
        
