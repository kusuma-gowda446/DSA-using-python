class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        total = 0

        for num in range(num1, num2 + 1):
            s = str(num)

            if len(s) < 3:
                continue

            for i in range(1, len(s) - 1):
                left = int(s[i - 1])
                mid = int(s[i])
                right = int(s[i + 1])

                if (mid > left and mid > right) or \
                   (mid < left and mid < right):
                    total += 1

        return total

        
