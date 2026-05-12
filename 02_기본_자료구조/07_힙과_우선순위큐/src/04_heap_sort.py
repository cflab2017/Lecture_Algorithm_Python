# Topic : 힙 정렬 (Heap Sort) -- O(n log n)
# Time  : O(n log n) -- heapify O(n) + n번 heappop O(log n)
# Space : O(n) heapq 버전 / O(1) in-place 버전

import heapq


def heap_sort_asc(arr: list[int]) -> list[int]:
    """힙 정렬 오름차순 -- heapq 사용, O(n log n).

    1. 리스트를 min-heap으로 변환 O(n)
    2. heappop을 n번 반복 -> 오름차순 O(n log n)
    """
    h = list(arr)         # 복사본 (원본 보존)
    heapq.heapify(h)      # O(n)
    result = []
    while h:
        result.append(heapq.heappop(h))   # O(log n) * n번
    return result


def heap_sort_desc(arr: list[int]) -> list[int]:
    """힙 정렬 내림차순 -- max-heap 트릭, O(n log n)."""
    h = [-x for x in arr]
    heapq.heapify(h)
    result = []
    while h:
        result.append(-heapq.heappop(h))
    return result


def heap_sort_inplace(arr: list[int]) -> None:
    """In-place 힙 정렬 -- Space O(1) (추가 배열 없음).

    최대 힙을 직접 구현하여 정렬.
    Python heapq는 min-heap이라 직접 구현 필요.
    """
    n = len(arr)

    def sift_down(arr: list[int], root: int, end: int) -> None:
        """root 위치에서 아래로 재배치 (max-heap)."""
        while True:
            largest = root
            left  = 2 * root + 1
            right = 2 * root + 2

            if left < end and arr[left] > arr[largest]:
                largest = left
            if right < end and arr[right] > arr[largest]:
                largest = right

            if largest == root:
                break
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # 1. max-heap 구성 O(n)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)

    # 2. 하나씩 뽑아 끝에 배치 O(n log n)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # 최댓값을 끝으로
        sift_down(arr, 0, end)


if __name__ == "__main__":
    import random

    print("=" * 55)
    print("힙 정렬 정확성 테스트")
    print("=" * 55)

    test_cases = [
        [5, 3, 8, 1, 9, 2, 7, 4, 6],
        [1],
        [],
        [3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]

    for arr in test_cases:
        asc  = heap_sort_asc(arr)
        desc = heap_sort_desc(arr)

        # in-place 검증
        inplace = list(arr)
        heap_sort_inplace(inplace)

        expected_asc  = sorted(arr)
        expected_desc = sorted(arr, reverse=True)

        ok_asc     = "OK" if asc     == expected_asc     else "NG"
        ok_desc    = "OK" if desc    == expected_desc    else "NG"
        ok_inplace = "OK" if inplace == expected_asc     else "NG"

        print(
            f"입력: {str(arr):30} | "
            f"오름차순 {ok_asc} | "
            f"내림차순 {ok_desc} | "
            f"in-place {ok_inplace}"
        )

    print()
    print("=" * 55)
    print("성능 테스트 (n=50,000)")
    print("=" * 55)
    import time

    big = random.sample(range(200_000), 50_000)

    t0 = time.perf_counter()
    heap_sort_asc(big)
    t1 = time.perf_counter()
    print(f"heap_sort_asc (heapq)  : {t1 - t0:.4f}s")

    t0 = time.perf_counter()
    sorted(big)
    t1 = time.perf_counter()
    print(f"sorted() (Timsort)     : {t1 - t0:.4f}s")
    print("(Timsort이 CPython 내장으로 더 빠릅니다)")
