class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        
        i0 = 0
        i2 = len(nums)-1
        
        i = 0
        while i < len(nums):
            
            if nums[i] == 2:
                nums[i],nums[i2] = nums[i2],nums[i]
                i2 -= 1
            elif nums[i] == 0:
                nums[i],nums[i0] = nums[i0],nums[i]
                i0 += 1
                i += 1
            else:
                i += 1
            
            if i0 >= i2 - 1 or i > i2:
                break
            
        return nums