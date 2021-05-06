class Solution:
	'''
	1636. Sort Array by Increasing Frequency
	Author: Ayushi Rawat
    '''
	
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)

        x = sorted(nums, key=nums.count)
        return x