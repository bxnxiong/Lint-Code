class Solution:
    # @param {string} digits A digital string
    # @return {string[]} all posible letter combinations
    def letterCombinations(self, digits):
        # Write your code here
        book = {'0':[],'1':[],'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
        n = len(digits)
        if n == 0: return []
        if n == 1: return book[digits]
        
        left = self.letterCombinations(digits[:(n/2)])
        right = self.letterCombinations(digits[(n/2):]) # right = left + 1 or = left
        
        return self.combination(left,right)
        
    
    def combination(self,list1,list2):
        res = []
        for i in list1:
            for j in list2:
                res.append(i+j)
        return res