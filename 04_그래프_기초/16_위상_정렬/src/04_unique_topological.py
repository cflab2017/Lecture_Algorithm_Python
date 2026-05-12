"""
Topic  : 유일한 위상 순서 판별 및 응용
Time   : O(V + E)
Space  : O(V)
"""

from collections import deque
import heapq


# ── 유일한 위상 순서 판별 ─────────────────────────────────────────────────────

def is_unique_topological(
    n: int, graph: list[list[int]]
) -> tuple[bool, list[int]]:
    """위상 정렬이 유일한지 판별.

    Kahn's 알고리즘에서 큐에 항상 1개만 있으면 유일.

    Returns:
        (유일 여부, 위상 순서)
    """
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    queue: deque[int] = deque(
        i for i in range(1, n + 1) if in_degree[i] == 0
    )
    result: list[int] = []
    is_unique = True

    while queue:
        if len(queue) > 1:
            is_unique = False   # 두 개 이상 → 선택지 발생
        node = queue.popleft()
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(result) < n:
        return False, []   # 사이클

    return is_unique, result


# ── 줄 세우기 문제 (백준 2252 스타일) ────────────────────────────────────────

def lineup(
    n: int, conditions: list[tuple[int, int]]
) -> list[int] | None:
    """조건을 만족하는 줄 세우기 순서.

    conditions: (a, b) → a가 b보다 앞에 서야 함
    """
    graph: list[list[int]] = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)

    for a, b in conditions:
        graph[a].append(b)
        in_degree[b] += 1

    queue: deque[int] = deque(
        i for i in range(1, n + 1) if in_degree[i] == 0
    )
    result: list[int] = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return result if len(result) == n else None


# ── 우선순위 큐 위상 정렬 (백준 1766 스타일) ─────────────────────────────────

def priority_topological(
    n: int,
    graph: list[list[int]],
    priority: list[int],
) -> list[int] | None:
    """우선순위 기반 위상 정렬.

    선수 과목을 모두 완료했으면, 번호가 작은 과목부터 풀기.
    """
    in_degree = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in graph[u]:
            in_degree[v] += 1

    heap: list[int] = [
        priority[i] for i in range(1, n + 1) if in_degree[i] == 0
    ]
    heapq.heapify(heap)
    result: list[int] = []

    # priority → original node 매핑
    pri_to_node = {priority[i]: i for i in range(1, n + 1)}

    while heap:
        pri = heapq.heappop(heap)
        node = pri_to_node[pri]
        result.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heapq.heappush(heap, priority[nxt])

    return result if len(result) == n else None


# ── 메인 ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=== 유일한 위상 순서 판별 ===")

    # 유일한 경우
    n1 = 5
    g1: list[list[int]] = [[] for _ in range(n1 + 1)]
    for u, v in [(1, 2), (2, 3), (3, 4), (4, 5)]:  # 선형
        g1[u].append(v)
    unique1, order1 = is_unique_topological(n1, g1)
    print(f"선형 그래프: 유일={unique1}, 순서={order1}")

    # 유일하지 않은 경우
    n2 = 4
    g2: list[list[int]] = [[] for _ in range(n2 + 1)]
    for u, v in [(1, 3), (2, 3), (3, 4)]:  # 1,2 순서 자유
        g2[u].append(v)
    unique2, order2 = is_unique_topological(n2, g2)
    print(f"분기 그래프: 유일={unique2}, 순서={order2}")

    # 줄 세우기
    print("\n=== 줄 세우기 (백준 2252 스타일) ===")
    n3, conditions = 3, [(1, 3), (2, 3)]
    result = lineup(n3, conditions)
    print(f"n=3, 조건={conditions}")
    print(f"순서: {result}")

    # 우선순위 위상 정렬
    print("\n=== 우선순위 위상 정렬 (백준 1766 스타일) ===")
    # 문제 4개: 선수 관계 있음 + 번호 작은 것 먼저 풀기
    n4 = 4
    g4: list[list[int]] = [[] for _ in range(n4 + 1)]
    for u, v in [(4, 2), (3, 1)]:   # 4→2, 3→1 (선수 관계)
        g4[u].append(v)
    # 자기 자신을 우선순위로 사용 (번호 = 우선순위)
    pri = [0] + list(range(1, n4 + 1))   # pri[i] = i
    result4 = priority_topological(n4, g4, pri)
    print(f"결과: {result4}")
    print("  3, 4 (선수 없음)를 먼저 풀고, 번호 작은 것 우선")

    # 정확성 검증
    assert unique1 is True
    assert unique2 is False
    print("\n정확성 검증: PASS")
