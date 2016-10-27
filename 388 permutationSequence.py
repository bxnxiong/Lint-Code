
from math import *
class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    
    def getPermutation(self, n, k):
        if n == 1: return str(n)
        if k == 1:
            res = ''
            for i in range(1,n+1):
                res += str(i)
            return res
        
        if n > 1:
            res = ''
            nums = range(1,n+1)
            
            while n > 0:
                tmp = self.calculate(n,k,nums)
                nums.remove(tmp)
                k = k%factorial(n-1) if k%factorial(n-1) != 0 else factorial(n-1)
                n -= 1
                res += str(tmp)
        return res
    def calculate(self,n,k,nums):
        #nums is a string
        return nums[(k-1)/factorial(n-1)]