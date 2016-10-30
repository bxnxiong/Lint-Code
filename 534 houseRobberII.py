class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        if nums == []: return 0
        n = len(nums)
        if n <= 3: return max(nums)
        
        max_sums = [0 for i in range(n)]
        max_sums[0],max_sums[1] = nums[0],max(nums[0],nums[1])
        
        for i in range(2,n):
            max_sums[i] = max(max_sums[i-1],max_sums[i-2]+nums[i])
        last_chosen = True if max_sums[-1] > max_sums[-2] else False
        
        max_sums = [0 for i in range(n)]
        max_sums[-1],max_sums[-2] = nums[-1],max(nums[-1],nums[-2])
        
        for i in range(n-3,-1,-1):
            max_sums[i] = max(max_sums[i+1],max_sums[i+2]+nums[i])
        
        first_chosen = True if max_sums[0] > max_sums[1] else False
        
        if first_chosen and last_chosen:
            
            tmp = nums[1:]
            max_sums = [0 for i in range(n-1)]
            max_sums[0],max_sums[1] = tmp[0],max(tmp[1],tmp[0])
            
            for i in range(2,n-1):
                max_sums[i] = max(max_sums[i-1],max_sums[i-2]+tmp[i])
            first = max_sums[-1]
            
            tmp = nums[:-1]
            max_sums = [0 for i in range(n-1)]
            max_sums[0],max_sums[1] = tmp[0],max(tmp[1],tmp[0])
            
            for i in range(2,n-1):
                max_sums[i] = max(max_sums[i-1],max_sums[i-2]+tmp[i])
            second = max_sums[-1]
            
            return max(first,second)
        else:
            return max_sums[0]
        