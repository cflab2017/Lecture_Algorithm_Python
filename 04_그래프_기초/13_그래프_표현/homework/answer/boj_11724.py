"""
백준 11724 – 연결 요소의 개수
https://www.acmicpc.net/problem/11724
Time  : O(V + E)
Space : O(V + E)
"""

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def main() -> None:
    n, m = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    count = 0

    def bfs(start: int) -> None:
        queue: deque[int] = deque([start])
        visited[start] = True
        while queue:
            node = queue.popleft()
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    queue.append(nxt)

    for node in range(1, n + 1):
        if not visited[node]:
            bfs(node)
            count += 1

    print(count)


if __name__ == "__main__":
    main()
