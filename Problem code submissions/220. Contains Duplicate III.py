class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            for j in range(i+1, i+k+1,1):
                if j < len(nums) and abs(nums[i] - nums[j]) <= t:
                    return True
        return False