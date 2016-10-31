class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        # Write your code here
        if s == '': return ''
        if len(set(s)) == len(s): return s[0]
        
        res = ''
        for i in range(len(s)-1):
            
            p1 = self.getPalindrome(s,i,i)
            p2 = self.getPalindrome(s,i,i+1)
            
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        return res
                
        
    def getPalindrome(self,s,l,r):
        while l>=0 and r<len(s) and s[l] == s[r]:
            l-= 1
            r += 1
        return s[(l+1):r]
        