class Solution:
'''
Problem Name: Gas Station
Author: Ayushi Rawat
Date: 23-09-2020
'''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        index = -1
        
        cost1 = sum(cost) - sum(gas)
        l = len(gas)
        
        if cost1 > 0:
            return -1
        
        for i in range(l):
            temp = tank + gas[i]
            
            if temp >= cost[i]:
                if tank == 0:
                    index = i
                    
                temp2 = gas[i] - cost[i]
                tank += temp2
            else:
                tank = 0
                index = -1
                
        return index
        