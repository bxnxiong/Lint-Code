def sortList(self, head):
        # write your code here
        if head:
            l = []
            temp = deepcopy(head)
            n = 0
            
            while temp:
                n += 1
                l.append(deepcopy(temp))
                temp = temp.next
            
            self.mergeSort(l,1,n)
            
            return l[0]
        else:
            return
        
    
    def iter(self,head):
        while head:
            yield head
            head = head.next
            
    def mergeSort(self,l,start,end):
        
        if end > start:
            middle = (end + start) / 2
            #print start,middle,end
            self.mergeSort(l,start,middle)
            self.mergeSort(l,middle+1,end)
            
            self.merge(l,start,middle,end)
        
            
    def merge(self,l,start,middle,end):
        left = deepcopy(l[(start-1):middle])
        right = deepcopy(l[middle:end])
        
        i = 0
        j = 0
        
        #print 'another round',start,middle,end
        for index in range(len(l)):
            if i >= middle - start + 1 and j >= end - middle:
                break
            elif index + 1 > end:
                break
            else:
                if index+1 >= start:
                    if i < middle - start + 1:
                        left_v = left[i].val
                    else:
                        left_v = float('Inf')
                        
                    if j < end - middle:
                        right_v = right[j].val
                    else:
                        right_v = float('Inf')
                    
                    if left_v <= right_v and left_v != float('Inf'):
                        l[index].val = left_v
                        if index >= 1:
                            l[index-1].next = l[index]
                        i += 1
                    elif right_v < left_v:
                        l[index].val = right_v
                        if index >= 1:
                            l[index-1].next = l[index]
                        j += 1
                    else:
                        break
                
        