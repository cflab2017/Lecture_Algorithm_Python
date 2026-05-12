# Topic : Min-Heap 기초 -- heappush, heappop, heapify, peek
# Time  : push O(log n), pop O(log n), heapify O(n)
# Space : O(n) -- 힙 크기

import heapq


def demo_basic_operations() -> None:
    """heapq 기본 연산 데모."""
    print("=" * 50)
    print("Min-Heap 기본 연산")
    print("=" * 50)

    h: list[int] = []

    # heappush -- O(log n)
    for val in [5, 3, 8, 1, 9, 2, 7]:
        heapq.heappush(h, val)
        print(f"push({val}) -> 힙 루트(최솟값): {h[0]}, 힙: {h}")

    print()
    # heappop -- O(log n): 항상 최솟값 반환
    print("pop 순서 (항상 최솟값):")
    snapshot = list(h)
    while snapshot:
        val = heapq.heappop(snapshot)
        print(f"  pop() -> {val}")


def demo_heapify() -> None:
    """heapify -- 리스트를 O(n)에 힙으로 변환."""
    print()
    print("=" * 50)
    print("heapify -- O(n) in-place 변환")
    print("=" * 50)

    lst = [9, 5, 3, 7, 1, 8, 2, 6, 4]
    print("변환 전:", lst)

    heapq.heapify(lst)   # in-place, 반환값 없음
    print("변환 후:", lst)
    print("루트(최솟값):", lst[0])

    # 주의: heapify는 None을 반환
    lst2 = [3, 1, 2]
    ret = heapq.heapify(lst2)
    print(f"\nheapify() 반환값: {ret}  (None -- 반환값 없음)")
    print("lst2 변환 후:", lst2)


def demo_peek() -> None:
    """peek -- 힙 루트 조회 (제거 없이)."""
    print()
    print("=" * 50)
    print("peek -- O(1) 최솟값 조회")
    print("=" * 50)

    h = [4, 7, 2, 9, 1, 5]
    heapq.heapify(h)
    print("힙:", h)
    print("peek (h[0]):", h[0])   # 제거 없이 최솟값 확인
    print("힙 변화 없음:", h)


def demo_tuple_heap() -> None:
    """튜플 힙 -- (우선순위, 값) 패턴."""
    print()
    print("=" * 50)
    print("튜플 힙 -- 우선순위 큐")
    print("=" * 50)

    # 작업 스케줄링: (우선순위, 작업명)
    h: list[tuple[int, str]] = []
    tasks = [(3, "낮은 우선순위"), (1, "긴급"), (2, "보통"), (1, "긴급2")]
    for priority, name in tasks:
        heapq.heappush(h, (priority, name))
        print(f"  push({priority}, {name!r})")

    print("\n처리 순서:")
    while h:
        priority, name = heapq.heappop(h)
        print(f"  우선순위 {priority}: {name}")


if __name__ == "__main__":
    demo_basic_operations()
    demo_heapify()
    demo_peek()
    demo_tuple_heap()
