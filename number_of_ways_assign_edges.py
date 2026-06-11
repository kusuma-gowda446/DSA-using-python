class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        depth = 0
        stack = [(1, 0, -1)]  # node, depth, parent

        while stack:
            node, d, par = stack.pop()
            depth = max(depth, d)

            for nei in g[node]:
                if nei != par:
                    stack.append((nei, d + 1, node))

        if depth == 0:
            return 0

        return pow(2, depth - 1, MOD)
        
