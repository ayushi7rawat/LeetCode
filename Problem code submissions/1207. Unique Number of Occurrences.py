class Solution:
#1207. Unique Number of Occurrences
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return len(set(d.values())) == len(d.values())