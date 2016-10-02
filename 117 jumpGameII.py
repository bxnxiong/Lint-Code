class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        # write your code here
        
        steps = 0
        farthest = 0
        curr = 0
        for i in range(len(A)):
            if i > farthest:
                farthest = curr
                steps += 1
            curr = max(curr, i+A[i])
        return steps
        
        