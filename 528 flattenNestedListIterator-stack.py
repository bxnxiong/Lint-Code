# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return {boolean} True if this NestedInteger holds a single integer,
#        rather than a nested list.
#        """
#
#    def getInteger(self):
#        """
#        @return {int} the single integer that this NestedInteger holds,
#        if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self):
#        """
#        @return {NestedInteger[]} the nested list that this NestedInteger holds,
#        if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = []
        self.l = nestedList
        
    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        
        return self.stack.pop().getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while self.l or self.stack:
            if not self.stack:
                self.stack.append(self.l.pop(0))
            while self.stack and not self.stack[-1].isInteger():
                top = self.stack.pop().getList()
                for e in top[::-1]:
                    self.stack.append(e)
            if self.stack and self.stack[-1].isInteger():
                return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())