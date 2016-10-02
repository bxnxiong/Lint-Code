class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        n = len(A)
        dp = [False for i in range(n)]
        dp[0] = True
        
        if A[0] == 0 and len(A) == 1:
            return True
        elif A[0] == 0:
            return False
        else:
            for i in range(n):
                for j in range(i+1,n):
                    if dp[i] and j-i<=A[i]:
                        dp[j] = True
                    
                 
            return dp[n-1]