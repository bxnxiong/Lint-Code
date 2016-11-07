class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if sum(nums) < s: return -1
        
        n = len(nums)
        l = 0
        r = 1
        subTotal = nums[0]
        res = n + 1
        while r < n:
            
            while subTotal < s and r < n:
                subTotal += nums[r]
                r += 1
                
            while subTotal >= s:
                res = min(res,r-l)
                subTotal -= nums[l]
                l += 1
        return res