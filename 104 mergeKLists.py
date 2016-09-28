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
        if len(lists) > 0:
            n = len(lists)
            result = ListNode(0)
            tmp = result
            
            while not self.isnull(lists):
                value_min = [float('Inf'),None]
                
                for i,head in enumerate(lists):
                    if head:
                        if head.val < value_min[0]:
                            value_min[0] = head.val
                            value_min[1] = i
                
                if lists[value_min[1]]:
                    min_node = lists[value_min[1]]
                    tmp.next = min_node
                    tmp = tmp.next
                    lists[value_min[1]] = min_node.next
                
            return result.next
        
        
    def isnull(self,lists):
        result = True
        
        for i in lists:
            if i:
                result = False
                break
        return result

