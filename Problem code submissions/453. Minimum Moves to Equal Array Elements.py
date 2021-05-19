class Solution:
    #gives timeout error
    def minMoves(self, nums: List[int]) -> int:
	'''
	453. Minimum Moves to Equal Array Elements
    By: Ayushi Rawat
	'''
        counter = 0
        curr_min = min(nums)
        curr_max = max(nums)

        while curr_max != curr_min:
            counter += 1
            nums.sort()
            
            for i in range(len(nums)-1):
                nums[i] += 1

            curr_min = min(nums)
            curr_max = max(nums)    
        return counter
        
    #second improved solution
    def minMoves(self, nums: List[int]) -> int:
        _sum = 0
        _min = min(nums)
        
        for i in range(len(nums)):
            _sum += (nums[i] - _min)
            
        return _sum