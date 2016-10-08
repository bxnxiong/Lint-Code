class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) > 0:
            profit = 0
            low = prices[0]
            
            for i in range(1,len(prices)):
                if prices[i] < low:
                    low = prices[i]
                profit = max(profit,prices[i]-low)
            
            return profit
        else:
            return 0