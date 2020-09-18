class Solution:
'''
Problem Name: Robot Bounded In Circle
Author: Ayushi Rawat
Date: 17-09-2020
'''
    def isRobotBounded(self, instructions: str) -> bool:
        di = (0,1)
        
        x,y = 0,0
        
        for instruction in instructions:
            if instruction == 'G':
                x,y = x+di[0],y+di[1]
            elif instruction == 'L':
                di = (-di[1],di[0])
            else:
                di = (di[1],-di[0])
                
        return (x == 0 and y == 0) or di!=(0,1)