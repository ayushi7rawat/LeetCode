class Solution:
'''
Problem Name: Partition Labels
Author: Ayushi Rawat
Date: 04-09-2020
'''
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        last_indices = [0] * 26

        for i in range(len(S)):
            last_indices[ord(S[i]) - ord('a')] = i

        begin = end = 0
        for i in range(len(S)):
            end = max(end, last_indices[ord(S[i]) - ord('a')])

            if end == i:
                res.append(end - begin + 1)
                begin = end + 1

        return res