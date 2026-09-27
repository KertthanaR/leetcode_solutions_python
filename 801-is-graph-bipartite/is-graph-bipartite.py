class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = {}

        for start in range(n):
            if start in color:
                continue
            color[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in color:
                        color[nei] = 1 - color[node]
                        queue.append(nei)
                    elif color[nei] == color[node]:
                        return False
        return True