"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """  
    def isValidBST(self, root):
        # write your code here
        result = True
        
        if root:
               
            if root.left:
                
                if root.left.val >= root.val:
                    result = False
                else:
                    temp = root.left
                    while temp.right:
                        temp = temp.right
                    if temp.val >= root.val:
                        result = False
                    else:
                        result = self.isValidBST(root.left)
        
            if result == False:
                return result
            else:
                if root.right:
                        
                    if root.right.val <= root.val:
                        result = False
                    else:
                        temp = root.right
                        while temp.left:
                            temp = temp.left
                        if temp.val <= root.val:
                            result = False
                        else:
                            result = self.isValidBST(root.right)
        return result    
                    