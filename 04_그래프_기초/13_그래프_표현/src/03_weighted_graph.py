"""
Topic  : 가중 그래프 표현 — 인접 리스트와 간선 표현
Time   : O(V + E) 공간
Space  : O(V + E)
"""

from collections import defaultdict
from dataclasses import dataclass


# ── 가중 인접 리스트 (튜플) ───────────────────────────────────────────────────

def build_weighted_list(
    n: int,
    edges: list[tuple[int, int, int]],
    directed: bool = False,
) -> list[list[tuple[int, int]]]:
    """가중 그래프 인접 리스트.

    graph[u] = [(v, weight), ...]
    """
    graph: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))
    return graph


# ── 간선 클래스 ───────────────────────────────────────────────────────────────

@dataclass
class Edge:
    u: int
    v: int
    weight: int

    def __repr__(self) -> str:
        return f"Edge({self.u}→{self.v}, w={self.weight})"

    def reversed(self) -> "Edge":
        return Edge(self.v, self.u, self.weight)


def build_edge_list(
    edges_raw: list[tuple[int, int, int]]
) -> list[Edge]:
    """Edge 객체 리스트."""
    return [Edge(u, v, w) for u, v, w in edges_raw]


# ── 간선 기반 인접 리스트 ────────────────────────────────────────────────────

def build_graph_from_edges(
    n: int, edge_list: list[Edge], directed: bool = False
) -> dict[int, list[Edge]]:
    """Edge 객체를 이용한 인접 리스트."""
    graph: dict[int, list[Edge]] = defaultdict(list)
    for edge in edge_list:
        graph[edge.u].append(edge)
        if not directed:
            graph[edge.v].append(edge.reversed())
    return dict(graph)


# ── 출력 ────────────────────────────────────────────────────────────────────

def print_weighted_graph(
    graph: list[list[tuple[int, int]]],
    title: str = "가중 그래프",
) -> None:
    """가중 인접 리스트 출력."""
    print(f"\n=== {title} ===")
    for i in range(1, len(graph)):
        if graph[i]:
            neighbors = ", ".join(f"{v}(w={w})" for v, w in graph[i])
            print(f"  {i}: [{neighbors}]")


# ── 통계 ────────────────────────────────────────────────────────────────────

def graph_stats(
    graph: list[list[tuple[int, int]]]
) -> None:
    """가중 그래프 통계."""
    n = len(graph) - 1
    all_weights = [w for adj in graph[1:] for _, w in adj]
    if not all_weights:
        return
    print(f"\n  노드 수: {n}")
    print(f"  간선 수(방향 기준): {len(all_weights)}")
    print(f"  최소 가중치: {min(all_weights)}")
    print(f"  최대 가중치: {max(all_weights)}")
    print(f"  평균 가중치: {sum(all_weights)/len(all_weights):.1f}")


# ── 다익스트라 준비 확인 ──────────────────────────────────────────────────────

def check_negative_weights(
    graph: list[list[tuple[int, int]]]
) -> bool:
    """음수 가중치 여부 확인 (다익스트라 사용 가능 여부)."""
    for adj in graph[1:]:
        for _, w in adj:
            if w < 0:
                return True
    return False


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 가중 무방향 그래프
    #  1 --5-- 2
    #  |       |
    #  3       7
    #  |
    #  1 --2-- 3 --1-- 4
    n = 5
    weighted_edges = [
        (1, 2, 5),
        (1, 3, 3),
        (2, 4, 7),
        (3, 4, 2),
        (3, 5, 8),
        (4, 5, 1),
    ]

    g = build_weighted_list(n, weighted_edges)
    print_weighted_graph(g, "가중 무방향 그래프")
    print("통계:")
    graph_stats(g)
    print(f"음수 가중치 있음? {check_negative_weights(g)}")

    # 가중 방향 그래프
    directed_weighted = [
        (1, 2, 10),
        (1, 3, 3),
        (2, 4, 2),
        (3, 2, 4),
        (3, 4, 8),
        (4, 5, 5),
    ]
    g_dir = build_weighted_list(n, directed_weighted, directed=True)
    print_weighted_graph(g_dir, "가중 방향 그래프")

    # Edge 객체 사용
    print("\n=== Edge 객체 방식 ===")
    edges = build_edge_list(weighted_edges)
    g_edge = build_graph_from_edges(n, edges)
    for node in sorted(g_edge):
        print(f"  {node}: {[str(e) for e in g_edge[node]]}")

    # 다익스트라 전형 코드 패턴
    print("\n=== 다익스트라 준비 패턴 ===")
    print("import heapq")
    print("dist = [float('inf')] * (n + 1)")
    print("dist[start] = 0")
    print("heap = [(0, start)]  # (거리, 노드)")
    print("while heap:")
    print("    d, u = heapq.heappop(heap)")
    print("    for v, w in graph[u]:")
    print("        if dist[u] + w < dist[v]:")
    print("            dist[v] = dist[u] + w")
    print("            heapq.heappush(heap, (dist[v], v))")
