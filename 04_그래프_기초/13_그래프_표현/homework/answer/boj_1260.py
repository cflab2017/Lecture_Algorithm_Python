"""
백준 1260 – DFS와 BFS
https://www.acmicpc.net/problem/1260
Time  : O((V + E) log V)  (정렬 포함)
Space : O(V + E)
"""

import sys
from collections import deque

input = sys.stdin.readline


def main() -> None:
    n, m, v = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # 번호 작은 것부터 방문하기 위해 정렬
    for i in range(1, n + 1):
        graph[i].sort()

    # DFS (재귀)
    visited_dfs = [False] * (n + 1)
    dfs_order: list[int] = []

    def dfs(node: int) -> None:
        visited_dfs[node] = True
        dfs_order.append(node)
        for nxt in graph[node]:
            if not visited_dfs[nxt]:
                dfs(nxt)

    dfs(v)
    print(' '.join(map(str, dfs_order)))

    # BFS
    visited_bfs = [False] * (n + 1)
    queue: deque[int] = deque([v])
    visited_bfs[v] = True
    bfs_order: list[int] = []

    while queue:
        node = queue.popleft()
        bfs_order.append(node)
        for nxt in graph[node]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)

    print(' '.join(map(str, bfs_order)))


if __name__ == "__main__":
    main()
