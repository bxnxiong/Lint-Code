class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        # write your code here
        
        n = len(nums)
        if nums[0] >= nums[-1] and n > 1:
            if n == 0:return
            if n == 2 or n == 3:
                i = 0
                while i+1 < n:
                    if nums[i] > nums[i+1]:
                        return nums[i+1]
                    i += 1
                return
            left = nums[:n/2]
            right = nums[n/2:]
            if len(set(left)) > 1 and len(set(right)) > 1:
                if left[0] > left[-1]:
                    return self.findMin(left)
                else:
                    return self.findMin(right)
            elif len(set(right)) == 1:
                if left[0] > left[-1] or left[0] <= right[0]:
                    return self.findMin(left)
                else:
                    return right[0]
            else:
                if right[0] > right[1] or right[0] <= left[0]:
                    return self.findMin(right)
                else:
                    return left[0]
                
        else:
            return nums[0]
            