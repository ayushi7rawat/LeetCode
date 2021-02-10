class Solution:
#242. Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)