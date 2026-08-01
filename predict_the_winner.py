class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = {}

        def solve(left, right):
            if left == right:
                return nums[left]

            if (left, right) in res:
                return res[(left, right)]

            pickLeft = nums[left] - solve(left + 1, right)
            pickRight = nums[right] - solve(left, right - 1)

            res[(left, right)] = max(pickLeft, pickRight)
            return res[(left, right)]

        return solve(0, len(nums) - 1) >= 0
        
