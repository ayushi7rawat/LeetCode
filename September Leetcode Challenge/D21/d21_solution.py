class Solution:
'''
Problem Name: Unique Paths III
Author: Ayushi Rawat
Date: 20-09-2020
'''
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        non_obstacles = 0
        start_row, start_col = 0, 0
        for row in range(0, rows):
            for col in range(0, cols):
                cell = grid[row][col] 
                if  cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row, start_col = row, col
                    
        path_count = 0

        def helper_backtrack(row, col, remain):
            nonlocal path_count

            if grid[row][col] == 2 and remain == 1:

                path_count += 1
                return

            temp = grid[row][col] 
            grid[row][col] = -4
            remain -= 1   
  
            for ro, co in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                next_row, next_col = row + ro, col + co

                if not (0 <= next_row < rows and 0 <= next_col < cols):
 
                    continue
                if grid[next_row][next_col] < 0:

                    continue

                helper_backtrack(next_row, next_col, remain)

            grid[row][col] = temp

        helper_backtrack(start_row, start_col, non_obstacles)

        return path_count
        