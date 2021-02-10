class Solution:
#387. First Unique Character in a String
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        d = Counter(s)
        
        for i in d:
            if d[i] == 1:
                return s.index(i)
        else:
            return -1