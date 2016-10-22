class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        # write your code here
        
        if sum(gas) >= sum(cost):
            n = len(gas)
            u = [0]*n
            
            for i in range(n):
                u[i] = gas[i]-cost[i]

            remain = [float('-inf')] * n
            
            for i in range(n):
                remain[i] = max(remain[i-1 if i-1>=0 else -1] + u[i],u[i])
            
            start = 0
            max_remain = 0

            for i in range(n):
                if remain[i] > 0 and remain[i-1 if i-1>=0 else -1] < 0:
                    if remain[i] > max_remain:
                        max_remain = remain[i]
                        start = i
            
            return start
            
        else:
            return -1