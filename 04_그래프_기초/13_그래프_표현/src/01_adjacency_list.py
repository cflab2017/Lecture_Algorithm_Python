"""
Topic  : 인접 리스트 — dict 및 list-of-lists, 방향/무방향
Time   : O(V + E) 공간
Space  : O(V + E)
"""

from collections import defaultdict


# ── 리스트 기반 인접 리스트 ───────────────────────────────────────────────────

def build_undirected_list(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """무방향 그래프 인접 리스트 (1-indexed).

    Args:
        n: 노드 수 (1~n)
        edges: (u, v) 쌍의 리스트
    """
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    # 양방향 추가
    return graph


def build_directed_list(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """방향 그래프 인접 리스트 (1-indexed)."""
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)    # u → v 방향만
    return graph


# ── 딕셔너리 기반 인접 리스트 ────────────────────────────────────────────────

def build_graph_dict(
    edges: list[tuple[int, int]],
    directed: bool = False,
) -> dict[int, list[int]]:
    """defaultdict 기반 인접 리스트.

    노드 번호가 불연속이거나 문자열일 때 유리.
    """
    graph: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return dict(graph)


# ── 출력 ─────────────────────────────────────────────────────────────────────

def print_graph(graph: list[list[int]], title: str = "그래프") -> None:
    """인접 리스트 출력."""
    print(f"\n=== {title} ===")
    for i, neighbors in enumerate(graph):
        if i == 0:
            continue    # 1-indexed이므로 0 건너뜀
        print(f"  {i}: {neighbors}")


def print_graph_dict(
    graph: dict[int, list[int]], title: str = "그래프"
) -> None:
    """딕셔너리 인접 리스트 출력."""
    print(f"\n=== {title} ===")
    for node in sorted(graph):
        print(f"  {node}: {sorted(graph[node])}")


# ── 그래프 정보 ───────────────────────────────────────────────────────────────

def graph_info(graph: list[list[int]]) -> None:
    """그래프 기본 정보 출력."""
    n = len(graph) - 1
    edge_count = sum(len(adj) for adj in graph[1:])
    print(f"  노드 수: {n}")
    print(f"  간선 수(방향 기준): {edge_count}")
    degrees = [len(graph[i]) for i in range(1, n + 1)]
    print(f"  최대 차수: {max(degrees)}, 최소 차수: {min(degrees)}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 예시 무방향 그래프
    #    1 --- 2
    #    |     |
    #    3 --- 4 --- 5
    n = 5
    undirected_edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

    g_und = build_undirected_list(n, undirected_edges)
    print_graph(g_und, "무방향 그래프")
    print("정보:")
    graph_info(g_und)

    # 방향 그래프
    #    1 → 2 → 4
    #    ↓       ↑
    #    3 ──────┘
    directed_edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    g_dir = build_directed_list(n, directed_edges)
    print_graph(g_dir, "방향 그래프")
    print("정보:")
    graph_info(g_dir)

    # 딕셔너리 방식 (문자열 노드)
    str_edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
    g_str: dict[str, list[str]] = defaultdict(list)
    for u, v in str_edges:
        g_str[u].append(v)
        g_str[v].append(u)
    print("\n=== 문자열 노드 그래프 ===")
    for node in sorted(g_str):
        print(f"  {node}: {sorted(g_str[node])}")

    # 공간 복잡도 확인
    print("\n=== 공간 복잡도 비교 ===")
    for v, e in [(10, 15), (100, 200), (1000, 3000)]:
        list_size = v + e      # O(V + E)
        matrix_size = v * v    # O(V²)
        print(f"V={v:>5}, E={e:>5}: "
              f"인접리스트 O({list_size:>7,}), "
              f"인접행렬 O({matrix_size:>10,})")
