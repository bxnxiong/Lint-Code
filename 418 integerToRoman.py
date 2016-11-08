class Solution:
    # @param {int} n The integer
    # @return {string} Roman representation
    def intToRoman(self, n):
        # Write your code here
        romans = 'I	V	X	L	C	D	M'
        romans = romans.split('\t')
        values = '1	5	10	50	100	500	1000'
        values = [int(i) for i in values.split('\t')]
        
        res = ''
        for i in range(len(values)-1,-1,-1):
            times = n / values[i]
            
            if times == 4 and str(n)[0] == '4':
                res = res + romans[i] + romans[i+1]
                n -= values[i+1]-values[i]
            elif times == 1 and str(n)[0] == '9':
                res = res + romans[i-1] + romans[i+1]
                n -= values[i+1] - values[i-1]
            else:
                res += romans[i] * times
                n -= values[i]*times
        return res

