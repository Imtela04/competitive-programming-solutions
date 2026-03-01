#recursive solution
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits==[]:
            return [1]
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        else:
            plus = self.plusOne(digits[:-1])
            plus.append(0)
            return plus




            
        
sol = Solution()
print(sol.plusOne([9,9,9,9,9])) 