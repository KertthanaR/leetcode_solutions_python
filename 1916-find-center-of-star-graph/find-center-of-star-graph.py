class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        a, b = edges[0]
        c, d = edges[1]
        return a if a in (c, d) else b