# Topic : 큐 기초 -- deque vs list 성능 비교, BFS 시뮬레이션
# Time  : enqueue O(1), dequeue O(1) (deque 기준)
# Space : O(n) -- 큐에 저장된 원소 수

import time
from collections import deque


def demo_deque_operations() -> None:
    """deque 기본 연산 데모."""
    print("=" * 50)
    print("deque 기본 연산")
    print("=" * 50)

    q: deque[int] = deque()

    # enqueue (오른쪽 추가)
    for val in [10, 20, 30, 40, 50]:
        q.append(val)
        print(f"enqueue({val:2}) -> front{list(q)}back")

    print()
    # dequeue (왼쪽 제거)
    while q:
        val = q.popleft()
        print(f"dequeue() -> {val:2}  front{list(q)}back")

    # 덱(deque): 양쪽 O(1)
    print()
    print("덱 양방향 연산:")
    d: deque[int] = deque([1, 2, 3])
    d.appendleft(0)   # 왼쪽 추가
    d.append(4)       # 오른쪽 추가
    print("appendleft(0), append(4):", list(d))   # [0,1,2,3,4]
    d.popleft()       # 왼쪽 제거
    d.pop()           # 오른쪽 제거
    print("popleft(), pop():         ", list(d))  # [1,2,3]

    # maxlen 기능 (슬라이딩 윈도우 유용)
    window: deque[int] = deque(maxlen=3)
    for v in range(6):
        window.append(v)
        print(f"  append({v}) -> {list(window)}")


def benchmark_list_vs_deque(n: int = 100_000) -> None:
    """list.pop(0) vs deque.popleft() 성능 비교."""
    print()
    print("=" * 50)
    print(f"성능 비교: list.pop(0) vs deque.popleft() (n={n:,})")
    print("=" * 50)

    # list 방식 -- O(n) per pop(0)
    lst = list(range(n))
    t0 = time.perf_counter()
    while lst:
        lst.pop(0)
    t1 = time.perf_counter()
    list_time = t1 - t0

    # deque 방식 -- O(1) per popleft()
    dq = deque(range(n))
    t0 = time.perf_counter()
    while dq:
        dq.popleft()
    t1 = time.perf_counter()
    deque_time = t1 - t0

    print(f"list.pop(0)       : {list_time:.4f}s")
    print(f"deque.popleft()   : {deque_time:.4f}s")
    if deque_time > 0:
        print(f"deque가 약 {list_time / deque_time:.1f}배 빠릅니다!")


def bfs_iterative(
    graph: dict[int, list[int]], start: int
) -> list[int]:
    """큐를 이용한 BFS -- Time O(V+E), Space O(V)."""
    visited: list[int] = []
    seen: set[int] = {start}
    queue: deque[int] = deque([start])

    while queue:
        node = queue.popleft()    # FIFO -> BFS
        visited.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited


def demo_bfs() -> None:
    """그래프 BFS 시뮬레이션."""
    print()
    print("=" * 50)
    print("큐 기반 BFS 시뮬레이션")
    print("=" * 50)

    #   1
    #  / \\
    # 2   3
    # |   |
    # 4   5
    graph = {1: [2, 3], 2: [4], 3: [5], 4: [], 5: []}
    print("그래프:", graph)
    order = bfs_iterative(graph, start=1)
    print("BFS 방문 순서 (시작=1):", order)   # [1, 2, 3, 4, 5]


if __name__ == "__main__":
    demo_deque_operations()
    benchmark_list_vs_deque()
    demo_bfs()
