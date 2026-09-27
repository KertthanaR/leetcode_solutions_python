import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        graph = defaultdict(dict)
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        dist = {0: 0}
        pq = [(0, 0)]
        visited = set()

        while pq:
            d, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for nei, cnt in graph[node].items():
                nd = d + cnt + 1
                if nei not in dist or nd < dist[nei]:
                    dist[nei] = nd
                    heapq.heappush(pq, (nd, nei))

        result = sum(1 for node in dist if dist[node] <= maxMoves)

        for u, v, cnt in edges:
            a = max(0, maxMoves - dist.get(u, float('inf')))
            b = max(0, maxMoves - dist.get(v, float('inf')))
            result += min(a + b, cnt)

        return result