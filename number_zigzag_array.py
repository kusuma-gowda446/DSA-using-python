class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1

        if m == 1:
            return 0

        # Length = 2
        up = [0] * m
        down = [0] * m

        for v in range(m):
            up[v] = v          # values smaller than v
            down[v] = m - 1 - v  # values larger than v

        # Build lengths 3..n
        for _ in range(3, n + 1):
            pref_down = [0] * (m + 1)
            pref_up = [0] * (m + 1)

            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD
                pref_up[i + 1] = (pref_up[i] + up[i]) % MOD

            total_up = pref_up[m]

            new_up = [0] * m
            new_down = [0] * m

            for x in range(m):
                # sum of down[y] for y < x
                new_up[x] = pref_down[x]

                # sum of up[y] for y > x
                new_down[x] = (total_up - pref_up[x + 1]) % MOD

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD
        
