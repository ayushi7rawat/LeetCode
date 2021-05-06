def threeConsecutiveOdds(arr):
	'''
	1550. Three Consecutive Odds
	Author: Ayushi Rawat
    '''
    if len(arr) < 3:
        return False

    for i in range(len(arr) - 2):
        odd1 = arr[i]
        odd2 = arr[i + 1]
        odd3 = arr[i + 2]

        if (odd1 % 2 != 0) and (odd2 % 2 != 0) and (odd3 % 2 != 0):
            return True
    return False

# res = threeConsecutiveOdds([7,8,9,3,2,3])
# print(res)