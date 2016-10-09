class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here  
        res = []
        nums = range(1,n+1)
        
        while k > 0:
            if len(res) == 0:
                for i in nums:
                    res.append([i])
            else:
                tmp = res[:]
                res = []
                for i in nums:
                    for j in tmp:
                        
                        if i not in j and i > j[-1]:
                            j_cp = j[:]
                            j_cp.append(i)
                            res.append(j_cp)
                            
            k -= 1
        return res