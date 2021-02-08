class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """         
        zero, one, two = 0, 0, 0
        
        #count occourance of 1's 2's 3's
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            else:
                two += 1
                
        nums[:] = [0]*zero + [1]*one + [2]*two