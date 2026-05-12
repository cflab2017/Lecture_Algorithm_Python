"""
백준 1753 — 최단경로
https://www.acmicpc.net/problem/1753

난이도 : Gold IV
Time  : O((V + E) log V)
Space : O(V + E)

풀이:
    방향 그래프, 단일 출발점(K) 다익스트라.
    도달 불가 정점은 "INF" 출력.
"""

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def solve() -> None:
    V, E = map(int, input().split())
    K = int(input())

    graph: list[list[tuple[int, int]]] = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    # 다익스트라
    dist = [INF] * (V + 1)
    dist[K] = 0
    heap: list[tuple[int, int]] = [(0, K)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    # 출력
    result = []
    for i in range(1, V + 1):
        result.append(str(dist[i]) if dist[i] < INF else "INF")
    print("\n".join(result))


if __name__ == "__main__":
    solve()
