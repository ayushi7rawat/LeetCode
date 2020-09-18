class Solution:
'''
Problem Name: Best Time to Buy and Sell Stock
Author: Ayushi Rawat
Date: 18-09-2020
'''
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float(inf)
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                temp = price - min_price
                max_profit = max(max_profit, temp)
        return max_profit