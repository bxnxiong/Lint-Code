class Solution:
    # @param {int[][]} matrix a matrix of m x n elements
    # @return {int[]} an integer array
    def spiralOrder(self, matrix):
        # Write your code here
        r_s,c_s = 0,0
        r_e = len(matrix)-1
        
        if matrix != []:
            c_e = len(matrix[0])-1
        else:
            return []
        
        res = []
        if c_e != -1 and r_e != -1:
            while r_s < r_e and c_s < c_e:

                for c in range(c_s,c_e):
                    res.append(matrix[r_s][c])
                for r in range(r_s,r_e):
                    res.append(matrix[r][c_e])
                for c in range(c_e,c_s,-1):
                    res.append(matrix[r_e][c])
                for r in range(r_e,r_s,-1):
                    res.append(matrix[r][c_s])
                r_s += 1
                r_e -= 1
                c_s += 1
                c_e -= 1
            
            if r_s == r_e and c_s == c_e:
                res.append(matrix[r_s][c_s])
            elif r_s == r_e:
                res.extend([matrix[r_s][c] for c in range(c_s,c_e+1)])
            elif c_s == c_e:
                res.extend([matrix[r][c_s] for r in range(r_s,r_e+1)])
        return res
        