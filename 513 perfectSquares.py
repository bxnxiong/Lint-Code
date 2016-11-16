class Solution:
    # @param {int} n a positive integer
    # @return {int} an integer
    def numSquares(self, n):
        # Write your code here
        # uses num theory: 4**x*(8a+7)
        while n % 4 == 0:
            n /= 4
        if n%8 == 7:
            return 4
        for i in range(0,int(n**0.5)+1):
            if int((n-i**2)**0.5)**2+i**2 == n:
                return 1+(0 if i == 0 else 1)
        return 3