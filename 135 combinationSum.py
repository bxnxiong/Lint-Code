class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    
    def combinationSum(self, candidates, target):
        # write your code here
        from copy import deepcopy
        table = [[] for i in range(target+1)]
        table[0] = [0]
        
        for i in candidates:
            table[i] = [[i]]
        
        for i in range(1,target+1):
            
            for j in candidates:
                
                if table[i] == []:
                    if i - j > 0:
                        table[i] = deepcopy(table[i-j])
                        for k in table[i]:
                            k.append(j)
                            k.sort()
                else:
                    if i - j > 0:
                        tmp = deepcopy(table[i-j][:])
                        
                        for k in tmp:
                            tmp2 = k[:]
                            tmp2.append(j)
                            tmp2.sort()
                            if tmp2 not in table[i]:
                                table[i].append(tmp2)
                        
        return table[-1]
                        