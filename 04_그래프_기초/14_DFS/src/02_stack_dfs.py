"""
Topic  : 스택 기반 DFS — 재귀와 비교
Time   : O(V + E)
Space  : O(V)
"""


# ── 스택 DFS ──────────────────────────────────────────────────────────────────

def dfs_stack(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """스택 기반 DFS.

    push 시 visited 처리 → 올바른 방법.
    """
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    order: list[int] = []

    while stack:
        node = stack.pop()
        order.append(node)
        # 재귀 DFS와 같은 순서를 위해 역순으로 push
        for nxt in reversed(graph[node]):
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

    return order


def dfs_stack_verbose(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """스택 DFS 단계별 출력."""
    visited = [False] * (n + 1)
    stack = [start]
    visited[start] = True
    order: list[int] = []

    print(f"초기 스택: {stack}")
    step = 0
    while stack:
        node = stack.pop()
        order.append(node)
        step += 1
        neighbors_added = []
        for nxt in reversed(graph[node]):
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                neighbors_added.append(nxt)
        print(f"단계{step:2d}: pop={node}, push={neighbors_added}, "
              f"스택={stack}")

    print(f"방문 순서: {order}")
    return order


# ── 재귀 DFS ─────────────────────────────────────────────────────────────────

def dfs_recursive(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """재귀 DFS."""
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


# ── 스택 DFS에서 흔한 실수 시연 ──────────────────────────────────────────────

def dfs_stack_wrong(
    graph: list[list[int]],
    start: int,
    n: int,
) -> list[int]:
    """잘못된 스택 DFS: pop 후 visited 처리.

    같은 노드가 여러 번 스택에 들어갈 수 있음.
    """
    visited = [False] * (n + 1)
    stack = [start]
    order: list[int] = []
    push_count = [0]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue         # 이미 방문한 노드 → 중복 처리
        visited[node] = True
        order.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                stack.append(nxt)
                push_count[0] += 1

    print(f"  (잘못된 방법) push 횟수: {push_count[0]}")
    return order


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 그래프 구축
    n = 6
    edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    print("=" * 55)
    print("스택 DFS vs 재귀 DFS 비교")
    print("=" * 55)

    stack_order = dfs_stack(graph, 1, n)
    rec_order = dfs_recursive(graph, 1, n)

    print(f"재귀  DFS 순서: {rec_order}")
    print(f"스택  DFS 순서: {stack_order}")
    print(f"순서 일치 여부: {rec_order == stack_order}")

    print("\n=== 스택 DFS 단계별 시각화 ===")
    dfs_stack_verbose(graph, 1, n)

    print("\n=== 잘못된 방법 vs 올바른 방법 ===")
    print("잘못된 방법 (pop 후 visited):")
    wrong_order = dfs_stack_wrong(graph, 1, n)
    print(f"  방문 순서: {wrong_order}")

    print("올바른 방법 (push 시 visited):")
    correct_order = dfs_stack(graph, 1, n)
    push_estimate = sum(len(graph[i]) for i in range(1, n + 1))
    print(f"  방문 순서: {correct_order}")
    print(f"  push 횟수: {n - 1}회 (노드 수 - 1)")

    # 재귀 없는 환경에서의 사용
    print("\n=== 재귀 한계 극복 ===")
    print("Python 기본 재귀 제한: 1,000")
    print("대형 그래프에서는 스택 DFS 사용 필요")
    print("또는 sys.setrecursionlimit(10**6) 설정")
