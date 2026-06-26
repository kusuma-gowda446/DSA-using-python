class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        arr = [1 if x == target else -1 for x in nums]

        prefix = [0]
        s = 0
        for x in arr:
            s += x
            prefix.append(s)

        
        vals = sorted(set(prefix))
        mp = {v: i + 1 for i, v in enumerate(vals)}

        m = len(vals) + 2
        bit = [0] * m

        def update(i):
            while i < m:
                bit[i] += 1
                i += i & -i

        def query(i):
            ans = 0
            while i > 0:
                ans += bit[i]
                i -= i & -i
            return ans

        ans = 0
        for p in prefix:
            r = mp[p]
            ans += query(r - 1)   
            update(r)

        return ans
       
