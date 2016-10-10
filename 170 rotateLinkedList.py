# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        # write your code here
        if head:
            if k == 0:
                return head
            else:
                pointer = head
                
                n = 1
                while pointer.next:
                    pointer = pointer.next
                    n += 1
                #print k%n
                
                k = k%n
                pointer.next = head
                
                while n - k > 0:
                    pointer = pointer.next
                    k += 1
                res = pointer.next
                pointer.next = None
                
                return res