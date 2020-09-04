class Solution:
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