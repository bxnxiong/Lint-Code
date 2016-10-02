class Solution: 
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        # write your code here
                
        n = len(S)
        m = len(T)
        table = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(n+1):
            table[i][0] = 1
            
        for s in range(1,n+1):
            for t in range(1,min(s+1,m+1)):
                if S[s-1] == T[t-1]:
                    table[s][t] = table[s-1][t] + table[s-1][t-1]
                else:
                    table[s][t] = table[s-1][t]
                    
        return table[n][m]