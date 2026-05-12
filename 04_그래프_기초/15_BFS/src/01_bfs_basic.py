"""
Topic  : BFS 기본 — 탐색 순서, 거리 배열
Time   : O(V + E)
Space  : O(V)
"""

from collections import deque


# ── 기본 BFS ─────────────────────────────────────────────────────────────────

def bfs(
    graph: list[list[int]],
    start: int,
    n: int,
) -> tuple[list[int], list[int]]:
    """BFS 탐색.

    Returns:
        (방문 순서, 최단 거리 배열)
        dist[i] = start → i 최단 거리 (-1이면 도달 불가)
    """
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue: deque[int] = deque([start])
    order: list[int] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)

    return order, dist


def bfs_verbose(
    graph: list[list[int]],
    start: int,
    n: int,
) -> None:
    """BFS 레이어별 출력."""
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue: deque[int] = deque([start])
    layer = 0

    print(f"레이어 {layer}: [{start}]  (거리 0)")
    while queue:
        next_layer: list[int] = []
        for _ in range(len(queue)):    # 현재 레이어 노드 모두 처리
            node = queue.popleft()
            for nxt in graph[node]:
                if dist[nxt] == -1:
                    dist[nxt] = dist[node] + 1
                    queue.append(nxt)
                    next_layer.append(nxt)
        if next_layer:
            layer += 1
            print(f"레이어 {layer}: {next_layer}  (거리 {layer})")


# ── BFS vs DFS 비교 ───────────────────────────────────────────────────────────

def dfs_order(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """DFS 방문 순서 (비교용)."""
    visited = [False] * (n + 1)
    order: list[int] = []

    def _dfs(node: int) -> None:
        visited[node] = True
        order.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                _dfs(nxt)

    _dfs(start)
    return order


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 트리 구조 그래프
    #        1
    #       /|\
    #      2 3 4
    #     /|   |
    #    5 6   7
    n = 7
    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (4, 7)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("=" * 55)
    print("BFS vs DFS 방문 순서 비교")
    print("=" * 55)
    bfs_order, dist = bfs(graph, 1, n)
    dfs_ord = dfs_order(graph, 1, n)

    print(f"BFS 순서: {bfs_order}")
    print(f"DFS 순서: {dfs_ord}")
    print(f"최단 거리: {dist[1:]}")

    print("\n=== BFS 레이어별 탐색 ===")
    bfs_verbose(graph, 1, n)

    # 선형 그래프
    print("\n=== 선형 그래프 1─2─3─4─5 ===")
    n2 = 5
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for i in range(1, n2):
        g2[i].append(i + 1)
        g2[i + 1].append(i)
    bfs_ord2, dist2 = bfs(g2, 1, n2)
    print(f"BFS 순서: {bfs_ord2}")
    print(f"거리 배열: {dist2[1:]}")

    # 비연결 그래프
    print("\n=== 비연결 그래프 ===")
    #  1─2  3─4  5(고립)
    n3 = 5
    g3: list[list[int]] = [[] for _ in range(n3 + 1)]
    for u, v in [(1, 2), (3, 4)]:
        g3[u].append(v)
        g3[v].append(u)
    _, dist3 = bfs(g3, 1, n3)
    print(f"시작=1 거리: {dist3[1:]}")
    print("  -1 = 도달 불가")

    # 거리 기반 레이어 출력
    print("\n=== 거리별 노드 ===")
    for d in range(max(x for x in dist if x >= 0) + 1):
        nodes = [i for i in range(1, n + 1) if dist[i] == d]
        print(f"  거리 {d}: {nodes}")
