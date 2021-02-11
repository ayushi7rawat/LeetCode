#Brute Force:
class Solution:
'''
1450. Number of Students Doing Homework at a Given Time
'''
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime  <=endTime[i]:
                count += 1
        return count


#One-liner:
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum((startTime[i] <= queryTime  <=endTime[i]) for i in range(len(startTime)))
