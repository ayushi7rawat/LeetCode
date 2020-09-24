class Solution:
'''
Problem Name: Find the Difference
Author: Ayushi Rawat
Date: 24-09-2020
'''
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        
        for i in s:
            t.remove(i)
            
        return t[0]
        