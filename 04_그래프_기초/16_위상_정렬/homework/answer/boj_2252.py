"""
백준 2252 – 줄 세우기
https://www.acmicpc.net/problem/2252
Time  : O(V + E)
Space : O(V + E)

전략: Kahn's 위상 정렬
"""

import sys
from collections import deque

input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    queue: deque[int] = deque(
        i for i in range(1, n + 1) if in_degree[i] == 0
    )
    result: list[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main()
