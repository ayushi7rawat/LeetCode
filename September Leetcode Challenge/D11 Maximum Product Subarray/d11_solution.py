class Solution:
'''
Problem Name: Maximum Product Subarray
Author: Ayushi Rawat
Date: 11-09-2020
'''
    def maxProduct(self, nums: List[int]) -> int:
            totalmax = nums[0]
            currentmin = nums[0]
            currentmax = nums[0]
            current = nums[0]
            
            for i in range(1,len(nums)):
                current = nums[i]
                
                currentmaxtemp = max(currentmin*current, currentmax*current, current)
                currentmintemp = min(currentmin*current, currentmax*current, current)
                
                currentmin = currentmintemp
                currentmax = currentmaxtemp
                
                if currentmax > totalmax:
                    totalmax = currentmax
                    
            return totalmax