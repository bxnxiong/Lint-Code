class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        if n == 0: return []
        start = ['']
        while n > 0:
            new_start = []
            for s in start:
                tmp = self.insert(s)
                new_start += [tmp[i] for i in range(len(tmp)) if tmp[i] not in new_start]
            n -= 1
            start = new_start
        return start
    def insert(self,string):
        # insert '()' str -> list[str]
        if len(string) == 0: return ['()']
        res = []
        for i in range(len(string)):
            tmp = string[:i]+'()'+string[(i):]
            if tmp not in res: res += [tmp]
        return res