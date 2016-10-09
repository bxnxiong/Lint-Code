class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """
    def rotate(self, matrix):
        # write your code here
        # pattern: (row,col) -> (col,n-1-row) but we rotate it backwards 3 times
        # so actual pattern used in code is: (row,col) -> (n-1-col,row)
        n = len(matrix)
        
        circle = 1
        while circle <= n/2:
            
            
            for c in range(circle-1,n-circle):
                start_row = circle - 1
                rotate = 3
                
                while rotate > 0:
                    
                    matrix[start_row][c],matrix[n-1-c][start_row] = matrix[n-1-c][start_row],matrix[start_row][c]
                    rotate -= 1
                    start_row,c = n-1-c,start_row
            circle += 1
        return matrix
            