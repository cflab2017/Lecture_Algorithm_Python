"""
Topic  : Kahn's 알고리즘 — BFS 기반 위상 정렬
Time   : O(V + E)
Space  : O(V)
"""

from collections import deque
import heapq


# ── Kahn's 위상 정렬 ──────────────────────────────────────────────────────────

def kahns_sort(
    n: int, graph: list[list[int]]
) -> list[int] | None:
    """Kahn's 알고리즘으로 위상 정렬.

    Returns:
        위상 순서 리스트, 사이클이 있으면 None
    """
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    queue: deque[int] = deque(
        [i for i in range(1, n + 1) if in_degree[i] == 0]
    )
    result: list[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(result) < n:
        return None    # 사이클 존재

    return result


def kahns_sort_verbose(
    n: int, graph: list[list[int]]
) -> list[int] | None:
    """Kahn's 알고리즘 단계별 출력."""
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    print(f"초기 진입 차수: {in_degree[1:]}")

    queue: deque[int] = deque(
        [i for i in range(1, n + 1) if in_degree[i] == 0]
    )
    result: list[int] = []
    step = 0

    while queue:
        node = queue.popleft()
        result.append(node)
        step += 1
        updated = []
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            updated.append(nxt)
            if in_degree[nxt] == 0:
                queue.append(nxt)
        print(f"단계{step:2d}: pop={node}, "
              f"in_degree 감소: {updated}, "
              f"큐: {list(queue)}")

    return result if len(result) == n else None


# ── 사전순 최소 위상 정렬 (heapq 사용) ───────────────────────────────────────

def kahns_sort_lex(
    n: int, graph: list[list[int]]
) -> list[int] | None:
    """사전순 최소 위상 정렬 (힙 사용)."""
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    heap: list[int] = [i for i in range(1, n + 1) if in_degree[i] == 0]
    heapq.heapify(heap)
    result: list[int] = []

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heapq.heappush(heap, nxt)

    return result if len(result) == n else None


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # DAG 구축
    #  1 → 3 → 5
    #  2 → 3
    #  2 → 4 → 5
    n = 5
    edges = [(1, 3), (2, 3), (2, 4), (3, 5), (4, 5)]
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)

    print("=" * 55)
    print("Kahn's 위상 정렬")
    print("=" * 55)
    result = kahns_sort_verbose(n, graph)
    print(f"\n위상 정렬 결과: {result}")

    # 사전순 비교
    print("\n=== 일반 vs 사전순 최소 ===")
    result_lex = kahns_sort_lex(n, graph)
    print(f"일반  : {result}")
    print(f"사전순: {result_lex}")

    # 사이클 케이스
    print("\n=== 사이클 탐지 ===")
    n2 = 3
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in [(1, 2), (2, 3), (3, 1)]:
        g2[u].append(v)
    result2 = kahns_sort(n2, g2)
    print(f"사이클 그래프 결과: {result2}  (None이면 사이클)")

    # 과목 수강 예시
    print("\n=== 과목 수강 순서 ===")
    courses = {
        "수학": 1, "물리": 2, "화학": 3,
        "공학수학": 4, "물리학": 5, "화학공학": 6
    }
    prereqs = [
        (courses["수학"], courses["공학수학"]),
        (courses["수학"], courses["물리학"]),
        (courses["물리"], courses["물리학"]),
        (courses["화학"], courses["화학공학"]),
        (courses["공학수학"], courses["화학공학"]),
    ]
    n3 = len(courses)
    g3: list[list[int]] = [[] for _ in range(n3 + 1)]
    for u, v in prereqs:
        g3[u].append(v)
    order = kahns_sort(n3, g3)
    rev_courses = {v: k for k, v in courses.items()}
    if order:
        print(f"수강 순서: {[rev_courses[i] for i in order]}")
