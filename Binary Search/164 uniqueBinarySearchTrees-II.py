"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @paramn n: An integer
    # @return: A list of root
    def generateTrees(self, n):
        # write your code here
        if n == 0:
            return [TreeNode('')]
        n = range(1,n+1)
        return self.dfs(n)
        
    def dfs(self,n):
        res = []
        #print n
        if len(n) == 0: return []
        elif len(n) == 1:
            tmp = TreeNode(n[0])
            res.append(tmp)
        elif len(n) == 2:
            tmp = TreeNode(n[0])
            tmp.right = TreeNode(n[1])
            res.append(tmp)
            
            tmp = TreeNode(n[1])
            tmp.left = TreeNode(n[0])
            res.append(tmp)
        else:
            for i in range(len(n)):
                tmp = n[:]
                left_trees = self.dfs(n[:i])
                right_trees = self.dfs(n[(i+1):])
                
                if len(left_trees) > 0 and len(right_trees) > 0:
                    for l in left_trees:
                        for r in right_trees:
                            t = TreeNode(n[i])
                            t.left = l
                            t.right = r
                            res.append(t)
                elif len(left_trees) > 0:
                    for l in left_trees:
                        t = TreeNode(n[i])
                        t.left = l
                        res.append(t)
                else:
                    for r in right_trees:
                        t = TreeNode(n[i])
                        t.right = r
                        res.append(t)
        return res
                    
            