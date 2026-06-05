class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def solve(n):
            if n < 0:
                return 0

            s = str(n)
            memo = {}

            def dp(pos, tight, started, a, b):
                key = (pos, tight, started, a, b)

                if key in memo:
                    return memo[key]

                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(pos + 1, ntight, False, -1, -1)

                    elif not started:
                        cnt, wav = dp(pos + 1, ntight, True, -1, d)

                    else:
                        add = 0
                        if a != -1 and (
                            (b > a and b > d) or
                            (b < a and b < d)
                        ):
                            add = 1

                        cnt, wav = dp(pos + 1, ntight, True, b, d)
                        wav += add * cnt

                    total_cnt += cnt
                    total_wavy += wav

                memo[key] = (total_cnt, total_wavy)
                return memo[key]

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)
        
