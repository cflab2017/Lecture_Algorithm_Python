# 주제: 피보나치 — 단순 재귀, 메모이제이션, @lru_cache
# Time: O(2^n) 단순재귀, O(n) 메모이제이션
# Space: O(n) 공통

import sys
import time
from functools import lru_cache

sys.setrecursionlimit(10_000)


# ── 방법 1: 단순 재귀 (비효율) ────────────────────────────────────────────
def fib_naive(n: int) -> int:
    """단순 재귀 피보나치.

    Time:  O(2^n) — 기하급수적 중복 계산
    Space: O(n)   — 재귀 스택
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ── 방법 2: 수동 메모이제이션 ────────────────────────────────────────────
def fib_memo(n: int, cache: dict[int, int] | None = None) -> int:
    """메모이제이션 피보나치.

    Time:  O(n) — 각 n에 대해 1번만 계산
    Space: O(n) — 캐시 딕셔너리
    """
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


# ── 방법 3: @lru_cache 데코레이터 ─────────────────────────────────────────
@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    """@lru_cache를 이용한 자동 메모이제이션.

    Time:  O(n)
    Space: O(n)
    """
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


# ── 방법 4: 명시적 메모 테이블 (클래스 변수) ─────────────────────────────
_memo: dict[int, int] = {}


def fib_global_memo(n: int) -> int:
    """전역 딕셔너리 메모이제이션.

    Time:  O(n) — 전체 호출에 걸쳐
    Space: O(n)
    """
    if n in _memo:
        return _memo[n]
    if n <= 1:
        _memo[n] = n
        return n
    _memo[n] = fib_global_memo(n - 1) + fib_global_memo(n - 2)
    return _memo[n]


# ── 성능 비교 ──────────────────────────────────────────────────────────────
def benchmark(func, n: int, label: str) -> None:
    start = time.perf_counter()
    result = func(n)
    elapsed = time.perf_counter() - start
    print(f"  {label:30s}: fib({n}) = {result}, 시간 = {elapsed:.6f}s")


if __name__ == "__main__":
    print("=== 피보나치 결과 확인 ===")
    for i in range(11):
        print(f"  fib({i:2d}) = {fib_lru(i)}", end="")
        if i < 10:
            print(",", end="")
    print()

    print("\n=== 성능 비교 ===")
    n = 30
    benchmark(fib_naive, n, "단순 재귀")
    benchmark(lambda x: fib_memo(x), n, "수동 메모이제이션")
    benchmark(fib_lru, n, "@lru_cache")
    benchmark(fib_global_memo, n, "전역 딕셔너리")

    print("\n=== 단순 재귀 한계 ===")
    print(f"  fib(35) 단순 재귀: {fib_naive(35)} (느림...)")
    print(f"  fib(35) lru_cache:  {fib_lru(35)} (즉시)")

    print("\n=== @lru_cache 캐시 정보 ===")
    info = fib_lru.cache_info()
    print(f"  hits={info.hits}, misses={info.misses}, size={info.currsize}")
