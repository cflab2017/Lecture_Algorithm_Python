"""
백준 1916 — 최소비용 구하기
https://www.acmicpc.net/problem/1916

난이도 : Gold V
Time  : O((V + E) log V)
Space : O(V + E)

풀이:
    방향 그래프, 단일 출발-목적 최단 경로.
    출발점에서 다익스트라 실행 후 도착점 거리 출력.
"""

import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize


def solve() -> None:
    n = int(input())
    m = int(input())

    graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, end = map(int, input().split())

    # 다익스트라
    dist = [INF] * (n + 1)
    dist[start] = 0
    heap: list[tuple[int, int]] = [(0, start)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        # 목적지 도달 시 조기 종료 (선택적 최적화)
        if u == end:
            break
        for v, w in graph[u]:
            nd = dist[u] + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    print(dist[end])


if __name__ == "__main__":
    solve()
