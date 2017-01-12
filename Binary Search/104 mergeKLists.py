"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        
        while len(lists) > 2:
            middle = len(lists) / 2
            left = self.mergeKLists(lists[:middle])
            right = self.mergeKLists(lists[middle:])
            return self.sort(left,right)
        if len(lists) == 1:
            return lists[0]
        elif len(lists) == 2:
            left,right = lists[0],lists[1]
            return self.sort(left,right)
            
        
    def sort(self,h1,h2):
        result = ListNode(0)
        pointer = result
        
        while h1 and h2:
            if h1.val < h2.val:
                pointer.next = h1
                h1 = h1.next
                pointer = pointer.next
            else:
                pointer.next = h2
                h2 = h2.next
                pointer = pointer.next
                
        if h1:
            pointer.next = h1
        elif h2:
            pointer.next = h2
        
        return result.next