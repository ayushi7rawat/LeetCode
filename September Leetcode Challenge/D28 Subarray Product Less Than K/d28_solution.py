class Solution:
'''
Problem Name: Subarray Product Less Than K
Author: Ayushi Rawat
Date: 28-09-2020
'''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        prod = 1
        res = left = 0
        
        for right, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[left]
                
                left += 1
                
            res += right - left + 1
            
        return res