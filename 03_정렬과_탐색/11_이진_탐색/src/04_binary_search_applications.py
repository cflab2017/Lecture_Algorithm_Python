"""
Topic  : 이진 탐색 응용 — 최초/최후 등장, 회전 배열 탐색
Time   : O(log n)
Space  : O(1)
"""

from bisect import bisect_left, bisect_right


# ── 최초 등장 위치 ────────────────────────────────────────────────────────────

def find_first(arr: list[int], target: int) -> int:
    """정렬 배열에서 target의 첫 번째 위치.

    없으면 -1 반환.
    """
    idx = bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1


def find_last(arr: list[int], target: int) -> int:
    """정렬 배열에서 target의 마지막 위치.

    없으면 -1 반환.
    """
    idx = bisect_right(arr, target) - 1
    if idx >= 0 and arr[idx] == target:
        return idx
    return -1


def demo_first_last() -> None:
    """최초/최후 등장 위치 데모."""
    arr = [1, 2, 3, 3, 3, 3, 4, 5]
    print("=== 최초 / 최후 등장 위치 ===")
    print(f"배열: {arr}")
    for target in [1, 3, 5, 6]:
        first = find_first(arr, target)
        last = find_last(arr, target)
        print(f"  target={target}: 최초={first:2d}, 최후={last:2d}")


# ── 회전 정렬 배열 탐색 ───────────────────────────────────────────────────────

def search_rotated(arr: list[int], target: int) -> int:
    """회전된 정렬 배열에서 target 탐색.

    예: [4, 5, 6, 7, 0, 1, 2] — 원래 [0,1,2,4,5,6,7] 에서 회전
    Time: O(log n)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        # 왼쪽 절반이 정렬됨
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # 오른쪽 절반이 정렬됨
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def demo_rotated_search() -> None:
    """회전 정렬 배열 탐색 데모."""
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"\n=== 회전 정렬 배열 탐색 ===")
    print(f"배열: {rotated}")
    for target in [0, 4, 7, 3]:
        idx = search_rotated(rotated, target)
        print(f"  target={target}: 인덱스={idx}")


# ── k번째 작은 수 (두 정렬 배열) ────────────────────────────────────────────

def find_kth_in_sorted_arrays(
    a: list[int], b: list[int], k: int
) -> int:
    """두 정렬 배열에서 합쳐진 k번째 원소 O(log(m+n)).

    간단 구현: 이진 탐색으로 분할점 결정
    """
    # k가 1-indexed
    if len(a) > len(b):
        a, b = b, a     # a가 더 짧도록
    lo = max(0, k - len(b))
    hi = min(k, len(a))

    while lo <= hi:
        i = (lo + hi) // 2
        j = k - i
        a_left = a[i - 1] if i > 0 else float('-inf')
        a_right = a[i] if i < len(a) else float('inf')
        b_left = b[j - 1] if j > 0 else float('-inf')
        b_right = b[j] if j < len(b) else float('inf')

        if a_left <= b_right and b_left <= a_right:
            return int(max(a_left, b_left))
        elif a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    return -1


def demo_kth_sorted() -> None:
    """두 정렬 배열에서 k번째 원소."""
    a = [1, 3, 8, 9, 15]
    b = [7, 11, 18, 19, 21, 25]
    merged = sorted(a + b)
    print(f"\n=== 두 정렬 배열에서 k번째 원소 ===")
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"합친 정렬: {merged}")
    for k in [1, 3, 6, 11]:
        result = find_kth_in_sorted_arrays(a, b, k)
        expected = merged[k - 1]
        status = "✓" if result == expected else "✗"
        print(f"  k={k:2d}: {result} (기대: {expected}) {status}")


# ── 정수 제곱근 (이진 탐색) ──────────────────────────────────────────────────

def integer_sqrt(n: int) -> int:
    """floor(sqrt(n)) 을 이진 탐색으로 계산.

    Python에는 math.isqrt 가 있지만, 이진 탐색 개념 연습.
    """
    if n < 0:
        raise ValueError("음수의 제곱근은 없음")
    if n == 0:
        return 0
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return mid
        elif sq < n:
            left = mid + 1
        else:
            right = mid - 1
    return right


def demo_sqrt() -> None:
    """이진 탐색으로 정수 제곱근."""
    import math
    print(f"\n=== 정수 제곱근 (이진 탐색) ===")
    for n in [0, 1, 4, 8, 9, 15, 16, 100, 1000000]:
        result = integer_sqrt(n)
        expected = math.isqrt(n)
        status = "✓" if result == expected else "✗"
        print(f"  sqrt({n:>8}) = {result:>5} {status}")


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    demo_first_last()
    demo_rotated_search()
    demo_kth_sorted()
    demo_sqrt()

    # 정확성 검증
    rotated_tests = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
    ]
    for arr, t, exp in rotated_tests:
        assert search_rotated(arr, t) == exp
    print("\n정확성 검증: PASS")
