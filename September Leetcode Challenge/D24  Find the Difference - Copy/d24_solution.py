class Solution:
'''
Problem Name: Largest Number
Author: Ayushi Rawat
Date: 25-09-2020
'''
    ddef largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ' '
        
        for x in range(0, len(nums)-1):
            for y in range(x+1, len(nums)):
                i = str(nums[x])
                j = str(nums[y])
                
                if int(i + j) < int(j + i):
                    temp = nums[x]
                    nums[x] = nums[y]
                    nums[y] = temp
        
        if nums[0] == 0:
            return '0'
        
        res = ''
        count = 0
        
        while count < len(nums):
            res += str(nums[count])
            
            count += 1
            
        return res
        