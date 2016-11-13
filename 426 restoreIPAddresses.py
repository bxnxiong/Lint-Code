class Solution:
    # @param {string} s the IP string
    # @return {string[]} All possible valid IP addresses
    def restoreIpAddresses(self, s):
        # Write your code here
        n = len(s)
        splits = self.lengthSequence(n)
        
        res = []
        for a1,a2,a3,a4 in splits:
            s1 = s[:a1]
            s2 = s[a1:(a1+a2)]
            s3 = s[(a1+a2):(n-a4)]
            s4 = s[(n-a4):]
            possible = True
            for i in [s1,s2,s3,s4]:
                if int(i) >255 or str(int(i)) != i:
                    possible = False
                    break
            if possible:
                tmp = '.'.join([s1,s2,s3,s4])
                res.append(tmp)
        return res
    def lengthSequence(self,n):
        res = [[]*3]
        length = 4
        while length > 0:
            tmp = []
            for r in res:
                for i in [1,2,3]: # address can only have at most 3-digits
                    if sum(r)+i<=n:
                        tmp.append(r+[i])
            res = tmp
            length -= 1
        res = [res[i] for i in range(len(res)) if sum(res[i])==n]
        return res
            
        