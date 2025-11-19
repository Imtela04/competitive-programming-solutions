class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums)==1:
            if nums[0] == val:
                nums.pop()
                return 0
            else:
                return 1
        else:
            k=0
            for i in range(len(nums)):
                if nums[k] == val:
                    nums.pop(k)
                    k -= 1
                k += 1
            return k, nums
sol = Solution()
print(sol.removeElement([0,1,2,2,3,0,4,2], 2))  