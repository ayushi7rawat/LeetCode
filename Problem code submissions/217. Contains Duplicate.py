class Solution:
#217. Contains Duplicate
    def containsDuplicate(self, nums: List[int]) -> bool:
        return  len(set(nums)) != len(nums)