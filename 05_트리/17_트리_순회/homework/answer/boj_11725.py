# 백준 11725 — 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725
# Time: O(n)   Space: O(n)

import sys
from collections import deque

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    graph: list[list[int]] = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)
    visited = [False] * (n + 1)

    # BFS: 루트(1)에서 시작
    queue: deque[int] = deque([1])
    visited[1] = True

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = node
                queue.append(neighbor)

    # 2번부터 n번 노드의 부모 출력
    result = [str(parent[i]) for i in range(2, n + 1)]
    sys.stdout.write("\n".join(result) + "\n")


solve()
