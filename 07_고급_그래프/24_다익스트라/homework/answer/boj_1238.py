"""
백준 1238 — 파티
https://www.acmicpc.net/problem/1238

난이도 : Gold III
Time  : O((N + M) log N)  — 다익스트라 2회
Space : O(N + M)

풀이:
    i번 학생의 왕복 거리 = dist_to_X[i] + dist_from_X[i]

    dist_from_X: 정방향 그래프에서 X를 출발점으로 다익스트라 1회
    dist_to_X  : 역방향 그래프에서 X를 출발점으로 다익스트라 1회
                 (역방향의 X→i 거리 = 정방향의 i→X 거리)

    역방향 그래프 기법: 간선 (a, b, t) → (b, a, t) 로 뒤집기
"""

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(
    graph: list[list[tuple[int, int]]],
    src: int,
    n: int,
) -> list[int]:
    """
    graph 에서 src 출발 최단 거리 배열 반환.

    Time : O((N + M) log N)
    Space: O(N + M)
    """
    dist = [INF] * (n + 1)
    dist[src] = 0
    heap: list[tuple[int, int]] = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist


def solve() -> None:
    N, M, X = map(int, input().split())

    graph_fwd: list[list[tuple[int, int]]] = [[] for _ in range(N + 1)]
    graph_rev: list[list[tuple[int, int]]] = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, t = map(int, input().split())
        graph_fwd[a].append((b, t))   # 정방향
        graph_rev[b].append((a, t))   # 역방향 (b→a 뒤집기)

    # X → 모든 학생 최단 거리 (정방향)
    dist_from_x = dijkstra(graph_fwd, X, N)

    # 모든 학생 → X 최단 거리 = 역방향 그래프에서 X → i 거리
    dist_to_x = dijkstra(graph_rev, X, N)

    # 왕복 거리 최댓값
    ans = max(dist_to_x[i] + dist_from_x[i] for i in range(1, N + 1))
    print(ans)


if __name__ == "__main__":
    solve()
