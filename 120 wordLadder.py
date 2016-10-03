class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here
        
        dict.add(end)
        
        q = []
        q.append((start,1))
        
        while q:
            curr = q.pop(0)
            c_word = curr[0];c_len = curr[1]
            if c_word == end: return c_len
            else:
                for i in range(len(c_word)):
                    left = c_word[:i];right = c_word[(i+1):]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if c_word[i] != j:
                            new = left + j + right
                            if new in dict:
                                q.append((new,c_len+1))
                                dict.remove(new)
        return 0