class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return[1]
        if (digits[-1]<9):
            digits[-1]+=1
            return digits
        else:
            digits[-1]=0
        return self.plusOne(digits[:-1])+[0]
