class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target>nums[-1]:
            return len(nums) 
        elif target<nums[0]:
            return 0
   

        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i    
                elif target not in nums:
                    if nums[i]>target:
                        return i
sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))