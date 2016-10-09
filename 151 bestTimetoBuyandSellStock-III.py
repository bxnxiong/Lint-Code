class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) ==0:return 0
        low = prices[0]
        high = prices[len(prices)-1]
        left = [0]*len(prices)
        leftP = 0
        right = [0]*len(prices)
        rightP = 0
        
        for i in range(1,len(prices)):
            if prices[i] < low:
                low = prices[i]
            left[i] = max(left[i-1],prices[i]-low)
            
        for j in range(len(prices)-2,-1,-1):
            
            if prices[j] > high:
                high = prices[j]
            right[j] = max(high - prices[j],right[j+1])
        
        result = 0
        for i in range(len(prices)):
            if left[i]+right[i] > result:
                result = left[i]+right[i]
        return result