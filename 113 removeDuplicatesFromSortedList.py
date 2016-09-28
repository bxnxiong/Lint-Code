"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head:
            
            if head.next:
                
                pre = ListNode(head.val-1)
                pre.next = head
                result = pre
                pointer = head.next
                
                while pointer:
                    if head.val == pointer.val:
                        pointer = pointer.next
                        
                        while pointer and head.val == pointer.val:
                            pointer = pointer.next
                        
                        if pointer:
                            pre.next = pointer
                            head = pointer
                            pointer = pointer.next
                        else:
                            pre.next = None
                            
                    else:
                        head = head.next
                        pointer = pointer.next
                        pre = pre.next
                
                return result.next
            else:
                return head
        