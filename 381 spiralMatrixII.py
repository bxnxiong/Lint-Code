class Solution:
    # @param {int} n an integer
    # @return {int[][]} a square matrix
    def generateMatrix(self, n):
        # Write your code here
        r_s,c_s = 0,0
        r_e,c_e = n-1,n-1
        if n > 0:
            res = [[0 for i in range(n)] for j in range(n)]
            
            curr = 1
            while r_e > r_s:
                for c in range(c_s,c_e):
                    
                    res[r_s][c] = curr
                    curr += 1
                for r in range(r_s,r_e):
                    res[r][c_e] = curr
                    curr += 1
                for c in range(c_e,c_s,-1):
                    res[r_e][c] = curr
                    curr += 1
                for r in range(r_e,r_s,-1):
                    res[r][c_s] = curr
                    curr += 1
                r_s += 1
                r_e -= 1
                c_s += 1
                c_e -= 1
            if r_e - r_s == 1:
                res[r_s][c_s] = curr
                curr += 1
                res[r_s][c_e] = curr
                curr += 1
                res[r_e][c_e] = curr
                curr += 1
                res[r_e][c_s] = curr
            elif r_e == r_s:
                res[r_s][c_s] = curr
            return res
        else:
            return []