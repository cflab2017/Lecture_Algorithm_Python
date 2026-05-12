# Topic : Max-Heap -- 음수 변환 트릭
# Time  : push O(log n), pop O(log n)
# Space : O(n) -- 힙 크기

import heapq


def max_heappush(h: list[int], val: int) -> None:
    """Max-Heap에 원소 추가 -- 음수로 변환해 push."""
    heapq.heappush(h, -val)


def max_heappop(h: list[int]) -> int:
    """Max-Heap에서 최댓값 추출 -- pop 후 부호 복원."""
    return -heapq.heappop(h)


def max_peek(h: list[int]) -> int:
    """Max-Heap 최댓값 조회 (제거 없이)."""
    return -h[0]


def demo_max_heap() -> None:
    """Max-Heap 데모."""
    print("=" * 50)
    print("Max-Heap -- 음수 변환 트릭")
    print("=" * 50)

    h: list[int] = []
    values = [5, 3, 8, 1, 9, 2, 7]

    for val in values:
        max_heappush(h, val)
        print(f"push({val}) -> 최댓값: {max_peek(h)}, 내부 힙: {h}")

    print()
    print("pop 순서 (항상 최댓값):")
    snapshot = list(h)
    while snapshot:
        val = max_heappop(snapshot)
        print(f"  pop() -> {val}")


def demo_max_heap_with_heapify() -> None:
    """기존 리스트를 Max-Heap으로 변환."""
    print()
    print("=" * 50)
    print("Max-Heap heapify")
    print("=" * 50)

    lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print("원본:", lst)

    # 모든 원소를 음수로 변환 후 heapify
    neg_lst = [-x for x in lst]
    heapq.heapify(neg_lst)
    print("내부 힙(음수):", neg_lst)
    print("최댓값:", -neg_lst[0])

    # 전부 꺼내기 (내림차순)
    sorted_desc = []
    while neg_lst:
        sorted_desc.append(-heapq.heappop(neg_lst))
    print("내림차순 정렬:", sorted_desc)


def demo_kth_largest() -> None:
    """K번째로 큰 원소 찾기 -- Min-Heap 크기 K 유지."""
    print()
    print("=" * 50)
    print("K번째로 큰 원소 -- Min-Heap 크기 K 유지")
    print("=" * 50)

    def kth_largest(nums: list[int], k: int) -> int:
        """Time O(n log k), Space O(k)."""
        h: list[int] = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)    # 가장 작은 것 제거
        return h[0]   # 크기 k min-heap의 루트 = k번째로 큰 값

    test_cases = [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ]
    for nums, k, expected in test_cases:
        result = kth_largest(nums, k)
        ok = "OK" if result == expected else "NG"
        print(f"nums={nums}, k={k} -> {result}  {ok}")


if __name__ == "__main__":
    demo_max_heap()
    demo_max_heap_with_heapify()
    demo_kth_largest()
