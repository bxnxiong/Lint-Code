class Solution:
    # @param s: a string
    # @return: an integer
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if s == '': return 0
        sets = set(s)
        
        book = {}
        for i in sets:
            book[i] = 0
        
        book[s[0]] = (0,1) # index,length of substr
        res = 1
        for i in range(1,len(s)):
            if book[s[i]] == 0:
                book[s[i]] = (i,book[s[i-1]][1]+1) 
                if book[s[i-1]][1]+1 > res:
                    res = book[s[i-1]][1]+1
            else:
                book[s[i]] = (i,min(i-book[s[i]][0],book[s[i-1]][1]+1))
                if min(i-book[s[i]][0],book[s[i-1]][1]+1) > res:
                    res = min(i-book[s[i]][0],book[s[i-1]][1]+1)
        #print book
        return res