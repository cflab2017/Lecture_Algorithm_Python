"""
Topic  : 퀵 정렬 (랜덤 피벗)
Time   : O(n log n) 평균, O(n²) 최악 (피벗이 항상 최솟/최댓값일 때)
Space  : O(log n) 평균 (재귀 스택), O(n) 최악
"""

import random
import sys

sys.setrecursionlimit(300_000)


# ── 기본 퀵 정렬 (항상 마지막 원소 피벗) ──────────────────────────────────────

def partition(arr: list[int], low: int, high: int) -> int:
    """Lomuto 파티션 스킴.

    피벗을 high 인덱스로 설정하고,
    피벗보다 작은 원소를 왼쪽으로 보냄.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_basic(arr: list[int], low: int, high: int) -> None:
    """항상 마지막 원소를 피벗으로 사용 (이미 정렬된 배열에서 O(n²))."""
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_basic(arr, low, pi - 1)
        quick_sort_basic(arr, pi + 1, high)


# ── 랜덤 피벗 퀵 정렬 ────────────────────────────────────────────────────────

def partition_random(arr: list[int], low: int, high: int) -> int:
    """랜덤 인덱스와 high를 교환한 뒤 Lomuto 파티션."""
    rand_idx = random.randint(low, high)
    arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
    return partition(arr, low, high)


def quick_sort_random(arr: list[int], low: int, high: int) -> None:
    """랜덤 피벗 퀵 정렬 — 최악 케이스 확률적으로 회피."""
    if low < high:
        pi = partition_random(arr, low, high)
        quick_sort_random(arr, low, pi - 1)
        quick_sort_random(arr, pi + 1, high)


# ── 3-way 파티션 퀵 정렬 (중복 원소 최적화) ──────────────────────────────────

def quick_sort_3way(arr: list[int], low: int, high: int) -> None:
    """Dutch National Flag 기반 3-way 파티션.

    같은 값이 많을 때 O(n log n) → O(n) 이 될 수도 있음.
    lt: 피벗보다 작은 구간의 끝
    gt: 피벗보다 큰 구간의 시작
    """
    if low >= high:
        return
    pivot = arr[low]
    lt = low        # arr[low..lt-1] < pivot
    gt = high       # arr[gt+1..high] > pivot
    i = low + 1     # arr[lt..i-1] == pivot

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    quick_sort_3way(arr, low, lt - 1)
    quick_sort_3way(arr, gt + 1, high)


# ── 최악 케이스 비교 ──────────────────────────────────────────────────────────

def count_comparisons_basic(arr: list[int]) -> int:
    """기본 퀵 정렬(마지막 원소 피벗) 비교 횟수 (시뮬레이션)."""

    count = [0]

    def _partition(a: list[int], lo: int, hi: int) -> int:
        pivot = a[hi]
        i = lo - 1
        for j in range(lo, hi):
            count[0] += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[hi] = a[hi], a[i + 1]
        return i + 1

    def _qs(a: list[int], lo: int, hi: int) -> None:
        if lo < hi:
            pi = _partition(a, lo, hi)
            _qs(a, lo, pi - 1)
            _qs(a, pi + 1, hi)

    _qs(arr[:], 0, len(arr) - 1)
    return count[0]


# ── 메인 ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 기본 정렬 테스트
    data = [3, 6, 8, 10, 1, 2, 1]
    arr1 = data[:]
    quick_sort_basic(arr1, 0, len(arr1) - 1)
    print(f"기본 퀵 정렬  : {data} → {arr1}")

    arr2 = data[:]
    quick_sort_random(arr2, 0, len(arr2) - 1)
    print(f"랜덤 퀵 정렬  : {data} → {arr2}")

    arr3 = data[:]
    quick_sort_3way(arr3, 0, len(arr3) - 1)
    print(f"3-way 퀵 정렬 : {data} → {arr3}")

    # 최악 케이스 비교
    n = 100
    already_sorted = list(range(n))
    random_data = already_sorted[:]
    random.shuffle(random_data)

    cmp_sorted = count_comparisons_basic(already_sorted)
    cmp_random = count_comparisons_basic(random_data)
    print(f"\n=== 비교 횟수 (n={n}) ===")
    print(f"이미 정렬된 배열 (최악): {cmp_sorted:>6,}  ≈ n²/2 = {n*n//2:,}")
    print(f"무작위 배열     (평균): {cmp_random:>6,}  ≈ n·log₂n ≈ {int(n*__import__('math').log2(n)):,}")

    # 중복 많은 배열 — 3-way 효과
    dup_data = [random.choice([1, 2, 3]) for _ in range(20)]
    arr4 = dup_data[:]
    quick_sort_3way(arr4, 0, len(arr4) - 1)
    print(f"\n중복 배열 3-way: {dup_data}")
    print(f"             → {arr4}")

    # 정확성 검증
    test = [random.randint(-50, 50) for _ in range(50)]
    a1 = test[:]
    quick_sort_random(a1, 0, len(a1) - 1)
    assert a1 == sorted(test), "정렬 오류!"
    print("\n정확성 검증: PASS")
