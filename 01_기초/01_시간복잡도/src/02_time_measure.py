# =============================================================================
# 파일명: 02_time_measure.py
# 설명  : timeit / time 모듈로 버블정렬(O(n²))과 내장 sorted()(O(n log n)) 비교
# 시간복잡도: 버블정렬 O(n²), sorted() O(n log n)
# 공간복잡도: O(n) — 정렬 대상 배열
# =============================================================================

import time
import timeit
import random
import copy


# ---------------------------------------------------------------------------
# 버블 정렬 — O(n²)
# ---------------------------------------------------------------------------
def bubble_sort(arr: list) -> list:
    """버블 정렬 구현. 시간복잡도: O(n²), 공간복잡도: O(1)"""
    a = arr[:]          # 원본 보호를 위해 복사
    n = len(a)
    for i in range(n):              # 외부 루프: n번
        swapped = False
        for j in range(n - i - 1):  # 내부 루프: n-i-1번
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 교환
                swapped = True
        if not swapped:             # 이미 정렬됨 → 조기 종료 최적화
            break
    return a


# ---------------------------------------------------------------------------
# 삽입 정렬 — O(n²) 평균, O(n) 최선
# ---------------------------------------------------------------------------
def insertion_sort(arr: list) -> list:
    """삽입 정렬 구현. 시간복잡도: O(n²) 평균, 공간복잡도: O(1)"""
    a = arr[:]
    for i in range(1, len(a)):       # 1번째부터 마지막까지
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:  # 적절한 위치 찾기
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ---------------------------------------------------------------------------
# 시간 측정 유틸리티
# ---------------------------------------------------------------------------
def measure_time(func, arr: list) -> float:
    """함수 실행 시간을 초 단위로 반환합니다."""
    data = copy.deepcopy(arr)
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


def benchmark(sizes: list) -> None:
    """다양한 입력 크기에 대해 정렬 알고리즘의 실행 시간을 비교합니다."""
    print("\n" + "=" * 70)
    print("  정렬 알고리즘 성능 비교")
    print("=" * 70)
    header = (
        f"{'입력 크기':>10}  "
        f"{'버블정렬(초)':>14} "
        f"{'삽입정렬(초)':>14} "
        f"{'sorted()(초)':>14}"
    )
    print(header)
    print("-" * 70)

    for size in sizes:
        random.seed(42)
        arr = [random.randint(1, 10 ** 6) for _ in range(size)]

        t_bubble = measure_time(bubble_sort, arr)
        t_insert = measure_time(insertion_sort, arr)

        # sorted()는 Timsort — O(n log n)
        start = time.perf_counter()
        sorted(arr)
        t_sorted = time.perf_counter() - start

        ratio_b = t_bubble / t_sorted if t_sorted > 0 else float('inf')
        ratio_i = t_insert / t_sorted if t_sorted > 0 else float('inf')

        print(
            f"{size:>10,}  "
            f"{t_bubble:>13.6f}s "
            f"{t_insert:>13.6f}s "
            f"{t_sorted:>13.6f}s"
        )
        print(
            f"{'':>10}  "
            f"  ({ratio_b:>6.1f}x 느림)   "
            f"({ratio_i:>6.1f}x 느림)"
        )

    print("=" * 70)
    print("[결론] O(n²) 알고리즘은 n이 커질수록 급격히 느려집니다.")
    print("       n=10,000 이상에서는 O(n log n)을 사용해야 합니다.")


def main():
    print("timeit 모듈 예제 — 짧은 코드 성능 측정")
    print("-" * 40)

    # timeit으로 list comprehension vs loop 비교
    t_comp = timeit.timeit(
        '[x**2 for x in range(1000)]',
        number=1000
    )
    t_loop = timeit.timeit(
        stmt=(
            'result = []\n'
            'for x in range(1000):\n'
            '    result.append(x**2)'
        ),
        number=1000
    )
    print(f"리스트 컴프리헨션 (1000회): {t_comp:.4f}초")
    print(f"for 루프 + append   (1000회): {t_loop:.4f}초")
    if t_comp > 0:
        print(f"컴프리헨션이 {t_loop/t_comp:.2f}배 빠름")

    # 정렬 알고리즘 벤치마크
    benchmark(sizes=[100, 1000, 5000])


if __name__ == "__main__":
    main()
