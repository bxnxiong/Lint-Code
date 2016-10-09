class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def setZeroes(self, matrix):
        # write your code here
        if len(matrix) > 0:
            m = len(matrix)
            n = len(matrix[0])
            cols = []
            
            
            for r in range(m):
                has0 = False
                for c in range(n):
                    
                    if matrix[r][c] == 0:
                        has0 = True
                        cols.append(c)
                if has0:
                    matrix[r] = [0]*n
            
            for c in cols:
                for r in range(m):
                    matrix[r][c] = 0
        return matrix