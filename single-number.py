class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[]
        for i in nums:
            if i not in num:
                num.append(i)
            else:
                num.remove(i)
        return num[0]

                        
