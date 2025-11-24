#beats 100%
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))