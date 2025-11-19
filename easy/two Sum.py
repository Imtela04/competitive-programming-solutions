class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortednums = sorted(nums)

        outlist = []

        for i in range(len(sortednums)):
          for j in sortednums[i+1:]:
              sum = sortednums[i] + j

              if sum==target:
                if sortednums[i]==j:
                  outlist.append(nums.index(sortednums[i]))
                  outlist.append(nums.index(j,nums.index(sortednums[i])+1))

                else:
                  outlist.append(nums.index(sortednums[i]))
                  outlist.append(nums.index(j))
                break

        return outlist


sol = Solution()
print(sol.twoSum([3,2,3],6))