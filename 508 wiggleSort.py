class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        i = 0
        if len(nums) <= 1: pass
        elif len(nums) <= 3:
            top = nums.index(max(nums))
            nums[1],nums[top] = nums[top],nums[1]
        else:
            while i+2 < len(nums):
                # pick max of three
                three = [nums[i],nums[i+1],nums[i+2]]
                top = three.index(max(three))
                if i+1 != top:
                    nums[i+1],nums[i+top] = nums[i+top],nums[i+1] # move to middle
                if i+3 < len(nums) and nums[i+2] > nums[i+3]:
                    nums[i+2],nums[i+3] = nums[i+3],nums[i+2]
                i += 2
