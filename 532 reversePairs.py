class Solution:
    # @param {int[]} A an array
    # @return {int} total of reverse pairs
    count = 0
    def reversePairs(self, A):
        # Write your code here
        # quick sort
        if len(A) <= 1: return 0
        self.mergesort(A)
        return Solution.count
    
    def mergesort(self,l):
        if len(l) <= 1:
            return l
        
        mid = len(l)/2
        left = self.mergesort(l[:mid])
        right = self.mergesort(l[mid:])
        return self.merge(left,right)
        
    def merge(self,l,r):
        i,j = 0,0
        s = []
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                s.append(l[i])
                i += 1
            else:
                Solution.count += len(l)-i
                s.append(r[j])
                j += 1
        if j < len(r):
            s += r[j:]
        else:
            s += l[i:]
        return s
                
                