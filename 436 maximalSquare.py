class Solution:
    #param matrix: a matrix of 0 and 1
    #return: an integer
    def maxSquare(self, matrix):
        # write your code here
        if len(matrix) == 0: return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0]*cols for i in range(rows)]
        
        res = 0
        
        for r in range(rows):
            for c in range(cols):
                if (not r) or (not c):
                    dp[r][c] = matrix[r][c]
                else:
                    if matrix[r][c] == 1:
                        dp[r][c] = min(dp[r-1][c-1],dp[r][c-1],dp[r-1][c]) + 1
                    else:
                        dp[r][c] = 0
                    if r == 3 and c == 0:
                        print dp[r][c],res
                if dp[r][c] > res:
                    res = dp[r][c]
        
        return res*res