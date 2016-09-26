"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from copy import *
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    
    # quick sort implementation
    def sortList(self,head):
        n = self.length(head)
        if head:
            self.quickSort(head,1,n)
            return head
        
    
    def length(self,head):
        n = 0
        while head:
            n += 1
            head = head.next
        return n
    
    def get(self,head,num):
        pre = head
        count = 1
        while count < num:
            count += 1
            pre = pre.next
        return pre
        
    def swap(self,head,i,j):
        count = 1
        pre = head
        if i < j:
            while pre and count < i:
                pre = pre.next
                count += 1
            first = pre
            while pre and count < j:
                pre = pre.next
                count += 1
            second = pre
            first.val,second.val = second.val,first.val
        return head
        
    def quickSort(self,head,start,end):
        
        if start < end:
            p = self.partition(head,start,end)
            #print start,end,p
            self.quickSort(head,start,p-1)
            self.quickSort(head,p+1,end)
            
    def partition(self,head,start,end):
        pivot = self.get(head,end).val
        i = start
        
                
        j = 1
        pre = head
        while j < start:
            pre = pre.next
            j += 1
        #pre = pre.next
        while j < end:
            if pre.val <= pivot:
                self.swap(head,i,j)
                i += 1
            j += 1
            pre = pre.next
            
        
        self.swap(head,i,end)
        return i