#beaten 100% of submissions
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romdict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}


        sub = 0
        if 'IV' in s or 'IX' in s:
          sub+=2
        if 'XL' in s or 'XC' in s:
          sub+=20
        if 'CD' in s or 'CM' in s:
          sub+=200

        num = 0
        for i in range(len(s)-1,-1,-1):
          num+=romdict[s[i]]
        num-=sub

        return num
sol = Solution()
print(sol.romanToInt('LVIII'))

