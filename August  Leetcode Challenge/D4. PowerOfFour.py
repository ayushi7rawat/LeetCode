class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        #with loop only
        if (num == 4 or num == 1):
            return True

        if (num < 4 or num % 4 != 0):
            return False
        #looping
        temp = num
        while (temp > 1):
            if (temp % 4 != 0):
                return False
            temp = temp / 4
        return temp == 1