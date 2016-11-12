class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        if len(s) == 0: return [[]]
        
        res = []
        if self.isPalindrome(s):
            res.append([s])
        for split in range(1,len(s)+1):
            
            if self.isPalindrome(s[:split]):
                left = [[s[:split]]]
                right = self.partition(s[split:])
            
                tmp = [left[0]+right[j] for j in range(len(right))]
                
                for i in tmp:
                    if i not in res:
                        res.append(i)
        return res
        
    def isPalindrome(self,string):
        if len(string) == 0: return True
        i = 0
        j = len(string)-1
        res = False
        while string[i] == string[j]:
            i += 1
            j -= 1
            if i >= j:
                res = True
                break
        return res