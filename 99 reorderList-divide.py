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
    def reorderList(self, head):
        # write your code here
        if head:
            n = self.length(head)
            middle = n/2
            #print n
            a,b = self.half(head,middle)
            l_a = self.length(a)
            l_b = self.length(b)
            #print l_a,l_b
            counter = 1
            while a and b:
                a_1,a_2 = self.half(a,1)
                b_1,b_2 = self.half(b,l_b-counter)
                a_1.next = b_2
                if b_2:
                    b_2.next = a_2
                    
                a = a_2
                b = b_1
                counter += 1
            if b:
                if b_2:
                    b_2.next = b_1
                elif a_1:
                    a_1.next = b_1
            ###########
            return head
        
    def half(self,head,middle):
        
        first = head
        count = 1
        while count < middle:
            first = first.next
            count += 1
        second = first.next
        first.next = None
        return head,second
    def length(self,head):
        count = 0
        pre = head
        while pre:
            count += 1
            pre = pre.next
        return count