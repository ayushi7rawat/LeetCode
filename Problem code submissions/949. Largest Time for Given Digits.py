class Solution:
    '''
    September Leetcode Challenge Day 1
    '''
    def largestTimeFromDigits(self, mylist1: List[int]) -> str:
        if len(mylist1) == 0:
            return ""
        mylist1.sort(reverse = True)
        arr = list(permutations(mylist1))

        for h1, h2, m1, m2 in arr:
            hrs = h1 * 10 + h2
            mins = m1 * 10 + m2

            if hrs < 24 and mins < 60:
                return "{}{}:{}{}".format(h1, h2, m1, m2)
        return ""
