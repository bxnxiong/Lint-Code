class Solution:
    # @param heights: a list of integers
    # @return: a integer
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n == 0: return 0
        forward = 0
        backward = 0
        res = 0
        
        piv = heights[0]
        start = 0
        for i in range(1,n):
            if i != n-1:
                if not (heights[i] >= heights[i-1] and heights[i] >= heights[i+1] and piv <= heights[i]):
                    diff = piv - heights[i] if piv - heights[i]>0 else 0
                    forward = forward + diff
                else:
                    tmp = forward
                    forward = 0
                    piv = heights[i]
                    for j in range(i-1,start-1,-1):
                        if heights[j] <= piv:
                            diff = piv - heights[j] if piv - heights[j]>0 else 0
                            backward = backward + diff
                    start = i
                    res += min(tmp,backward)
                    backward = 0
            else:
                piv = heights[i]
                for j in range(i-1,start-1,-1):
                    if heights[j] <= piv:
                        backward = backward + piv - heights[j]
                    else:
                        piv = heights[j]
                res += min(forward,backward)
                    
        return res
        
