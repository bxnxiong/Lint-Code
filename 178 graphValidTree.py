class Solution:
    # @param {int} n an integer
    # @param {int[][]} edges a list of undirected edges
    # @return {boolean} true if it's a valid tree, or false
    def validTree(self, n, edges):
        # Write your code here
        
        group = [i for i in range(n)]
        
        for i,j in edges:
            p,q = group[i],group[j] # groupIDs: p q
            if group[i] == group[j]:
                return False
            for g in range(n):
                if group[g] == p:
                    group[g] = q
            #print group
        if len(set(group))> 1: return False
        return True