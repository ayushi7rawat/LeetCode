class Solution:
    def checkZeroOnes(self, s: str) -> bool: 
    '''
    1869. Longer Contiguous Segments of Ones than Zeros
    By: Ayushi Rawat
    '''
        count0, count1, temp0, temp1 = 0, 0, 0, 0
        
        for number in s:
            if number == '0':
                temp0 += 1
                temp1 = 0
            else:
                temp1 += 1
                temp0 = 0
            count0 = max(count0, temp0)
            count1 = max(count1, temp1)
            
        return count1 > count0
            