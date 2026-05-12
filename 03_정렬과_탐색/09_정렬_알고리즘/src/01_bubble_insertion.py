"""
Topic  : 버블 정렬 & 삽입 정렬 비교
Time   : O(n²) 평균/최악, O(n) 최선 (이미 정렬된 경우)
Space  : O(1) — in-place
"""

import random
import time


# ── 버블 정렬 ──────────────────────────────────────────────────────────────────

def bubble_sort(arr: list[int]) -> tuple[list[int], int]:
    """버블 정렬.

    인접한 두 원소를 비교하여 큰 값을 뒤로 보냄.
    Returns:
        (정렬된 배열, 교환 횟수)
    """
    a = arr[:]
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:        # 이미 정렬됐으면 조기 종료
            break
    return a, swaps


# ── 삽입 정렬 ──────────────────────────────────────────────────────────────────

def insertion_sort(arr: list[int]) -> tuple[list[int], int]:
    """삽입 정렬.

    정렬된 구간에 현재 원소를 적절한 위치에 삽입.
    Returns:
        (정렬된 배열, 이동 횟수)
    """
    a = arr[:]
    n = len(a)
    moves = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            moves += 1
        a[j + 1] = key
    return a, moves


# ── 단계별 시각화 ──────────────────────────────────────────────────────────────

def bubble_sort_verbose(arr: list[int]) -> list[int]:
    """각 패스 후 배열 상태 출력."""
    a = arr[:]
    n = len(a)
    print(f"초기  : {a}")
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        print(f"패스{i + 1:2d}: {a}")
        if not swapped:
            print("  ↳ 교환 없음 → 조기 종료")
            break
    return a


def insertion_sort_verbose(arr: list[int]) -> list[int]:
    """각 삽입 후 배열 상태 출력."""
    a = arr[:]
    n = len(a)
    print(f"초기  : {a}")
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"삽입[{i}]: {a}  ← {key} 삽입")
    return a


# ── 성능 비교 ─────────────────────────────────────────────────────────────────

def compare_performance(n: int = 1000) -> None:
    """무작위 배열로 두 정렬의 실행 시간과 연산 수 비교."""
    data = [random.randint(0, 10000) for _ in range(n)]

    t0 = time.perf_counter()
    _, b_swaps = bubble_sort(data)
    t1 = time.perf_counter()
    _, i_moves = insertion_sort(data)
    t2 = time.perf_counter()

    print(f"\n=== n={n} 무작위 배열 성능 비교 ===")
    print(f"버블 정렬  : 교환 {b_swaps:>10,}회  | {t1 - t0:.4f}초")
    print(f"삽입 정렬  : 이동 {i_moves:>10,}회  | {t2 - t1:.4f}초")

    # 거의 정렬된 배열
    nearly = list(range(n))
    for _ in range(max(1, n // 50)):    # 2% 정도 랜덤 교환
        i, j = random.sample(range(n), 2)
        nearly[i], nearly[j] = nearly[j], nearly[i]

    _, b_sw2 = bubble_sort(nearly)
    _, i_mv2 = insertion_sort(nearly)
    print(f"\n=== n={n} 거의 정렬된 배열 ===")
    print(f"버블 정렬  : 교환 {b_sw2:>10,}회")
    print(f"삽입 정렬  : 이동 {i_mv2:>10,}회  ← 삽입 정렬이 유리!")


# ── 메인 ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    sample = [64, 34, 25, 12, 22, 11, 90]

    print("=" * 50)
    print("버블 정렬 단계별 시각화")
    print("=" * 50)
    bubble_sort_verbose(sample)

    print()
    print("=" * 50)
    print("삽입 정렬 단계별 시각화")
    print("=" * 50)
    insertion_sort_verbose(sample)

    compare_performance(n=2000)

    # 정확성 검증
    test = [random.randint(-100, 100) for _ in range(20)]
    b_result, _ = bubble_sort(test)
    i_result, _ = insertion_sort(test)
    expected = sorted(test)
    print(f"\n정확성 검증: {'PASS' if b_result == i_result == expected else 'FAIL'}")
