#two pointers approach
class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
                
        return f'{k}, nums = {nums}'
sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,2,2,2,3,3,4]))
