class Solution:
    '''
    1619. Mean of Array After Removing Some Elements
    Author: Ayushi Rawat
    '''
    
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        
        n = len(arr)

        per = int(n*5/100)

        l2 = arr[per:len(arr)-per]
        x = sum(l2)/len(l2)

        return x
        
        