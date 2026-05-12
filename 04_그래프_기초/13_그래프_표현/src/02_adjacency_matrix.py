"""
Topic  : 인접 행렬 — 공간 분석, 사용 적합 케이스
Time   : O(V²) 공간
Space  : O(V²)
"""


# ── 인접 행렬 구축 ────────────────────────────────────────────────────────────

def build_matrix_undirected(
    n: int, edges: list[tuple[int, int]]
) -> list[list[int]]:
    """무방향 그래프 인접 행렬 (1-indexed).

    matrix[i][j] = 1 이면 i-j 간선 존재.
    """
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix


def build_matrix_directed(
    n: int, edges: list[tuple[int, int]]
) -> list[list[int]]:
    """방향 그래프 인접 행렬."""
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v in edges:
        matrix[u][v] = 1
    return matrix


def build_matrix_weighted(
    n: int,
    edges: list[tuple[int, int, int]],
    directed: bool = False,
    no_edge: int | float = 0,
) -> list[list[int | float]]:
    """가중 그래프 인접 행렬.

    Args:
        no_edge: 간선 없을 때의 값 (0 또는 float('inf'))
    """
    matrix: list[list[int | float]] = [
        [no_edge] * (n + 1) for _ in range(n + 1)
    ]
    for u, v, w in edges:
        matrix[u][v] = w
        if not directed:
            matrix[v][u] = w
    return matrix


# ── 출력 ─────────────────────────────────────────────────────────────────────

def print_matrix(
    matrix: list[list[int | float]], n: int, title: str = "인접 행렬"
) -> None:
    """인접 행렬 출력."""
    print(f"\n=== {title} ===")
    # 헤더
    header = "   " + " ".join(f"{j:3d}" for j in range(1, n + 1))
    print(header)
    print("   " + "----" * n)
    for i in range(1, n + 1):
        row_vals = []
        for j in range(1, n + 1):
            v = matrix[i][j]
            if v == float('inf'):
                row_vals.append("  ∞")
            else:
                row_vals.append(f"{v:3g}")
        print(f"{i:2d}|" + " ".join(row_vals))


# ── 간선 조회 O(1) ────────────────────────────────────────────────────────────

def has_edge(
    matrix: list[list[int | float]], u: int, v: int
) -> bool:
    """O(1) 간선 존재 여부 확인."""
    return matrix[u][v] != 0


def get_neighbors(
    matrix: list[list[int | float]], u: int, n: int
) -> list[int]:
    """u의 인접 노드 리스트 (O(V))."""
    return [v for v in range(1, n + 1) if matrix[u][v] != 0]


# ── 공간 분석 ────────────────────────────────────────────────────────────────

def space_analysis() -> None:
    """인접 행렬 공간 사용량 분석."""
    print("\n=== 공간 사용량 분석 ===")
    print("(Python int = 28 bytes, list overhead 제외)")
    print(f"{'V':>6}  {'V²':>10}  {'메모리(MB)':>12}")
    for v in [10, 100, 500, 1000, 5000, 10000]:
        cells = v * v
        mb = cells * 28 / 1024 / 1024
        feasible = "✅" if mb < 256 else "❌"
        print(f"{v:>6}  {cells:>10,}  {mb:>10.1f}MB  {feasible}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 무방향 그래프
    n = 5
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]

    mat = build_matrix_undirected(n, edges)
    print_matrix(mat, n, "무방향 인접 행렬")

    print(f"\n1-2 간선 존재? {has_edge(mat, 1, 2)}")
    print(f"1-4 간선 존재? {has_edge(mat, 1, 4)}")
    print(f"노드 1의 이웃: {get_neighbors(mat, 1, n)}")
    print(f"노드 4의 이웃: {get_neighbors(mat, 4, n)}")

    # 가중 방향 그래프
    INF = float('inf')
    weighted_edges = [(1, 2, 5), (1, 3, 3), (2, 4, 7), (3, 4, 2)]
    wmat = build_matrix_weighted(n, weighted_edges, directed=True, no_edge=INF)
    # 자기 자신은 0
    for i in range(1, n + 1):
        wmat[i][i] = 0
    print_matrix(wmat, n, "가중 방향 인접 행렬 (∞=없음)")

    space_analysis()

    print("\n=== 인접 행렬 vs 인접 리스트 선택 기준 ===")
    criteria = [
        ("V ≤ 1000이고 E ≈ V² (밀집)", "인접 행렬"),
        ("특정 간선 O(1) 조회 빈번", "인접 행렬"),
        ("플로이드-워셜 알고리즘", "인접 행렬"),
        ("V 크거나 E << V² (희소)", "인접 리스트"),
        ("DFS/BFS 등 일반 탐색", "인접 리스트"),
    ]
    for cond, choice in criteria:
        print(f"  {cond:45s} → {choice}")
