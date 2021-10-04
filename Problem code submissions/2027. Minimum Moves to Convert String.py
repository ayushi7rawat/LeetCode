class Solution:
#2027. Minimum Moves to Convert String
    def minimumMoves(self, s: str) -> int:
        count, i = 0, 0

        while i < len(s):
            if s[i] == 'O':
                i += 1
            else:
                #print(s[i],count,i)
                count += 1
                i = i + 3
        return count
