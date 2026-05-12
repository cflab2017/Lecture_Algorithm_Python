"""
Topic  : 이진 탐색 — 반복 & 재귀 구현
Time   : O(log n)
Space  : O(1) 반복, O(log n) 재귀 스택
"""

import random


# ── 반복 이진 탐색 ────────────────────────────────────────────────────────────

def binary_search_iterative(
    arr: list[int], target: int
) -> int:
    """반복문 기반 이진 탐색.

    Returns:
        찾은 인덱스, 없으면 -1
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ── 재귀 이진 탐색 ────────────────────────────────────────────────────────────

def binary_search_recursive(
    arr: list[int], target: int, left: int, right: int
) -> int:
    """재귀 기반 이진 탐색.

    Returns:
        찾은 인덱스, 없으면 -1
    """
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ── 단계별 시각화 ─────────────────────────────────────────────────────────────

def binary_search_verbose(arr: list[int], target: int) -> int:
    """이진 탐색 단계를 출력하면서 진행."""
    left, right = 0, len(arr) - 1
    step = 0
    print(f"\n탐색 배열: {arr}")
    print(f"찾는 값 : {target}")
    print("-" * 50)

    while left <= right:
        step += 1
        mid = (left + right) // 2
        # 배열 시각화
        display = []
        for i, v in enumerate(arr):
            if i == mid:
                display.append(f"[{v}]")     # 피벗
            elif left <= i <= right:
                display.append(f" {v} ")
            else:
                display.append(f" · ")
        print(f"단계{step:2d}: {''.join(display)}")
        print(f"      left={left}, mid={mid}, right={right}, "
              f"arr[mid]={arr[mid]}")

        if arr[mid] == target:
            print(f"  → 발견! 인덱스 {mid}")
            return mid
        elif arr[mid] < target:
            print(f"  → {arr[mid]} < {target}, 오른쪽 탐색")
            left = mid + 1
        else:
            print(f"  → {arr[mid]} > {target}, 왼쪽 탐색")
            right = mid - 1

    print(f"  → 없음 (-1)")
    return -1


# ── 메인 ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    print("=" * 55)
    print("이진 탐색 — 반복 vs 재귀")
    print("=" * 55)

    for target in [7, 1, 19, 6]:
        it = binary_search_iterative(arr, target)
        rec = binary_search_recursive(arr, target, 0, len(arr) - 1)
        status = "✓" if it == rec else "✗"
        print(f"target={target:3d}: 반복={it:3d}, 재귀={rec:3d} {status}")

    # 단계별 시각화
    binary_search_verbose(arr, 7)
    binary_search_verbose(arr, 6)

    # 비교 횟수 분석
    print("\n=== 비교 횟수 분석 ===")
    n = len(arr)
    import math
    print(f"배열 길이 n={n}, 최대 비교 횟수 ≈ log₂({n}) = {math.log2(n):.1f}")

    # 정확성 검증
    test_arr = sorted(random.sample(range(1, 1000), 100))
    for t in random.sample(test_arr, 20) + [999, 0]:
        expected = test_arr.index(t) if t in test_arr else -1
        assert binary_search_iterative(test_arr, t) == expected
    print("정확성 검증: PASS")
