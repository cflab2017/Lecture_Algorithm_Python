"""
단원 24 — 다익스트라: 경로 복원 (Path Reconstruction)
Topic : Dijkstra with Path Reconstruction
Time  : O((V + E) log V)
Space : O(V + E)

설명:
    prev[] 배열을 함께 관리하여, 최단 경로를 역추적한다.
    dist[v] 를 갱신할 때마다 prev[v] = u 로 기록한다.
    목적지에서 출발지까지 prev를 따라가면 최단 경로를 얻는다.
"""

import heapq
import sys

INF = sys.maxsize


def dijkstra_with_path(
    graph: list[list[tuple[int, int]]],
    src: int,
) -> tuple[list[int], list[int]]:
    """
    최단 거리 + 경로 복원 정보를 반환한다.

    Args:
        graph: graph[u] = [(v, weight), ...] 인접 리스트
        src  : 출발 노드 (0-indexed)

    Returns:
        (dist, prev)
        dist[v] : src → v 최단 거리
        prev[v] : 최단 경로에서 v 의 직전 노드 (-1 이면 없음)

    Time : O((V + E) log V)
    Space: O(V + E)
    """
    n = len(graph)
    dist = [INF] * n
    prev = [-1] * n          # 경로 복원용: prev[v] = v 직전 노드
    dist[src] = 0

    heap: list[tuple[int, int]] = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:      # lazy deletion
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u  # ← 경로 기록
                heapq.heappush(heap, (new_dist, v))

    return dist, prev


def reconstruct_path(prev: list[int], src: int, dst: int) -> list[int]:
    """
    prev 배열을 역추적하여 src → dst 경로를 반환한다.

    Args:
        prev: dijkstra_with_path 에서 반환된 prev 배열
        src : 출발 노드
        dst : 목적 노드

    Returns:
        src → dst 최단 경로 노드 목록 (도달 불가면 빈 리스트)

    Time : O(V)  (경로 길이 ≤ V)
    Space: O(V)
    """
    if prev[dst] == -1 and dst != src:
        return []   # 도달 불가

    path: list[int] = []
    cur = dst
    while cur != -1:
        path.append(cur)
        cur = prev[cur]

    path.reverse()
    return path


def main() -> None:
    # ── 예제 그래프 (무방향) ──
    # 노드: 0=A, 1=B, 2=C, 3=D, 4=E
    #
    #   A --4-- B --2-- D
    #   |      /        |
    #   2    1          3
    #   |  /            |
    #   C ------3------ E
    #
    n = 5
    edges = [
        (0, 1, 4),  # A-B
        (0, 2, 2),  # A-C
        (1, 2, 1),  # B-C
        (1, 3, 2),  # B-D
        (2, 4, 3),  # C-E
        (3, 4, 3),  # D-E
    ]

    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    names = ["A", "B", "C", "D", "E"]
    src = 0   # 출발: A

    dist, prev = dijkstra_with_path(graph, src)

    print("=" * 55)
    print(f"출발점: {names[src]}")
    print("=" * 55)
    print(f"{'목적지':>5} {'최단거리':>8}  {'경로'}")
    print("-" * 55)

    for dst in range(n):
        d = dist[dst] if dist[dst] < INF else "INF"
        path = reconstruct_path(prev, src, dst)
        path_str = " → ".join(names[p] for p in path) if path else "도달불가"
        print(f"  {names[src]} → {names[dst]}  {str(d):>6}    {path_str}")

    # ── 특정 경로 상세 출력 ──
    print()
    print("=" * 55)
    print("A → E 경로 상세")
    print("=" * 55)
    path_ae = reconstruct_path(prev, 0, 4)
    print(f"경로  : {' → '.join(names[p] for p in path_ae)}")
    print(f"거리  : {dist[4]}")
    print()

    # ── 도달 불가 케이스 ──
    print("=" * 55)
    print("도달 불가 테스트 (고립 노드 포함)")
    print("=" * 55)
    graph2: list[list[tuple[int, int]]] = [[] for _ in range(3)]
    graph2[0].append((1, 5))  # 노드 2는 고립
    dist2, prev2 = dijkstra_with_path(graph2, 0)
    path2 = reconstruct_path(prev2, 0, 2)
    print(f"0 → 2: 거리={dist2[2]}, 경로={path2 if path2 else '도달불가'}")


if __name__ == "__main__":
    main()
