# 주제: 피보나치 타뷸레이션 (Bottom-up) 및 공간 최적화
# Time: O(n)   Space: O(n) → O(1) 최적화

def fib_tabulation(n: int) -> int:
    """타뷸레이션 피보나치 (Bottom-up).

    작은 문제부터 순서대로 테이블을 채움.

    Time:  O(n)
    Space: O(n) — dp 배열
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def fib_space_optimized(n: int) -> int:
    """공간 최적화 피보나치.

    dp[i]는 dp[i-1]과 dp[i-2]만 필요 → 변수 2개로 충분

    Time:  O(n)
    Space: O(1) ← 핵심!
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


def fib_generator(count: int):
    """피보나치 수열 생성기 (Generator).

    Time:  O(1) per yield
    Space: O(1)
    """
    a, b = 0, 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def fib_matrix(n: int) -> int:
    """행렬 거듭제곱을 이용한 피보나치 O(log n).

    [[1,1],[1,0]]^n = [[fib(n+1), fib(n)], [fib(n), fib(n-1)]]

    Time:  O(log n)
    Space: O(log n) — 재귀 스택
    """
    if n <= 1:
        return n

    def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [a[0][0]*b[0][0] + a[0][1]*b[1][0],
             a[0][0]*b[0][1] + a[0][1]*b[1][1]],
            [a[1][0]*b[0][0] + a[1][1]*b[1][0],
             a[1][0]*b[0][1] + a[1][1]*b[1][1]],
        ]

    def mat_pow(m: list[list[int]], p: int) -> list[list[int]]:
        if p == 1:
            return m
        if p % 2 == 0:
            half = mat_pow(m, p // 2)
            return mat_mul(half, half)
        return mat_mul(m, mat_pow(m, p - 1))

    base = [[1, 1], [1, 0]]
    result = mat_pow(base, n)
    return result[0][1]


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 타뷸레이션 vs 공간 최적화 ===")
    print(f"{'n':>5} | {'타뷸레이션':>15} | {'공간O(1)':>15} | {'행렬O(logn)':>15}")
    print("-" * 58)
    for n in [0, 1, 5, 10, 20, 30, 40]:
        t = fib_tabulation(n)
        s = fib_space_optimized(n)
        m = fib_matrix(n)
        print(f"{n:>5} | {t:>15} | {s:>15} | {m:>15}")

    print("\n=== 타뷸레이션 테이블 시각화 (n=10) ===")
    dp = [0] * 11
    dp[1] = 1
    print(f"dp[0] = {dp[0]}")
    print(f"dp[1] = {dp[1]}")
    for i in range(2, 11):
        dp[i] = dp[i-1] + dp[i-2]
        print(f"dp[{i}] = dp[{i-1}] + dp[{i-2}] = {dp[i-1]} + {dp[i-2]} = {dp[i]}")

    print("\n=== 피보나치 생성기 (처음 15개) ===")
    fib_list = list(fib_generator(15))
    print(f"  {fib_list}")

    print("\n=== 공간 최적화 과정 시각화 ===")
    prev2, prev1 = 0, 1
    print(f"  초기: prev2={prev2}, prev1={prev1}")
    for i in range(2, 11):
        curr = prev1 + prev2
        print(f"  i={i}: {prev2} + {prev1} = {curr}")
        prev2, prev1 = prev1, curr
    print(f"  결과: {prev1}")
