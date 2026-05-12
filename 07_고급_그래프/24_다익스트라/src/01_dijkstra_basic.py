"""
단원 24 — 다익스트라: 기본 구현
Topic : Dijkstra's Algorithm (Basic)
Time  : O((V + E) log V)
Space : O(V + E)

설명:
    heapq를 이용한 우선순위 큐 기반 다익스트라.
    단일 출발점에서 모든 노드까지의 최단 거리를 구한다.
    음수 가중치가 없는 그래프에서만 동작한다.
"""

import heapq
import sys

INF = sys.maxsize


def dijkstra(graph: list[list[tuple[int, int]]], src: int) -> list[int]:
    """
    단일 출발점 최단 경로를 반환한다.

    Args:
        graph: graph[u] = [(v, weight), ...] 형태의 인접 리스트
        src  : 출발 노드 (0-indexed)

    Returns:
        dist[v] = src 에서 v 까지의 최단 거리 (도달 불가면 INF)

    Time : O((V + E) log V)
    Space: O(V + E)
    """
    n = len(graph)
    dist = [INF] * n
    dist[src] = 0

    # (거리, 노드) 형태로 힙에 삽입
    heap: list[tuple[int, int]] = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)

        # Lazy Deletion: 이미 더 짧은 거리로 처리된 노드는 스킵
        if d > dist[u]:
            continue

        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


def build_graph(n: int, edges: list[tuple[int, int, int]],
                directed: bool = False) -> list[list[tuple[int, int]]]:
    """
    간선 목록으로 인접 리스트를 생성한다.

    Args:
        n       : 노드 수 (0-indexed: 0 ~ n-1)
        edges   : (u, v, weight) 목록
        directed: True이면 방향 그래프, False이면 무방향 그래프

    Time : O(E)
    Space: O(V + E)
    """
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph


def main() -> None:
    # ── 예제 1: 강의 본문 예제 그래프 (1-indexed → 0-indexed 변환) ──
    # 노드: 1~6 → 0~5
    # 간선: (u, v, w) (무방향)
    edges_ex1 = [
        (0, 1, 2),   # 1-2
        (0, 2, 1),   # 1-3
        (1, 2, 3),   # 2-3
        (1, 3, 5),   # 2-4
        (1, 4, 4),   # 2-5
        (2, 4, 1),   # 3-5
        (3, 5, 6),   # 4-6
        (4, 5, 2),   # 5-6
    ]
    graph1 = build_graph(6, edges_ex1, directed=False)
    dist1 = dijkstra(graph1, src=0)

    print("=" * 50)
    print("예제 1: 강의 본문 그래프 (출발: 노드 1)")
    print("=" * 50)
    for i, d in enumerate(dist1):
        label = str(d) if d < INF else "도달불가"
        print(f"  노드 1 → 노드 {i + 1}: {label}")

    # ── 예제 2: 방향 그래프 ──
    print()
    print("=" * 50)
    print("예제 2: 방향 그래프 (출발: 노드 0)")
    print("=" * 50)
    edges_ex2 = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
    ]
    graph2 = build_graph(4, edges_ex2, directed=True)
    dist2 = dijkstra(graph2, src=0)
    node_names = ["A", "B", "C", "D"]
    for i, d in enumerate(dist2):
        label = str(d) if d < INF else "도달불가"
        print(f"  A → {node_names[i]}: {label}")

    # ── 예제 3: 도달 불가 노드 포함 ──
    print()
    print("=" * 50)
    print("예제 3: 도달 불가 노드 포함")
    print("=" * 50)
    edges_ex3 = [(0, 1, 3), (1, 2, 2)]
    graph3 = build_graph(5, edges_ex3, directed=True)  # 노드 3, 4 도달 불가
    dist3 = dijkstra(graph3, src=0)
    for i, d in enumerate(dist3):
        label = str(d) if d < INF else "INF (도달불가)"
        print(f"  0 → {i}: {label}")


if __name__ == "__main__":
    main()
