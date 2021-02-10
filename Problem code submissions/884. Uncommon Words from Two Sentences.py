class Solution:
#884. Uncommon Words from Two Sentences
    def uncommonFromSentences(self, a: str, b: str) -> List[str]:
            s1 = a.split(' ') + b.split(' ')
            d = {}

            for i in s1:
              if i in d:
                d[i] += 1
              else:
                d[i] = 1

            res = []

            for i in d:
              if d[i] == 1:
                res.append(i)
            return res