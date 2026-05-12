"""
백준 4386 — 별자리 만들기
https://www.acmicpc.net/problem/4386

난이도 : Gold III
Time  : O(N² log N)  N ≤ 100
Space : O(N²)

풀이:
    N개 별 좌표 → 완전 그래프 구성 (E = N*(N-1)/2)
    프림 알고리즘으로 MST 계산 (좌표 기반 밀집 그래프에 적합).
    출력: 소수점 2자리.
"""

import heapq
import math
import sys

input = sys.stdin.readline


def solve() -> None:
    N = int(input())
    stars: list[tuple[float, float]] = []
    for _ in range(N):
        x, y = map(float, input().split())
        stars.append((x, y))

    # 인접 리스트 생성 (완전 그래프)
    graph: list[list[tuple[float, int]]] = [[] for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = stars[i]
            x2, y2 = stars[j]
            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            graph[i].append((dist, j))
            graph[j].append((dist, i))

    # 프림 MST
    in_mst = [False] * N
    total = 0.0
    # (거리, 현재 노드)
    heap: list[tuple[float, int]] = [(0.0, 0)]

    while heap:
        d, u = heapq.heappop(heap)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total += d
        for w, v in graph[u]:
            if not in_mst[v]:
                heapq.heappush(heap, (w, v))

    print(f"{total:.2f}")


if __name__ == "__main__":
    solve()
