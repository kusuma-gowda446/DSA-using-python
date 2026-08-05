class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods using DFS
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Check if any safe method calls a suspicious method
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Return all non-suspicious methods
        return [i for i in range(n) if i not in suspicious]
       
