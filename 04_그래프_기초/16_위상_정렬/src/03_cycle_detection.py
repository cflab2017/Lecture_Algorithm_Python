"""
Topic  : 사이클 탐지 — 위상 정렬 기반 (방향 그래프)
Time   : O(V + E)
Space  : O(V)
"""

import sys
sys.setrecursionlimit(100_000)

from collections import deque


# ── Kahn's 기반 사이클 탐지 ──────────────────────────────────────────────────

def has_cycle_kahns(n: int, graph: list[list[int]]) -> bool:
    """Kahn's 알고리즘으로 방향 그래프 사이클 탐지.

    위상 정렬 결과 길이가 V보다 작으면 사이클 존재.
    """
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    queue: deque[int] = deque(
        i for i in range(1, n + 1) if in_degree[i] == 0
    )
    visited_count = 0

    while queue:
        node = queue.popleft()
        visited_count += 1
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return visited_count < n


# ── DFS 기반 사이클 탐지 ─────────────────────────────────────────────────────

def has_cycle_dfs(n: int, graph: list[list[int]]) -> tuple[bool, list[int]]:
    """DFS 기반 사이클 탐지 및 사이클 경로 반환.

    Returns:
        (사이클 존재 여부, 사이클 노드 목록)
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * (n + 1)
    parent = [-1] * (n + 1)
    cycle: list[int] = []

    def dfs(node: int) -> bool:
        color[node] = GRAY
        for nxt in graph[node]:
            if color[nxt] == GRAY:
                # 사이클 발견 — 경로 재구성
                cycle.append(nxt)
                cur = node
                while cur != nxt:
                    cycle.append(cur)
                    cur = parent[cur]
                cycle.append(nxt)
                cycle.reverse()
                return True
            if color[nxt] == WHITE:
                parent[nxt] = node
                if dfs(nxt):
                    return True
        color[node] = BLACK
        return False

    for node in range(1, n + 1):
        if color[node] == WHITE:
            if dfs(node):
                return True, cycle

    return False, []


# ── 사이클 있는/없는 그래프 예시 ─────────────────────────────────────────────

def demo_cycle_detection() -> None:
    """다양한 그래프에서 사이클 탐지."""
    test_cases = [
        # (n, edges, 설명)
        (4, [(1, 2), (2, 3), (3, 4)], "DAG (사이클 없음)"),
        (4, [(1, 2), (2, 3), (3, 1)], "삼각형 사이클"),
        (5, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 3)], "긴 사이클"),
        (4, [(1, 2), (1, 3), (2, 4), (3, 4)], "다이아몬드 (사이클 없음)"),
        (3, [(1, 1)], "자기 루프"),
    ]

    print("=== 사이클 탐지 결과 ===")
    for n, edges, desc in test_cases:
        g: list[list[int]] = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)

        has_c_k = has_cycle_kahns(n, g)
        has_c_d, cycle_path = has_cycle_dfs(n, g)

        print(f"\n{desc}:")
        print(f"  간선: {edges}")
        print(f"  Kahn's: {'사이클 있음' if has_c_k else '사이클 없음'}")
        print(f"  DFS   : {'사이클 있음' if has_c_d else '사이클 없음'}", end="")
        if cycle_path:
            print(f"  경로: {' → '.join(map(str, cycle_path))}", end="")
        print()

        assert has_c_k == has_c_d, f"두 알고리즘 결과 불일치: {desc}"


# ── 무방향 그래프 사이클 (DFS 기반) ──────────────────────────────────────────

def has_cycle_undirected(
    n: int, graph: list[list[int]]
) -> bool:
    """무방향 그래프 사이클 탐지.

    주의: 방향 그래프와 다름 (부모 제외)
    """
    visited = [False] * (n + 1)

    def dfs(node: int, parent: int) -> bool:
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                if dfs(nxt, node):
                    return True
            elif nxt != parent:
                return True      # 부모가 아닌 이미 방문한 노드
        return False

    for node in range(1, n + 1):
        if not visited[node]:
            if dfs(node, -1):
                return True
    return False


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_cycle_detection()

    print("\n=== 무방향 그래프 사이클 탐지 ===")
    # 삼각형 (사이클 있음)
    n3 = 3
    g3: list[list[int]] = [[] for _ in range(n3 + 1)]
    for u, v in [(1, 2), (2, 3), (3, 1)]:
        g3[u].append(v)
        g3[v].append(u)
    print(f"삼각형: {has_cycle_undirected(n3, g3)}")

    # 트리 (사이클 없음)
    n4 = 4
    g4: list[list[int]] = [[] for _ in range(n4 + 1)]
    for u, v in [(1, 2), (1, 3), (2, 4)]:
        g4[u].append(v)
        g4[v].append(u)
    print(f"트리  : {has_cycle_undirected(n4, g4)}")
