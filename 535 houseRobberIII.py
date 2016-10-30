"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        sef.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root, the root of binary tree.
    # @return {int} The maximum amount of money you can rob tonight
    def houseRobber3(self, root):
        # write your code here
        if not root: return 0
        return max(self.max_sum(root))
            
    def max_sum(self,root):
        ''' return (current_val,children_sum)'''
        if root.left:
            left = self.max_sum(root.left)
            l_v = max(left)
        else:
            left,l_v = (0,0),0
        
        if root.right:
            right = self.max_sum(root.right)
            r_v = max(right)
        else:
            right,r_v = (0,0),0
        
        return (root.val+left[1]+right[1],l_v+r_v)
        
        