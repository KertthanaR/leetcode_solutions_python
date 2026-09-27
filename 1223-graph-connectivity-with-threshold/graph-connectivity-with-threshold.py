class Solution:
    def areConnected(self, n: int, threshold: int, queries: list[list[int]]) -> list[bool]:
        parent = list(range(n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[px] = py

        for z in range(threshold + 1, n + 1):
            for multiple in range(2 * z, n + 1, z):
                union(z, multiple)

        return [find(a) == find(b) for a, b in queries]