"""
Topic  : 연결 요소 — DFS로 개수 세기 및 분류
Time   : O(V + E)
Space  : O(V)
"""

import sys
sys.setrecursionlimit(100_000)


# ── 연결 요소 개수 ────────────────────────────────────────────────────────────

def count_components(n: int, graph: list[list[int]]) -> int:
    """무방향 그래프의 연결 요소 개수 반환."""
    visited = [False] * (n + 1)
    count = 0

    def dfs(node: int) -> None:
        visited[node] = True
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt)

    for node in range(1, n + 1):
        if not visited[node]:
            dfs(node)
            count += 1

    return count


# ── 연결 요소 분류 ────────────────────────────────────────────────────────────

def find_components(
    n: int, graph: list[list[int]]
) -> list[list[int]]:
    """각 연결 요소에 속한 노드 목록 반환."""
    visited = [False] * (n + 1)
    components: list[list[int]] = []

    def dfs(node: int, component: list[int]) -> None:
        visited[node] = True
        component.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                dfs(nxt, component)

    for node in range(1, n + 1):
        if not visited[node]:
            comp: list[int] = []
            dfs(node, comp)
            components.append(sorted(comp))

    return components


# ── 레이블 배열 ──────────────────────────────────────────────────────────────

def label_components(
    n: int, graph: list[list[int]]
) -> list[int]:
    """각 노드가 속한 연결 요소 번호 반환 (1-indexed).

    같은 연결 요소는 같은 번호.
    """
    label = [0] * (n + 1)   # 0 = 미방문
    comp_id = 0

    def dfs(node: int, cid: int) -> None:
        label[node] = cid
        for nxt in graph[node]:
            if label[nxt] == 0:
                dfs(nxt, cid)

    for node in range(1, n + 1):
        if label[node] == 0:
            comp_id += 1
            dfs(node, comp_id)

    return label


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 그래프 1: 3개 연결 요소
    #  1─2   3─4─5   6
    n1 = 6
    edges1 = [(1, 2), (3, 4), (4, 5)]
    g1: list[list[int]] = [[] for _ in range(n1 + 1)]
    for u, v in edges1:
        g1[u].append(v)
        g1[v].append(u)

    print("=" * 50)
    print("연결 요소 탐색")
    print("=" * 50)
    print(f"그래프 1: 1─2   3─4─5   6")
    cnt = count_components(n1, g1)
    comps = find_components(n1, g1)
    labels = label_components(n1, g1)

    print(f"연결 요소 수: {cnt}")
    for i, comp in enumerate(comps, 1):
        print(f"  요소 {i}: {comp}")
    print(f"레이블 배열: {labels[1:]}")

    # 그래프 2: 완전 연결
    #  1─2─3─4─5
    n2 = 5
    edges2 = [(1, 2), (2, 3), (3, 4), (4, 5)]
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in edges2:
        g2[u].append(v)
        g2[v].append(u)

    print(f"\n그래프 2: 1─2─3─4─5 (선형)")
    cnt2 = count_components(n2, g2)
    comps2 = find_components(n2, g2)
    print(f"연결 요소 수: {cnt2}")
    print(f"연결 요소: {comps2}")

    # 그래프 3: 모두 고립
    n3 = 4
    g3: list[list[int]] = [[] for _ in range(n3 + 1)]
    print(f"\n그래프 3: 1  2  3  4 (모두 고립)")
    cnt3 = count_components(n3, g3)
    print(f"연결 요소 수: {cnt3}")

    # 응용: 노드 색칠 (이분 그래프 판별)
    print("\n=== 이분 그래프 판별 ===")
    def is_bipartite(n: int, graph: list[list[int]]) -> bool:
        color = [-1] * (n + 1)

        def dfs_color(node: int, c: int) -> bool:
            color[node] = c
            for nxt in graph[node]:
                if color[nxt] == -1:
                    if not dfs_color(nxt, 1 - c):
                        return False
                elif color[nxt] == c:
                    return False
            return True

        for node in range(1, n + 1):
            if color[node] == -1:
                if not dfs_color(node, 0):
                    return False
        return True

    # 이분 그래프
    g_bip: list[list[int]] = [[] for _ in range(5)]
    for u, v in [(1, 2), (1, 4), (3, 2), (3, 4)]:
        g_bip[u].append(v)
        g_bip[v].append(u)
    print(f"이분 그래프 (사각형): {is_bipartite(4, g_bip)}")

    # 홀수 사이클
    g_odd: list[list[int]] = [[] for _ in range(4)]
    for u, v in [(1, 2), (2, 3), (3, 1)]:
        g_odd[u].append(v)
        g_odd[v].append(u)
    print(f"홀수 사이클 (삼각형): {is_bipartite(3, g_odd)}")
