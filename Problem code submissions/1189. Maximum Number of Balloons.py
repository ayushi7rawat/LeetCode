class Solution:
#1189. Maximum Number of Balloons
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"b":0, "a":0, "l":0, "o":0, "n":0} 
		
        for l in text:
            if l in d:
                d[l] += 1
				
        lo_count = min(d["l"], d["o"]) // 2
        ban_count = min(d["b"], d["a"], d["n"])
		
        return min(lo_count, ban_count)