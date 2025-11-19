class Solution(object):
    def shorteststringlen(self,strs):
      shortest=201
      for i in strs:
        if len(i)<shortest:
          shortest=len(i)
      return shortest
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        strs.sort()


        for i in range(self.shorteststringlen(strs)):
          if strs[0][i]==strs[-1][i]:
            res+=strs[0][i]
          else:
            break

        return res
sol = Solution()
print(sol.longestCommonPrefix(["","",""]))