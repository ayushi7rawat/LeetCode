class Solution:
#1748. Sum of Unique Elements 
    def sumOfUnique(self, nums: List[int]) -> int:
        s = {}
        for i in nums:
          if i in s:
            s[i] += 1
          else:
            s[i] = 1
        
        res = 0
        for i in s:
          if s[i]==1:
            res += i
        return res(a)