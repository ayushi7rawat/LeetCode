class Solution:
#5850. Find Greatest Common Divisor of Array
    def findGCD(self, nums: List[int]) -> int:
        first = min(nums)
        second = max(nums)
        res = 1
        
        for i in range(1, nums[-1]+1):
            if first%i == 0 and second%i == 0:
                res = i
        return res
        