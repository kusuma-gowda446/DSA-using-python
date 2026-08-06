class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            p = 1

            for digit in str(n):
                p *= int(digit)

            if p % t == 0:
                return n

            n += 1
        
