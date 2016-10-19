class Solution:
    # @param strs: A list of strings
    # @return: A list of strings
    def anagrams(self, strs):
        # write your code here
        book = {}
        for s in strs:
            if str(sorted(s)) not in book:
                book[str(sorted(s))] = [1,[s]]
            else:
                book[str(sorted(s))][1].append(s)
                book[str(sorted(s))][0] += 1
        
        
        res = []
        for k in book.keys():
            if book[k][0] > 1:
                res.extend(book[k][1])
        
        return res
                