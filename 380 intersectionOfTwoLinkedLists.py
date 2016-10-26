# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        # Write your code here
        counter_a,counter_b = 1,1
        
        pointerA = headA
        if headA and headB:
            while pointerA.next:
                counter_a += 1
                pointerA = pointerA.next
            pointerB = headB
            while pointerB.next:
                counter_b += 1
                pointerB = pointerB.next
            
            if pointerA.val == pointerB.val:
                pointerA,pointerB = headA,headB
                if counter_a < counter_b:
                    count = counter_b - counter_a
                    
                    for i in range(count):
                        pointerB = pointerB.next
                elif counter_b < counter_a:
                    count = counter_a - counter_b
                    
                    for i in range(count):
                        pointerA = pointerA.next
                    
                while pointerA and pointerB and pointerA.val != pointerB.val :
                    pointerA = pointerA.next
                    pointerB = pointerB.next
                        
                return pointerA
            
            
        