# =============================================================================
# 파일명: 01_list_complexity.py
# 설명  : list 연산별 시간복잡도를 timeit으로 실측
# 시간복잡도: append O(1) 분할상환, insert(0) O(n), pop() O(1), pop(0) O(n)
# 공간복잡도: O(n) — 리스트 크기
# =============================================================================

import timeit
import time


# ---------------------------------------------------------------------------
# append vs insert(0) 비교
# ---------------------------------------------------------------------------
def benchmark_append_vs_insert(n: int = 10_000) -> None:
    """끝에 추가(append)와 앞에 삽입(insert(0))의 속도를 비교합니다."""
    print(f"\n[append vs insert(0)] n={n:,}번 수행")
    print("-" * 50)

    # append — O(1) 분할 상환
    t_append = timeit.timeit(
        stmt='lst.append(0)',
        setup='lst = []',
        number=n
    )

    # insert(0) — O(n): 모든 원소를 한 칸씩 오른쪽으로 이동
    t_insert = timeit.timeit(
        stmt='lst.insert(0, 0)',
        setup='lst = []',
        number=n
    )

    ratio = t_insert / t_append if t_append > 0 else float('inf')
    print(f"  append:    {t_append:.6f}초  (O(1) 분할상환)")
    print(f"  insert(0): {t_insert:.6f}초  (O(n))")
    print(f"  insert(0)가 {ratio:.1f}배 느림")

    # 리스트 크기가 커질수록 차이가 벌어지는지 확인
    print(f"\n  리스트 크기별 insert(0) 시간 변화:")
    for size in [1_000, 5_000, 10_000, 50_000]:
        t = timeit.timeit(
            stmt='lst.insert(0, 0)',
            setup=f'lst = list(range({size}))',
            number=1000
        )
        print(f"    크기={size:>6,}: {t:.6f}초 (1000회)")


# ---------------------------------------------------------------------------
# pop() vs pop(0) 비교
# ---------------------------------------------------------------------------
def benchmark_pop_vs_pop0(n: int = 5_000) -> None:
    """끝에서 제거(pop())와 앞에서 제거(pop(0))의 속도를 비교합니다."""
    print(f"\n[pop() vs pop(0)] n={n:,}번 수행")
    print("-" * 50)

    # pop() — O(1): 끝 원소만 제거
    t_pop = timeit.timeit(
        stmt='lst.pop()',
        setup=f'lst = list(range({n * 2}))',
        number=n
    )

    # pop(0) — O(n): 첫 원소 제거 후 모든 원소를 왼쪽으로 이동
    t_pop0 = timeit.timeit(
        stmt='lst.pop(0)',
        setup=f'lst = list(range({n * 2}))',
        number=n
    )

    ratio = t_pop0 / t_pop if t_pop > 0 else float('inf')
    print(f"  pop():  {t_pop:.6f}초  (O(1))")
    print(f"  pop(0): {t_pop0:.6f}초  (O(n))")
    print(f"  pop(0)가 {ratio:.1f}배 느림")


# ---------------------------------------------------------------------------
# 인덱스 접근 vs 선형 탐색
# ---------------------------------------------------------------------------
def benchmark_index_vs_search(n: int = 100_000) -> None:
    """인덱스 접근(O(1))과 선형 탐색(O(n))을 비교합니다."""
    print(f"\n[인덱스 접근 vs 선형 탐색] n={n:,}")
    print("-" * 50)

    # 인덱스 접근 — O(1)
    t_index = timeit.timeit(
        stmt=f'_ = lst[{n // 2}]',
        setup=f'lst = list(range({n}))',
        number=10_000
    )

    # 선형 탐색 (최악의 경우: 마지막 원소) — O(n)
    t_search = timeit.timeit(
        stmt=f'_ = {n - 1} in lst',
        setup=f'lst = list(range({n}))',
        number=1_000
    )

    print(f"  lst[n//2] (인덱스):     {t_index:.6f}초 (10000회)")
    print(f"  n-1 in lst (선형탐색): {t_search:.6f}초 (1000회)")
    print(f"  [참고] set 멤버십은 O(1) 평균 → 더 빠름")


# ---------------------------------------------------------------------------
# 슬라이싱 복사 — O(k) (슬라이스 크기에 비례)
# ---------------------------------------------------------------------------
def benchmark_slicing(n: int = 100_000) -> None:
    """슬라이싱의 시간복잡도를 확인합니다."""
    print(f"\n[슬라이싱 복잡도] n={n:,}")
    print("-" * 50)
    lst = list(range(n))

    for k in [10, 1_000, 10_000, n]:
        t0 = time.perf_counter()
        for _ in range(1000):
            _ = lst[:k]     # O(k) — k개를 복사
        elapsed = time.perf_counter() - t0
        print(f"  lst[:{k:>7,}] 슬라이싱 1000회: {elapsed:.4f}초")

    print("  [결론] 슬라이싱은 O(k) — 슬라이스 크기에 비례")


def main():
    print("=" * 55)
    print("  list 연산 시간복잡도 실측")
    print("=" * 55)

    benchmark_append_vs_insert(n=10_000)
    benchmark_pop_vs_pop0(n=5_000)
    benchmark_index_vs_search(n=100_000)
    benchmark_slicing(n=100_000)

    print("\n" + "=" * 55)
    print("  핵심 정리")
    print("=" * 55)
    print("  append(x)     : O(1) 분할상환  ← 끝에 추가")
    print("  insert(0, x)  : O(n)           ← 앞에 추가 (피해야 함)")
    print("  pop()         : O(1)           ← 끝 제거")
    print("  pop(0)        : O(n)           ← 앞 제거 (피해야 함)")
    print("  lst[i]        : O(1)           ← 랜덤 접근")
    print("  x in lst      : O(n)           ← 선형 탐색")
    print("  대안: 앞뒤 O(1) 연산이 필요하면 deque를 사용하세요!")


if __name__ == "__main__":
    main()
