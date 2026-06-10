class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        import heapq

class SparseTable:
    def __init__(self, nums):
        n = len(nums)

        self.log = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log[i] = self.log[i // 2] + 1

        m = self.log[n] + 1

        self.mx = [[0] * m for _ in range(n)]
        self.mn = [[0] * m for _ in range(n)]

        for i in range(n):
            self.mx[i][0] = nums[i]
            self.mn[i][0] = nums[i]

        j = 1
        while (1 << j) <= n:
            length = 1 << j
            half = length >> 1

            for i in range(n - length + 1):
                self.mx[i][j] = max(
                    self.mx[i][j - 1],
                    self.mx[i + half][j - 1]
                )
                self.mn[i][j] = min(
                    self.mn[i][j - 1],
                    self.mn[i + half][j - 1]
                )

            j += 1

    def query(self, l, r):
        k = self.log[r - l + 1]

        mx = max(
            self.mx[l][k],
            self.mx[r - (1 << k) + 1][k]
        )

        mn = min(
            self.mn[l][k],
            self.mn[r - (1 << k) + 1][k]
        )

        return mx - mn


class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        st = SparseTable(nums)

        heap = []

        for l in range(n):
            val = st.query(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)

            ans += -val

            if r > l:
                nxt = st.query(l, r - 1)
                heapq.heappush(heap, (-nxt, l, r - 1))

        return ans
       
