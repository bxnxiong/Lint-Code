class Solution:
    # @param {double} x the base number
    # @param {int} n the power number
    # @return {double} the result
    def myPow(self, x, n):
        # Write your code here
        if n == 1: return x
        if n == 0: return 1
        if n < 0:
            return 1/self.myPow(x,-n)
        elif n % 2 == 0:
            return self.myPow(x*x,n/2)
        else:
            return self.myPow(x*x,n/2)*x