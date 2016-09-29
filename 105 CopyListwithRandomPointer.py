# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

#import copy
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    
    def copyRandomList(self, head):
        if head:
            tmp = head
            
            while tmp:
                new = RandomListNode(tmp.label)
                new.next = tmp.next
                tmp.next = new
                tmp = tmp.next.next
                
            tmp = head
            
            while tmp:
                if tmp.next and tmp.next.random == None:
                    if tmp.random != None:
                        tmp.next.random = tmp.random.next
                tmp = tmp.next.next
            
            result = head.next
            tmp = result
            
            while tmp.next:
                tmp.next = tmp.next.next
                tmp = tmp.next
            return result
    
            