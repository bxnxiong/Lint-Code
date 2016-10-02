class Solution:
    # @param s: A string s
    # @param dict: A dictionary of words dict
    def wordBreak(self, s, dict):
        # write your code here
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        same_length = True
        for i in range(1,len(dict.keys())):
            if len(dict.keys()[i]) != len(dict.keys()[i-1]):
                same_length = False
                
        if dict.keys() == [""] and s != "":
            return False
        elif dict.keys() == [""] and s == "":
            return True
        elif list(set(s)) == dict.keys(): # if s = 'abc' and dict = ['a','b','c']
            return True
        elif same_length and len(dict.keys()) > 0:
            n = len(dict.keys()[0])
            if n > 0 and len(s) % n != 0:
                return False
            else:
                tmp = {}
                i = 0
                while i < len(s) and s[i:(i+n)] not in tmp:
                    tmp[s[i:(i+n)]] = 0
                    i += n
                if list(set(tmp)) != dict.keys():
                    return False
                else:
                    return True
        else:
            for i in range(1,len(s)+1):
                for j in range(i):
                    if dp[j] and s[j:i] in dict:
                        dp[i] = True
                        break
            
            return dp[len(s)]