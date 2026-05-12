# =============================================================================
# 파일명: 04_complexity_compare.py
# 설명  : 선형탐색 O(n) vs 이진탐색 O(log n) 비교 (카운터로 연산 수 측정)
# 시간복잡도: 선형탐색 O(n), 이진탐색 O(log n)
# 공간복잡도: O(1) — 추가 공간 없음
# =============================================================================

import math
import time
import random


# ---------------------------------------------------------------------------
# 선형 탐색 — O(n)
# 배열을 앞에서부터 순서대로 탐색
# ---------------------------------------------------------------------------
def linear_search(arr: list, target: int) -> tuple:
    """선형 탐색으로 target의 인덱스와 비교 횟수를 반환합니다.

    시간복잡도: O(n) — 최악의 경우 n번 비교
    공간복잡도: O(1)
    """
    count = 0
    for i, val in enumerate(arr):  # 앞에서부터 순서대로
        count += 1
        if val == target:
            return i, count
    return -1, count  # 찾지 못한 경우


# ---------------------------------------------------------------------------
# 이진 탐색 — O(log n)
# 정렬된 배열에서 중간값과 비교해 범위를 절반씩 좁혀나감
# ---------------------------------------------------------------------------
def binary_search(arr: list, target: int) -> tuple:
    """이진 탐색으로 target의 인덱스와 비교 횟수를 반환합니다.

    전제 조건: arr은 오름차순 정렬되어 있어야 합니다.
    시간복잡도: O(log n) — 매 단계마다 탐색 범위 절반 감소
    공간복잡도: O(1)
    """
    count = 0
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # 중간 인덱스
        count += 1

        if arr[mid] == target:
            return mid, count       # 찾음
        elif arr[mid] < target:
            left = mid + 1          # 오른쪽 절반으로
        else:
            right = mid - 1         # 왼쪽 절반으로

    return -1, count  # 찾지 못한 경우


# ---------------------------------------------------------------------------
# 시각화: 이진 탐색 단계별 출력
# ---------------------------------------------------------------------------
def binary_search_verbose(arr: list, target: int) -> int:
    """이진 탐색 과정을 단계별로 출력합니다."""
    left, right = 0, len(arr) - 1
    step = 0

    print(f"  탐색 대상: {target}")
    print(f"  배열 크기: {len(arr)}")

    while left <= right:
        mid = (left + right) // 2
        step += 1
        print(
            f"  단계 {step}: left={left}, right={right}, "
            f"mid={mid}, arr[mid]={arr[mid]}"
        )

        if arr[mid] == target:
            print(f"  → 발견! 인덱스 {mid}, 총 {step}단계")
            return mid
        elif arr[mid] < target:
            left = mid + 1
            print(f"     arr[mid] < target → 오른쪽으로 이동")
        else:
            right = mid - 1
            print(f"     arr[mid] > target → 왼쪽으로 이동")

    print(f"  → 찾지 못함, 총 {step}단계")
    return -1


# ---------------------------------------------------------------------------
# 비교 벤치마크
# ---------------------------------------------------------------------------
def compare_benchmark(sizes: list) -> None:
    """다양한 입력 크기에서 두 탐색 알고리즘을 비교합니다."""
    print("\n" + "=" * 70)
    print("  선형탐색 O(n) vs 이진탐색 O(log n) 비교")
    print("=" * 70)
    print(
        f"{'n':>10}  {'선형 비교 횟수':>14} "
        f"{'이진 비교 횟수':>16} {'배율':>8}"
    )
    print("-" * 70)

    for n in sizes:
        arr = list(range(n))       # 0 ~ n-1 정렬된 배열
        target = n - 1              # 최악의 경우: 마지막 원소

        _, linear_count = linear_search(arr, target)
        _, binary_count = binary_search(arr, target)
        expected_log = int(math.log2(n)) + 1 if n > 1 else 1

        ratio = linear_count / binary_count if binary_count > 0 else 0
        print(
            f"{n:>10,}  "
            f"{linear_count:>14,} "
            f"{binary_count:>10,} (예상 log₂n≈{expected_log}) "
            f"{ratio:>8.1f}배"
        )

    print("=" * 70)


def main():
    print("=" * 55)
    print("  탐색 알고리즘 복잡도 비교 데모")
    print("=" * 55)

    # -----------------------------------------------------------------------
    # 이진 탐색 시각화 (작은 배열)
    # -----------------------------------------------------------------------
    print("\n[이진 탐색 단계별 시각화]")
    small_arr = list(range(0, 32, 2))  # [0, 2, 4, ..., 62]
    print(f"배열: {small_arr}")
    binary_search_verbose(small_arr, 42)

    # -----------------------------------------------------------------------
    # 탐색 결과 정확성 검증
    # -----------------------------------------------------------------------
    print("\n[결과 검증]")
    random.seed(42)
    test_arr = sorted(random.sample(range(1, 1001), 50))
    target = test_arr[25]  # 배열 중간값 선택

    lin_idx, lin_cnt = linear_search(test_arr, target)
    bin_idx, bin_cnt = binary_search(test_arr, target)

    print(f"배열 크기 50, target={target}")
    print(f"  선형탐색: 인덱스={lin_idx}, 비교횟수={lin_cnt}")
    print(f"  이진탐색: 인덱스={bin_idx}, 비교횟수={bin_cnt}")
    print(f"  결과 일치: {lin_idx == bin_idx}")

    # -----------------------------------------------------------------------
    # 벤치마크 테이블
    # -----------------------------------------------------------------------
    compare_benchmark([10, 100, 1_000, 10_000, 100_000, 1_000_000])

    # -----------------------------------------------------------------------
    # 실행 시간 비교
    # -----------------------------------------------------------------------
    print("\n[실행 시간 비교] n=1,000,000, 최악의 경우 1,000회 탐색")
    big_arr = list(range(1_000_000))
    target = 999_999
    repeat = 1000

    start = time.perf_counter()
    for _ in range(repeat):
        linear_search(big_arr, target)
    t_linear = time.perf_counter() - start

    start = time.perf_counter()
    for _ in range(repeat):
        binary_search(big_arr, target)
    t_binary = time.perf_counter() - start

    print(f"  선형탐색 {repeat}회: {t_linear:.4f}초")
    print(f"  이진탐색 {repeat}회: {t_binary:.6f}초")
    if t_binary > 0:
        print(f"  이진탐색이 {t_linear/t_binary:.0f}배 빠름")


if __name__ == "__main__":
    main()
