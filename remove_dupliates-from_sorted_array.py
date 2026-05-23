class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        k = []

        for i in range(len(nums)):
            if nums[i] not in k:
                k.append(nums[i])

        for i in range(len(k)):
            nums[i] = k[i]

        return len(k)
