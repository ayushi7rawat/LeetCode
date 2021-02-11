class Solution:
#1304. Find N Unique Integers Sum up to Zero
    def sumZero(self, n: int) -> List[int]:
            res = []

            for i in range(1, (n //2)+ 1):
                res.append(i)
                res.append(-i)

            if n % 2 != 0:
                res.append(0)
            return res