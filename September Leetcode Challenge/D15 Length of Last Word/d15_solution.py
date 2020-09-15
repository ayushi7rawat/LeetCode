class Solution:
'''
Problem Name: Length of Last Word
Author: Ayushi Rawat
Date: 15-09-2020
'''
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip() #remove leading and trailing whitespaces
        counter = 0
        for i in string[::-1]: #reverse the whole string
            if i == ' ':
                break
            else:
                counter += 1
        return counter
        