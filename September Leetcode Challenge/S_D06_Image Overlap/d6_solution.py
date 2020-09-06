class Solution:
'''
Problem Name: Image Overlap
Author: Ayushi Rawat
Date: 06-09-2020
'''
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        d1 = collections.defaultdict(int)
        temp1 = []
        temp2 = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if(A[i][j] == 1):
                    temp1.append((i,j))
                if(B[i][j] == 1):
                    temp2.append((i,j))
        res = 0
        for a in temp1:
            for b in temp2:
                c = (b[0]-a[0],b[1]-a[1])
                d1[c] += 1
                res = max(res, d1[c])
        return res