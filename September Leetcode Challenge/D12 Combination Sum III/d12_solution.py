class Solution:
'''
Problem Name: Maximum Product Subarray
Author: Ayushi Rawat
Date: 12-09-2020
'''
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
            res = []
            
            def helper(nums, k, n, index, path, res):
                if k < 0  or n < 0:
                    return
                if k == 0 and n == 0:
                    res.append(path)
                    
                for i in range(index, len(nums)):
                    helper(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)
                
            helper(range(1,10), k, n, 0, [], res)
            
            return res