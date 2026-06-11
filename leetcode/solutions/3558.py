# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

def dfs(adj, visited, node, temp):
    visited[node] = True
    depth = temp

    for neighbour in adj[node]:
        if not visited[neighbour]:
            depth = max(depth, dfs(adj, visited, neighbour, temp + 1))

    return depth


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1

        adj_list = [[] for _ in range(n + 1)]

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        depth = dfs(adj_list, [False] * (n + 1), 1, 0)

        return pow(2, depth - 1) % (pow(10, 9) + 7)
