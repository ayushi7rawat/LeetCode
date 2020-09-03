class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sub = ''
        l1 = len(s)
        
        for i in range(l1-1):
            sub = sub + s[i]
            l2 = len(sub)
            
            res = sub*(l1//l2)
            
            if res == s:
                return True
        return False