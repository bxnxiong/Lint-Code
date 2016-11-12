# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def isPalindrome(self, head):
        # Write your code here
        if not head: return True
        
        # count length of linked list
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half linked list
        p,pre = slow.next,None
        while p:
            next = p.next
            p.next = pre
            pre,p = p,next
        
        p1,p2 = head,pre
        while p1 and p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        return p2 is None