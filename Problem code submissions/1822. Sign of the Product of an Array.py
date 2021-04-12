class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
		
        for i in range(len(nums)):
            prod *= nums[i]
            
        if prod > 0:
            return 1
        elif prod == 0:
            return 0
        else:
            return -1
			
				
#Second solution
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
			
        count = 0
        for i in nums:
            if i < 0:
                count += 1
        return 1 if count%2 == 0 else -1
            