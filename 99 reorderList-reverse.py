"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: nothing
    """

    def reorderList(self,head):
        # basic steps:
        # step 1: split linked list into two halves
        # step 2: reverse the second half linked list
        # step 3: create new linked list using those two halves
        
        head1,head2 = self.half(head)
        head2 = self.reverse(head2)
        
        result = ListNode(0)
        pointer = result
        
        while head1 and head2:
            pointer.next = head1
            head1 = head1.next
            pointer = pointer.next
            pointer.next = head2
            head2 = head2.next
            pointer = pointer.next
        
        result = result.next
        return result
            
        
    def half(self,head):
        # use slow and quick pointer
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = dummy
        head2 = slow.next
        slow.next = None
        head1 = head1.next
        
        return head1,head2
        
    def reverse(self,head):
        dummy = ListNode(0)
        dummy.next = head
        h2 = head.next
        head.next = None
        
        while h2:
            tmp = h2
            h2 = h2.next
            tmp.next = dummy.next
            dummy.next = tmp
        
        return dummy.next