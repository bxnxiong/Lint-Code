class Solution:
    # @param {string} s Roman representation
    # @return {int} an integer
    def romanToInt(self, s):
        # Write your code here
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        i = 0
        res = 0
        while i < len(s):
            if i < len(s)-1 and roman[s[i]]<roman[s[i+1]]:
                res += roman[s[i+1]]-roman[s[i]]
                i += 2
            else:
                res += roman[s[i]]
                i += 1
        return res