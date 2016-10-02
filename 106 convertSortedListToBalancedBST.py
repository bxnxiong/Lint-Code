"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if head:
            if head.next and head.next.next: # length >= 3
                left_half,right_half = self.half(head)
                root = left_half #root node is always on left_half
                
                pre = ListNode(0)
                pre.next = root
                
                while root.next:
                    root = root.next
                    pre = pre.next
                
                left = left_half
                right = right_half
                pre.next = None
                
                root = TreeNode(root.val)
                root.left = self.sortedListToBST(left)
                root.right = self.sortedListToBST(right)
                
                return root
            elif head.next: # length = 2
                root = TreeNode(head.val)
                root.right = TreeNode(head.next.val)
                return root
            else: # length = 1
                return TreeNode(head.val)
    def half(self,head):
        slow = fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        h1 = head
        h2 = slow.next
        slow.next = None
        
        return h1,h2
            
        