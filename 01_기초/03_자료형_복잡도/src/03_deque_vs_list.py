# =============================================================================
# 파일명: 03_deque_vs_list.py
# 설명  : deque vs list 큐 연산 속도 비교
# 시간복잡도: deque.popleft() O(1), list.pop(0) O(n)
# 공간복잡도: O(n) — 저장되는 원소 수
# =============================================================================

import time
import timeit
from collections import deque


# ---------------------------------------------------------------------------
# BFS 큐 시뮬레이션: list.pop(0) 사용 — O(n²)
# ---------------------------------------------------------------------------
def bfs_with_list(graph: dict, start: int) -> list:
    """list를 큐로 사용한 BFS. 시간복잡도: O(V + E) but pop(0) O(V²)"""
    visited = []
    order = []
    queue = [start]         # list를 큐로 사용

    while queue:
        node = queue.pop(0)  # O(n) — 모든 원소를 앞으로 이동
        if node in visited:
            continue
        visited.append(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return order


# ---------------------------------------------------------------------------
# BFS 큐 시뮬레이션: deque.popleft() 사용 — O(V + E)
# ---------------------------------------------------------------------------
def bfs_with_deque(graph: dict, start: int) -> list:
    """deque를 큐로 사용한 BFS. 시간복잡도: O(V + E)"""
    visited = set()
    order = []
    queue = deque([start])  # deque를 큐로 사용

    while queue:
        node = queue.popleft()  # O(1) — 앞에서 바로 제거
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

    return order


# ---------------------------------------------------------------------------
# deque 연산 데모
# ---------------------------------------------------------------------------
def demo_deque_operations() -> None:
    """deque의 주요 연산을 시연합니다."""
    print("\n[deque 기본 연산 데모]")
    print("-" * 50)

    dq = deque()

    # 양쪽 끝에 추가
    dq.append(3)         # 오른쪽 추가: [3]
    dq.append(4)         # 오른쪽 추가: [3, 4]
    dq.appendleft(2)     # 왼쪽 추가:  [2, 3, 4]
    dq.appendleft(1)     # 왼쪽 추가:  [1, 2, 3, 4]
    print(f"  append/appendleft 후: {list(dq)}")

    # 양쪽 끝에서 제거
    right = dq.pop()     # 오른쪽 제거: [1, 2, 3]
    left = dq.popleft()  # 왼쪽 제거:  [2, 3]
    print(f"  pop() = {right}, popleft() = {left}")
    print(f"  제거 후: {list(dq)}")

    # 회전
    dq = deque([1, 2, 3, 4, 5])
    dq.rotate(2)   # 오른쪽으로 2 회전
    print(f"  rotate(2) 후: {list(dq)}")  # [4, 5, 1, 2, 3]
    dq.rotate(-2)  # 왼쪽으로 2 회전
    print(f"  rotate(-2) 후: {list(dq)}")  # [1, 2, 3, 4, 5]

    # maxlen 옵션 — 최대 크기 제한
    fixed = deque(maxlen=3)
    for i in range(5):
        fixed.append(i)
        print(f"  append({i}) → {list(fixed)}")


# ---------------------------------------------------------------------------
# 성능 벤치마크
# ---------------------------------------------------------------------------
def benchmark_queue_operations(n: int = 10_000) -> None:
    """list와 deque의 큐 연산 속도를 비교합니다."""
    print(f"\n[큐 연산 벤치마크] n={n:,}번 append + popleft")
    print("-" * 50)

    # list: append + pop(0) — O(n²) 전체
    t0 = time.perf_counter()
    lst = []
    for i in range(n):
        lst.append(i)
    for _ in range(n):
        lst.pop(0)           # O(n) 매번
    t_list = time.perf_counter() - t0

    # deque: append + popleft — O(n) 전체
    t0 = time.perf_counter()
    dq = deque()
    for i in range(n):
        dq.append(i)
    for _ in range(n):
        dq.popleft()         # O(1) 매번
    t_deque = time.perf_counter() - t0

    ratio = t_list / t_deque if t_deque > 0 else float('inf')
    print(f"  list (pop(0)):   {t_list:.4f}초  O(n²)")
    print(f"  deque (popleft): {t_deque:.6f}초  O(n)")
    print(f"  deque가 {ratio:.1f}배 빠름 (n={n}에서)")


def main():
    print("=" * 55)
    print("  deque vs list 큐 연산 비교")
    print("=" * 55)

    # deque 기본 연산 시연
    demo_deque_operations()

    # BFS 정확성 검증
    print("\n[BFS 정확성 검증]")
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [5, 6],
        4: [],
        5: [6],
        6: []
    }
    result_list = bfs_with_list(graph, 1)
    result_deque = bfs_with_deque(graph, 1)
    print(f"  list BFS:  {result_list}")
    print(f"  deque BFS: {result_deque}")
    print(f"  결과 일치: {result_list == result_deque}")

    # 성능 벤치마크
    benchmark_queue_operations(n=10_000)

    print("\n" + "=" * 55)
    print("  핵심 정리")
    print("=" * 55)
    print("  BFS 큐로 list.pop(0) → O(n²) 전체  [금지]")
    print("  BFS 큐로 deque.popleft() → O(n) 전체 [권장]")
    print("  from collections import deque 을 항상 사용하세요!")


if __name__ == "__main__":
    main()
