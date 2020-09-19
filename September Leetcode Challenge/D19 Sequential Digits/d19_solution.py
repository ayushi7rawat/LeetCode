class Solution:
'''
Problem Name: Sequential Digits
Author: Ayushi Rawat
Date: 19-09-2020
'''
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        for num in range(1,9):
            while num <= high:
                x = num % 10
                
                if x == 0:
                    break
                    
                if num >= low:
                    res.append(num)
                
                num = (num * 10) + x + 1
        
        return sorted(res)
        