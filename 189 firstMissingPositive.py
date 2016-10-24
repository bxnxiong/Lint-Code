class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        posi = []
        
        for i in range(len(A)):
            if A[i] > 0:
                posi.append(A[i])
        
        n = len(posi)
        for i in range(n):
            if abs(posi[i]) <= n:
                posi[abs(posi[i])-1] = -abs(posi[abs(posi[i])-1])
            
        for i in range(n):
            if posi[i] > 0: return i+1
        return n+1
        
        
        