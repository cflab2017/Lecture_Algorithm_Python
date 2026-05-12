"""
Topic  : 재귀 DFS 템플릿 — 방문 순서, 트리/그래프
Time   : O(V + E)
Space  : O(V) 재귀 스택
"""

import sys
sys.setrecursionlimit(100_000)


# ── 기본 재귀 DFS ─────────────────────────────────────────────────────────────

def dfs(
    graph: list[list[int]],
    node: int,
    visited: list[bool],
    order: list[int],
) -> None:
    """재귀 DFS.

    Args:
        graph: 인접 리스트 (1-indexed)
        node: 현재 노드
        visited: 방문 여부
        order: 방문 순서 기록
    """
    visited[node] = True
    order.append(node)
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(graph, nxt, visited, order)


def dfs_with_depth(
    graph: list[list[int]],
    node: int,
    visited: list[bool],
    depth: int = 0,
) -> None:
    """DFS를 들여쓰기로 시각화."""
    visited[node] = True
    indent = "  " * depth
    print(f"{indent}→ 노드 {node} 방문 (깊이={depth})")
    for nxt in sorted(graph[node]):
        if not visited[nxt]:
            dfs_with_depth(graph, nxt, visited, depth + 1)
    print(f"{indent}← 노드 {node} 복귀")


# ── 전처리/후처리 DFS ─────────────────────────────────────────────────────────

def dfs_pre_post(
    graph: list[list[int]],
    node: int,
    visited: list[bool],
    pre: list[int],
    post: list[int],
) -> None:
    """전위(pre-order) 및 후위(post-order) 기록.

    후위 순서의 역: 위상 정렬에 사용됨.
    """
    visited[node] = True
    pre.append(node)
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs_pre_post(graph, nxt, visited, pre, post)
    post.append(node)


# ── 연결 여부 확인 ────────────────────────────────────────────────────────────

def is_reachable(
    graph: list[list[int]], src: int, dst: int, n: int
) -> bool:
    """src에서 dst까지 도달 가능한가?"""
    visited = [False] * (n + 1)
    order: list[int] = []
    dfs(graph, src, visited, order)
    return visited[dst]


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 그래프 구축
    #    1 ─── 2 ─── 5
    #    │     │
    #    3 ─── 4
    n = 5
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 4)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("=" * 50)
    print("재귀 DFS — 방문 순서")
    print("=" * 50)
    visited = [False] * (n + 1)
    order: list[int] = []
    dfs(graph, 1, visited, order)
    print(f"DFS 방문 순서 (시작=1): {order}")

    print("\n=== DFS 깊이별 시각화 ===")
    visited2 = [False] * (n + 1)
    dfs_with_depth(graph, 1, visited2)

    # 전위/후위 순서
    print("\n=== 전위 / 후위 순서 ===")
    visited3 = [False] * (n + 1)
    pre: list[int] = []
    post: list[int] = []
    dfs_pre_post(graph, 1, visited3, pre, post)
    print(f"전위(pre) 순서  : {pre}")
    print(f"후위(post) 순서 : {post}")
    print(f"후위 역순       : {post[::-1]}  ← 위상 정렬에 사용")

    # 도달 가능성
    print("\n=== 도달 가능성 ===")
    for src, dst in [(1, 5), (1, 3), (5, 3)]:
        print(f"  {src} → {dst}: {is_reachable(graph, src, dst, n)}")

    # 비연결 그래프
    print("\n=== 비연결 그래프 ===")
    #  1─2  3─4  5(고립)
    n2 = 5
    edges2 = [(1, 2), (3, 4)]
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in edges2:
        g2[u].append(v)
        g2[v].append(u)

    vis2 = [False] * (n2 + 1)
    components = 0
    for node in range(1, n2 + 1):
        if not vis2[node]:
            ord2: list[int] = []
            dfs(g2, node, vis2, ord2)
            components += 1
            print(f"  연결 요소 {components}: {ord2}")
    print(f"  총 연결 요소 수: {components}")
