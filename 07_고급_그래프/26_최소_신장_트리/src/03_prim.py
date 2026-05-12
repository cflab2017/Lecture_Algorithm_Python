"""
단원 26 — MST: 프림 알고리즘 (Prim)
Topic : Prim's MST Algorithm using heapq
Time  : O((V + E) log V)
Space : O(V + E)

설명:
    임의 출발 정점에서 시작, MST에 인접한 최소 가중치 간선을 반복 선택.
    heapq(최소 힙)를 사용해 미방문 정점 중 최소 가중치 간선을 빠르게 선택.
    lazy deletion: 힙에서 꺼낸 정점이 이미 MST에 포함되면 건너뜀.
"""

import heapq
import sys

INF = sys.maxsize


def prim(
    graph: list[list[tuple[int, int]]],
    start: int = 0,
) -> tuple[int, list[tuple[int, int, int]]]:
    """
    프림 알고리즘으로 MST를 계산한다.

    Args:
        graph: graph[u] = [(v, weight), ...] 인접 리스트 (무방향)
        start: 시작 정점 (0-indexed)

    Returns:
        (total_weight, mst_edges)

    Time : O((V + E) log V)
    Space: O(V + E)
    """
    n = len(graph)
    in_mst = [False] * n
    total = 0
    mst_edges: list[tuple[int, int, int]] = []

    # (가중치, 현재 노드, 이전 노드)
    heap: list[tuple[int, int, int]] = [(0, start, -1)]

    while heap and len(mst_edges) < n - 1:
        w, u, prev = heapq.heappop(heap)

        if in_mst[u]:       # lazy deletion: 이미 MST에 포함
            continue

        in_mst[u] = True
        total += w

        if prev != -1:
            mst_edges.append((prev, u, w))

        # 인접 정점 중 미방문만 힙에 추가
        for v, weight in graph[u]:
            if not in_mst[v]:
                heapq.heappush(heap, (weight, v, u))

    return total, mst_edges


def build_undirected_graph(
    n: int,
    edges: list[tuple[int, int, int]],
) -> list[list[tuple[int, int]]]:
    """무방향 인접 리스트 생성. Time O(E), Space O(V+E)."""
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph


def main() -> None:
    # ── 예제 1: 기본 그래프 ──
    print("=" * 55)
    print("예제 1: 프림 MST (5개 정점)")
    print("=" * 55)

    # 노드 0~4
    # 0──4──1──2──3
    # |      \  |
    # 8       1 3
    # |          \
    # 4 ────5──── 2
    edges1 = [
        (0, 1, 4), (0, 4, 8),
        (1, 2, 2), (1, 3, 1),
        (2, 3, 3), (3, 4, 5),
    ]
    graph1 = build_undirected_graph(5, edges1)
    total1, mst1 = prim(graph1, start=0)

    print(f"MST 총 가중치: {total1}")
    print("MST 간선:")
    for u, v, w in mst1:
        print(f"  {u} -- {v}  (가중치 {w})")

    # ── 예제 2: 크루스칼과 비교 ──
    print()
    print("=" * 55)
    print("예제 2: 프림 vs 크루스칼 결과 비교")
    print("=" * 55)

    edges2 = [
        (0, 1, 7), (0, 3, 5),
        (1, 2, 8), (1, 3, 9), (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15), (3, 5, 6),
        (4, 5, 8), (4, 6, 9),
        (5, 6, 11),
    ]
    n2 = 7
    graph2 = build_undirected_graph(n2, edges2)
    total_prim, mst_prim = prim(graph2, start=0)

    # 크루스칼 (간단 구현으로 비교)
    parent = list(range(n2))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x: int, y: int) -> bool:
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        parent[ry] = rx
        return True

    sorted_e = sorted(edges2, key=lambda e: e[2])
    total_kr = 0
    for u, v, w in sorted_e:
        if union(u, v):
            total_kr += w

    print(f"  프림    MST 가중치: {total_prim}")
    print(f"  크루스칼 MST 가중치: {total_kr}")
    print(f"  결과 동일: {total_prim == total_kr}")

    # ── 예제 3: 좌표 기반 완전 그래프 (프림 유리) ──
    print()
    print("=" * 55)
    print("예제 3: 좌표 기반 완전 그래프 MST")
    print("  — 좌표 간 유클리드 거리로 가중치 설정")
    print("=" * 55)

    import math
    coords = [(0, 0), (3, 0), (6, 1), (1, 4), (4, 5)]
    m = len(coords)
    edges3 = []
    for i in range(m):
        for j in range(i + 1, m):
            x1, y1 = coords[i]
            x2, y2 = coords[j]
            dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
            edges3.append((i, j, dist))

    graph3_list: list[list[tuple[int, float]]] = [[] for _ in range(m)]
    for u, v, w in edges3:
        graph3_list[u].append((v, w))  # type: ignore[arg-type]
        graph3_list[v].append((u, w))  # type: ignore[arg-type]

    # prim 함수는 int weight 기대; float 버전 인라인
    in_mst = [False] * m
    total3 = 0.0
    heap3: list[tuple[float, int, int]] = [(0.0, 0, -1)]
    mst3: list[tuple[int, int, float]] = []

    while heap3 and len(mst3) < m - 1:
        w, u, prev = heapq.heappop(heap3)
        if in_mst[u]:
            continue
        in_mst[u] = True
        total3 += w
        if prev != -1:
            mst3.append((prev, u, w))
        for v, weight in graph3_list[u]:
            if not in_mst[v]:
                heapq.heappush(heap3, (weight, v, u))

    print(f"MST 총 거리: {total3:.4f}")
    for u, v, w in mst3:
        print(f"  {coords[u]} -- {coords[v]}  거리={w:.4f}")


if __name__ == "__main__":
    main()
