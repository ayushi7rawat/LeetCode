class Solution:
'''
Problem Name:  Teemo Attacking
Author: Ayushi Rawat
Date: 26-09-2020
'''
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        
        if n==0:
            return 0
        
        total = 0
        
        for i in range(n-1):
            total += min(timeSeries[i+1] - timeSeries[i], duration)
            
        return total + duration
            