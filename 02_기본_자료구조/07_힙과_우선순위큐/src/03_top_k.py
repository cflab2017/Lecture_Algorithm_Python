# Topic : Top-K 패턴 -- nlargest, nsmallest, 스트리밍 Top-K
# Time  : O(n log k) -- n원소 처리, k 크기 힙 유지
# Space : O(k) -- 힙 크기

import heapq


def top_k_largest_builtin(nums: list[int], k: int) -> list[int]:
    """heapq.nlargest 사용 -- O(n log k)."""
    return heapq.nlargest(k, nums)


def top_k_smallest_builtin(nums: list[int], k: int) -> list[int]:
    """heapq.nsmallest 사용 -- O(n log k)."""
    return heapq.nsmallest(k, nums)


def top_k_largest_manual(nums: list[int], k: int) -> list[int]:
    """크기 k min-heap 유지로 Top-K 최댓값 -- O(n log k).

    아이디어: min-heap의 루트 < 새 원소면 루트 교체.
    최종적으로 힙에 남은 k개가 전체 최댓값 k개.
    """
    h: list[int] = []
    for num in nums:
        if len(h) < k:
            heapq.heappush(h, num)
        elif num > h[0]:          # 현재 k번째보다 크면 교체
            heapq.heapreplace(h, num)  # heappop + heappush (최적화)
    return sorted(h, reverse=True)


def streaming_top_k(stream: list[int], k: int) -> list[int]:
    """스트리밍 데이터에서 Top-K 실시간 유지.

    원소가 하나씩 들어올 때마다 Top-K를 유지한다.
    Time O(n log k), Space O(k).
    """
    h: list[int] = []
    results = []
    for num in stream:
        heapq.heappush(h, num)
        if len(h) > k:
            heapq.heappop(h)
        results.append(sorted(h, reverse=True))
    return results[-1] if results else []


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """빈도 기준 Top-K 원소 반환 -- O(n log k)."""
    freq: dict[int, int] = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # (빈도, 값) 으로 nlargest
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 3

    print("=" * 55)
    print(f"Top-K 테스트 (nums={nums}, k={k})")
    print("=" * 55)

    print("nlargest (상위 3):", top_k_largest_builtin(nums, k))
    print("nsmallest (하위 3):", top_k_smallest_builtin(nums, k))
    print("manual top-k largest:", top_k_largest_manual(nums, k))

    print()
    print("=" * 55)
    print("스트리밍 Top-K")
    print("=" * 55)
    stream = [7, 2, 5, 1, 9, 3]
    k2 = 3
    final = streaming_top_k(stream, k2)
    print(f"stream={stream}, k={k2}")
    print("최종 Top-K:", final)

    print()
    print("=" * 55)
    print("빈도 기준 Top-K")
    print("=" * 55)
    freq_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
    ]
    for arr, k3, expected in freq_cases:
        result = top_k_frequent(arr, k3)
        ok = "OK" if sorted(result) == sorted(expected) else "NG"
        print(f"nums={arr}, k={k3} -> {result}  {ok}")

    print()
    print("=" * 55)
    print("nlargest vs sorted 복잡도 비교 안내")
    print("=" * 55)
    print("nlargest(k, arr): O(n log k)  -- k << n 일 때 유리")
    print("sorted(arr)[-k:]: O(n log n)  -- k가 n에 가까울 때 유사")
    print("단, k >= n/2 이면 sorted가 더 빠를 수 있음")
