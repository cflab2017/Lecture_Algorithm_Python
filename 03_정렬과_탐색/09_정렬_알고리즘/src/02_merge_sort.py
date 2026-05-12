"""
Topic  : 병합 정렬 (재귀 & 반복)
Time   : O(n log n) — 최선/평균/최악 모두
Space  : O(n) — 보조 배열 필요
"""

import random


# ── 재귀 병합 정렬 ─────────────────────────────────────────────────────────────

_merge_count = 0     # 병합 호출 횟수 전역 카운터


def merge(arr: list[int], left: int, mid: int, right: int) -> int:
    """두 정렬된 구간 [left, mid], [mid+1, right] 를 병합.

    Returns:
        이번 병합에서 수행한 비교 횟수
    """
    global _merge_count
    _merge_count += 1

    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]

    i = j = 0
    k = left
    comparisons = 0
    while i < len(left_sub) and j < len(right_sub):
        comparisons += 1
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1

    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1

    return comparisons


def merge_sort_recursive(arr: list[int], left: int, right: int) -> None:
    """재귀 병합 정렬 (in-place 수정)."""
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort_recursive(arr, left, mid)
    merge_sort_recursive(arr, mid + 1, right)
    merge(arr, left, mid, right)


# ── 반복 병합 정렬 (Bottom-Up) ────────────────────────────────────────────────

def merge_sort_iterative(arr: list[int]) -> list[int]:
    """Bottom-up 반복 병합 정렬.

    크기 1 → 2 → 4 → 8 … 순서로 병합.
    재귀 스택 없이 동작.
    """
    a = arr[:]
    n = len(a)
    size = 1
    while size < n:
        for left in range(0, n, size * 2):
            mid = min(left + size - 1, n - 1)
            right = min(left + size * 2 - 1, n - 1)
            if mid < right:
                merge(a, left, mid, right)
        size *= 2
    return a


# ── 단계 시각화 ───────────────────────────────────────────────────────────────

def merge_sort_verbose(arr: list[int], depth: int = 0) -> list[int]:
    """분할/병합 과정을 들여쓰기로 시각화."""
    indent = "  " * depth
    if len(arr) <= 1:
        print(f"{indent}└ {arr}")
        return arr[:]

    mid = len(arr) // 2
    print(f"{indent}분할: {arr} → {arr[:mid]} | {arr[mid:]}")
    left = merge_sort_verbose(arr[:mid], depth + 1)
    right = merge_sort_verbose(arr[mid:], depth + 1)

    merged: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}병합: {left} + {right} → {merged}")
    return merged


# ── 메인 ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 단계 시각화 (소규모)
    small = [5, 2, 8, 1, 9, 3]
    print("=" * 55)
    print("병합 정렬 분할/병합 시각화")
    print("=" * 55)
    result = merge_sort_verbose(small)
    print(f"\n최종 결과: {result}")

    # 재귀 정렬
    data = [random.randint(1, 100) for _ in range(16)]
    print(f"\n재귀 병합 정렬 전: {data}")
    _merge_count = 0
    arr_copy = data[:]
    merge_sort_recursive(arr_copy, 0, len(arr_copy) - 1)
    print(f"재귀 병합 정렬 후: {arr_copy}")
    print(f"병합 함수 호출 횟수: {_merge_count}회  (n-1 = {len(data)-1})")

    # 반복 정렬
    arr2 = data[:]
    _merge_count = 0
    arr2_sorted = merge_sort_iterative(arr2)
    print(f"\n반복 병합 정렬 후: {arr2_sorted}")
    print(f"병합 함수 호출 횟수: {_merge_count}회")

    # 정확성 검증
    assert arr_copy == arr2_sorted == sorted(data), "정렬 오류!"
    print("\n정확성 검증: PASS")

    # 안정 정렬 확인
    students = [("Alice", 85), ("Bob", 92), ("Charlie", 85), ("Dave", 92)]
    # 점수 기준 정렬 (안정: 같은 점수끼리 원래 순서 유지)
    students_sorted = sorted(students, key=lambda x: x[1])
    print(f"\n안정 정렬 확인: {students_sorted}")
    print("← 같은 점수(85: Alice<Charlie, 92: Bob<Dave) 순서 유지됨")
