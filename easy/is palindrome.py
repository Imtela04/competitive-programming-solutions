class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xlist = [int(y) for y in str(x)]

        for i in range(len(xlist)//2):
          if xlist[i]!=xlist[len(xlist)-1-i]:
            return False
        return True
sol = Solution()
print(sol.isPalindrome(121))

# better soln

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x!=0 and x%10==0):
          return False
        half = 0
        while x>half:
          half = half*10 + x%10
          x = x//10
        return x == half or x == half//10
sol = Solution()
print(sol.isPalindrome(121))
