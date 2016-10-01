class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        
        table = [[False for i in range(len(s))] for j in range(len(s))]
        cuts = [0 for i in range(len(s)+1)]
        # initialize cuts lists to store cost of cutting every element
        for i in range(len(s)+1):
            cuts[i] = len(s)-i
            
        for row in range(len(s)-1,-1,-1):
            for col in range(row,len(s)):
                if s[row] == s[col] and (col - row < 2 or table[row+1][col-1]):
                    table[row][col] = True
                    cuts[row] = min(cuts[row],cuts[col+1]+1)
        
        return cuts[0]-1
            
            