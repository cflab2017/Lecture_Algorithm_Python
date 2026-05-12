"""
Topic  : BFS 최단 경로 — dist 배열, 경로 재구성
Time   : O(V + E)
Space  : O(V)
"""

from collections import deque


# ── 최단 경로 거리 ────────────────────────────────────────────────────────────

def bfs_dist(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """BFS로 모든 노드까지 최단 거리 계산.

    Returns:
        dist[i] = start→i 최단 거리 (-1=도달 불가)
    """
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue: deque[int] = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                queue.append(nxt)
    return dist


# ── 경로 재구성 ───────────────────────────────────────────────────────────────

def bfs_with_parent(
    graph: list[list[int]],
    start: int,
    n: int,
) -> tuple[list[int], list[int]]:
    """BFS + 부모 배열로 경로 재구성.

    Returns:
        (dist, parent)
        parent[i] = BFS 트리에서 i의 부모 (-1이면 없음)
    """
    dist = [-1] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    queue: deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                parent[nxt] = node
                queue.append(nxt)

    return dist, parent


def reconstruct_path(parent: list[int], start: int, end: int) -> list[int]:
    """parent 배열로 start → end 경로 재구성.

    Returns:
        경로 리스트 (도달 불가이면 빈 리스트)
    """
    if parent[end] == -1 and end != start:
        return []   # 도달 불가

    path: list[int] = []
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]
    return path[::-1]


# ── 특정 목표까지 최단 거리 ──────────────────────────────────────────────────

def bfs_to_target(
    graph: list[list[int]],
    start: int,
    target: int,
    n: int,
) -> int:
    """start에서 target까지 최단 거리 (조기 종료).

    Returns:
        최단 거리 (-1이면 도달 불가)
    """
    if start == target:
        return 0
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue: deque[int] = deque([start])

    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if dist[nxt] == -1:
                dist[nxt] = dist[node] + 1
                if nxt == target:
                    return dist[nxt]
                queue.append(nxt)
    return -1


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 그래프 구축
    #  1─2─3─6
    #  │ │
    #  4─5
    n = 6
    edges = [(1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (4, 5)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("=" * 55)
    print("BFS 최단 경로")
    print("=" * 55)

    start = 1
    dist, parent = bfs_with_parent(graph, start, n)

    print(f"시작점: {start}")
    print(f"거리 배열: {dist[1:]}")

    for target in [1, 3, 5, 6]:
        path = reconstruct_path(parent, start, target)
        d = dist[target]
        print(f"  {start} → {target}: 거리={d}, 경로={path}")

    # 비연결 노드
    n2 = 5
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in [(1, 2), (3, 4)]:
        g2[u].append(v)
        g2[v].append(u)
    d2, p2 = bfs_with_parent(g2, 1, n2)
    path_to_3 = reconstruct_path(p2, 1, 3)
    print(f"\n비연결: 1 → 3 경로 = {path_to_3}  (빈 리스트 = 도달 불가)")

    # 조기 종료 테스트
    print("\n=== 조기 종료 최단 거리 ===")
    for src, dst in [(1, 6), (1, 5), (4, 6)]:
        d_fast = bfs_to_target(graph, src, dst, n)
        d_full = bfs_dist(graph, src, n)[dst]
        assert d_fast == d_full
        print(f"  {src} → {dst}: {d_fast}")
    print("정확성 검증: PASS")
