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
        size = 2 * m

        # Matrix multiplication
        def multiply(A, B):
            C = [[0] * size for _ in range(size)]
            for i in range(size):
                for k in range(size):
                    if A[i][k] == 0:
                        continue
                    for j in range(size):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C

        # Matrix × Vector
        def multiply_vec(A, v):
            res = [0] * size
            for i in range(size):
                for j in range(size):
                    res[i] = (res[i] + A[i][j] * v[j]) % MOD
            return res

        # Build transition matrix
        T = [[0] * size for _ in range(size)]

        for v in range(m):
            # up[v] <- down[u] where u < v
            for u in range(v):
                T[v][m + u] = 1

            # down[v] <- up[u] where u > v
            for u in range(v + 1, m):
                T[m + v][u] = 1

        # Base state for arrays of length 2
        state = [0] * size

        for v in range(m):
            state[v] = v              # up[v]
            state[m + v] = m - 1 - v # down[v]

        power = n - 2

        while power:
            if power & 1:
                state = multiply_vec(T, state)

            T = multiply(T, T)
            power >>= 1

        return sum(state) % MOD
        
        
       
