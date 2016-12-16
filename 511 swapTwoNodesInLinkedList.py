# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        # Write your code here
        if head:
            pointer = head
            v1_pointer,v2_pointer = None,None
            # get node locations and previous nodes
            if pointer.val == v1:
                v1_pointer = pointer
                v1_prev = None
            if pointer.val == v2:
                v2_pointer = pointer
                v2_prev = None
            while pointer.next:
                if pointer.next.val == v1:
                    v1_pointer = pointer.next
                    v1_prev = pointer
                if pointer.next.val == v2:
                    v2_pointer = pointer.next
                    v2_prev = pointer
                if v1_pointer and v2_pointer:
                    break
                pointer = pointer.next
            # check if both values exist in the linked list
            if v1_pointer and v2_pointer:
                # check if neighboring nodes
                # if not check, will exceed time limit
                if (v1_pointer.next and v1_pointer.next.val == v2) or (v2_pointer.next and v2_pointer.next.val == v1):
                    if v1_pointer.next.val == v2:
                        v2_next = v2_pointer.next
                        v2_pointer.next = v1_pointer
                        v1_pointer.next = v2_next
                        if v1_prev:
                            v1_prev.next = v2_pointer
                        else:
                            head = v2_pointer
                    else:
                        v1_next = v1_pointer.next
                        v1_pointer.next = v2_pointer
                        v2_pointer.next = v1_next
                        if v2_prev:
                            v2_prev.next = v1_pointer
                        else:
                            head = v1_pointer
                else:
                    # cut off v1_pointer and v2_pointer as single nodes
                    v1_next = v1_pointer.next
                    v2_next = v2_pointer.next
                    
                    # swap
                    if v1_prev and v2_prev:
                        v1_prev.next = v2_pointer
                        v2_prev.next = v1_pointer
                    elif v2_prev: # if head.val == v1
                        v2_prev.next = v1_pointer
                        head = v2_pointer
                    elif v1_prev:
                        v1_prev.next = v2_pointer
                        head = v1_pointer
                    
                    v1_pointer.next = v2_next
                    v2_pointer.next = v1_next
        return head
        