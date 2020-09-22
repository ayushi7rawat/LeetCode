class Solution:
'''
Problem Name: Majority Element II
Author: Ayushi Rawat
Date: 22-09-2020
'''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_capacity = collections.defaultdict(int)
            
            for i in range(len(trips)):
                num = trips[i][0]
                start = trips[i][1]
                dest = trips[i][2]
                
                for j in range(start,dest):
                    trip_capacity[j] += num
                    
                    if trip_capacity[j] > capacity:
                        return False
            return True
        