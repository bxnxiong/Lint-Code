class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) > 0:
            low = prices[0]
            profits = 0
            maxProfit = 0
            
            for i in range(1,len(prices)):
                if prices[i] < prices[i-1]:
                    low = prices[i]
                    profits += maxProfit
                    maxProfit = 0
                maxProfit = max(prices[i]-low,maxProfit)
            profits += maxProfit
            return profits
        
        else:
            return 0