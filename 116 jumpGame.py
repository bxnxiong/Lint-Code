class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        # write your code here
        i = 0
        while i < len(A) and A[i]+i < len(A):
            max_step = 0
            max_i = 0
            
            if A[i] == 0:
                if len(A) == 1:
                    return True
                else:
                    return False
            else:
                if len(A) >= 2:
                    for j in range(1,A[i]+1):
                        if i+j < len(A) and A[i+j] >= max_step:
                            max_step = A[i+j]
                            max_i = i+j
                    
                    i = max_i
                    if i == len(A) - 1:
                        return True
                    
        return True