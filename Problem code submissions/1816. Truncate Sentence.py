class Solution:
'''
1816. Truncate Sentence
'''
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        return " ".join(words[:k])