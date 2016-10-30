class Solution:
    # @param A: a list of non-negative integers.
    # return: an integer
    def houseRobber(self, A):
        # write your code here
        if A == []: return 0
        if len(A) <= 2: return max(A)
        
        max_sum = [0 for i in range(len(A))]
        
        max_sum[0] = A[0]
        max_sum[1] = max(A[0],A[1])
        
        for i in range(2,len(A)):
            max_sum[i] = max(max_sum[i-1],max_sum[i-2]+A[i])
        return max_sum[-1]