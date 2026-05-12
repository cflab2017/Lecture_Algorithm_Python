"""
백준 2606 – 바이러스
https://www.acmicpc.net/problem/2606
Time  : O(V + E)
Space : O(V + E)
"""

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main() -> None:
    n = int(input())
    m = int(input())
    graph: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    count = [0]

    def dfs(node: int) -> None:
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                count[0] += 1
                dfs(nxt)

    dfs(1)
    print(count[0])


if __name__ == "__main__":
    main()
