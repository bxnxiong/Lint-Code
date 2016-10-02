class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        # write your code here
        
        n = len(word1)
        m = len(word2)
        
        table = [[0 for i in range(m+1)] for j in range(n+1)]
        
        for i in range(1,n+1):
            table[i][0] = i
            
        for j in range(1,m+1):
            table[0][j] = j
            
        for i in range(1,n+1):
            for j in range(1,m+1):
                table[i][j] = min(table[i-1][j]+1,table[i][j-1]+1,table[i-1][j-1]+(1 if word1[i-1]!=word2[j-1] else 0))
        
        return table[n][m]