class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        if (len(s) == 0) or (s[0]==')'or s[0]==']' or s[0]=='}') or (len(s)%2!=0):
            return False

        for i in s:
          if i== '(' or i== '[' or i== '{':
            stack.append(i)
          elif (len(stack)==0):
            return False
          else:
            top=stack.pop()
            if i==')'and top!='(':
                return False
            if i==']'and top!='[':
                return False
            if i=='}'and top!='{':
                return False

        return len(stack) == 0




sol = Solution()
print(sol.isValid("[{}]"))