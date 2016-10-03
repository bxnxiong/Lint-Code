class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        
        book = {x:False for x in num}
        maxLen = -1
        
        for i in book:
            
            if book[i] == False:
                #book[i] = True
                current = i + 1
                right_len = 0
                
                while current in book:
                    book[current] = True
                    right_len += 1
                    current += 1
                
                current = i - 1
                left_len = 0
                
                while current in book:
                    left_len += 1
                    book[current] = True
                    current -= 1
                maxLen = max(maxLen,left_len + right_len + 1)
        
        return maxLen
        
        
        