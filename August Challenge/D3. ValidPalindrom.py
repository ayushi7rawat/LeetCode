class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        for i in range(len(s)):
            if s[i].isalnum():
                s2 += s[i]
        return s2.lower() == s2[::-1].lower()