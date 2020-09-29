class Solution:
'''
Problem Name: Word Break
Author: Ayushi Rawat
Date: 29-09-2020
'''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        
        def helper(s):
            if s == "":
                return True
            
            if s in dp:
                return dp[s]
            
            for i in wordDict:
                if i == s[:len(i)] and helper(s[len(i):]):
                    dp[s] = True
                    
                    return True
            dp[s] = False
            
        return helper(s)