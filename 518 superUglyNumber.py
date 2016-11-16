class Solution:
    # @param {int} n a positive integer
    # @param {int[]} primes the given prime list
    # @return {int} the nth super ugly number
    def nthSuperUglyNumber(self, n, primes):
        # Write your code here
        if n == 1: return 1
        
        powers = [0]*len(primes) # index of num to be multiplied with i_th primes
        q = [1]
        while len(q) < n:
            min_num = min([q[powers[i]]*primes[i] for i in range(len(powers))])
            q += [min_num]
            for i in range(len(powers)):
                if q[powers[i]]*primes[i] == min_num:
                    powers[i] += 1
        return q[-1]