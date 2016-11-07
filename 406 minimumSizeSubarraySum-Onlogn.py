class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        if sum(nums) < s: return -1
        
        n = len(nums)
        res = 0
        size = n
        pre_size = 0
        visited = {}
        while size not in visited:
            visited[size] = 1
            if self.possible(size,nums,s):
                res = size
                pre_size = size
                size /= 2
            else:
                size = (pre_size+size)/2

        if pre_size - size >= 2:
            for i in range(size,pre_size):
                if i not in visited:
                    if self.possible(i,nums,s):
                        return i
        return res
    def possible(self,size,nums,s):
        sums = 0
        
        for i in range(len(nums)):
            sums += nums[i]
            if i >= size:
                sums -= nums[i-size] # keep window size at constant
            if sums >= s:
                return True
        return False
