"""
백준 1260 – DFS와 BFS
https://www.acmicpc.net/problem/1260
Time  : O((V + E) log V)
Space : O(V + E)
"""

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def main() -> None:
    n, m, v = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        graph[i].sort()

    # DFS
    visited_dfs = [False] * (n + 1)
    dfs_result: list[int] = []

    def dfs(node: int) -> None:
        visited_dfs[node] = True
        dfs_result.append(node)
        for nxt in graph[node]:
            if not visited_dfs[nxt]:
                dfs(nxt)

    dfs(v)
    print(' '.join(map(str, dfs_result)))

    # BFS
    visited_bfs = [False] * (n + 1)
    queue: deque[int] = deque([v])
    visited_bfs[v] = True
    bfs_result: list[int] = []

    while queue:
        node = queue.popleft()
        bfs_result.append(node)
        for nxt in graph[node]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)

    print(' '.join(map(str, bfs_result)))


if __name__ == "__main__":
    main()
