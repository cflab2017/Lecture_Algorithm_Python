"""
Topic  : DFS 기반 위상 정렬 — 후위 순서 역
Time   : O(V + E)
Space  : O(V) 재귀 스택
"""

import sys
sys.setrecursionlimit(100_000)


# ── DFS 위상 정렬 ─────────────────────────────────────────────────────────────

def dfs_topological_sort(
    n: int, graph: list[list[int]]
) -> list[int] | None:
    """DFS 기반 위상 정렬.

    후위(post-order) 순서의 역이 위상 정렬 순서.

    Returns:
        위상 순서, 사이클이면 None
    """
    WHITE = 0   # 미방문
    GRAY = 1    # 방문 중 (DFS 스택에 있음)
    BLACK = 2   # 완전 탐색 완료

    color = [WHITE] * (n + 1)
    post_order: list[int] = []
    has_cycle = [False]

    def dfs(node: int) -> None:
        color[node] = GRAY
        for nxt in graph[node]:
            if color[nxt] == GRAY:
                has_cycle[0] = True
                return
            if color[nxt] == WHITE:
                dfs(nxt)
                if has_cycle[0]:
                    return
        color[node] = BLACK
        post_order.append(node)

    for node in range(1, n + 1):
        if color[node] == WHITE:
            dfs(node)
            if has_cycle[0]:
                return None

    return post_order[::-1]


def dfs_topological_verbose(
    n: int, graph: list[list[int]]
) -> list[int] | None:
    """DFS 위상 정렬 단계별 출력."""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * (n + 1)
    post_order: list[int] = []
    has_cycle = [False]
    depth = [0]

    def dfs(node: int) -> None:
        color[node] = GRAY
        indent = "  " * depth[0]
        print(f"{indent}→ 노드 {node} 진입 (GRAY)")
        depth[0] += 1
        for nxt in graph[node]:
            if color[nxt] == GRAY:
                print(f"{indent}  ⚠ 사이클 발견! {nxt} → {node}")
                has_cycle[0] = True
                return
            if color[nxt] == WHITE:
                dfs(nxt)
                if has_cycle[0]:
                    return
        depth[0] -= 1
        color[node] = BLACK
        post_order.append(node)
        print(f"{indent}← 노드 {node} 완료 (BLACK), post_order={post_order}")

    for node in range(1, n + 1):
        if color[node] == WHITE:
            dfs(node)
            if has_cycle[0]:
                return None

    result = post_order[::-1]
    print(f"\npost_order    : {post_order}")
    print(f"위상 정렬 순서 : {result}")
    return result


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # DAG
    #  1 → 2 → 4
    #  1 → 3 → 4
    #         ↓
    #         5
    n = 5
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)

    print("=" * 55)
    print("DFS 기반 위상 정렬")
    print("=" * 55)
    result = dfs_topological_verbose(n, graph)

    # Kahn's 와 비교
    from collections import deque

    def kahns(n: int, graph: list[list[int]]) -> list[int]:
        in_deg = [0] * (n + 1)
        for u in range(1, n + 1):
            for v in graph[u]:
                in_deg[v] += 1
        q: deque[int] = deque(i for i in range(1, n + 1) if in_deg[i] == 0)
        res: list[int] = []
        while q:
            node = q.popleft()
            res.append(node)
            for nxt in graph[node]:
                in_deg[nxt] -= 1
                if in_deg[nxt] == 0:
                    q.append(nxt)
        return res

    kahn_result = kahns(n, graph)
    print(f"\nKahn's 결과   : {kahn_result}")
    print(f"DFS 결과      : {result}")

    # 유효성 검증 (두 결과 모두 올바른 위상 순서여야 함)
    def verify_topological(order: list[int], n: int, edges: list[tuple[int, int]]) -> bool:
        pos = {v: i for i, v in enumerate(order)}
        return all(pos[u] < pos[v] for u, v in edges)

    print(f"\nKahn's 유효성: {verify_topological(kahn_result, n, edges)}")
    print(f"DFS 유효성   : {verify_topological(result or [], n, edges)}")

    # 사이클 케이스
    print("\n=== 사이클 탐지 ===")
    n2 = 4
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in [(1, 2), (2, 3), (3, 4), (4, 2)]:  # 2→3→4→2 사이클
        g2[u].append(v)
    result2 = dfs_topological_sort(n2, g2)
    print(f"사이클 그래프 결과: {result2}  (None이면 사이클)")
