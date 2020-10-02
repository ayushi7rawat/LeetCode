class Solution:
'''
Problem Name: First Missing Positive
Author: Ayushi Rawat
Date: 30-09-2020
'''
    def firstMissingPositive(self, nums: List[int]) -> int:
        #If given list is not empty, we will found maximum number of list.
        if nums:
            res = max(nums) 
        #If given list is empty, our first missing positive number will be 1.
        else:
            return 1
        #If maximum number in given list is less than or equal to 0 then our result will be 1. 
        if res <= 0:
            return 1
            
        #Otherwise we will iterate from 1 to res + 2, if any number will not be present in given list, we return that number.
        for i in range(1, res + 2):
            if i not in nums:
                return i
        
