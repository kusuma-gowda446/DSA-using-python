class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            ans = cnt[1]
            if ans % 2 == 0:
                ans -= 1

        # Check all other numbers
        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt.get(cur, 0) >= 2:
                length += 2
                if cur * cur > 10**18:  # avoid extremely large numbers
                    break
                cur *= cur

            if cnt.get(cur, 0) >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
        
