# 주제: 계단 오르기 (Climbing Stairs) DP
# Time: O(n)   Space: O(n) → O(1)

def climb_basic(n: int) -> int:
    """기본 계단 오르기: 1칸 또는 2칸씩.

    dp[i] = i번 계단까지 오르는 방법 수
    dp[i] = dp[i-1] + dp[i-2]

    Time:  O(n)
    Space: O(n)
    """
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1   # {1}
    dp[2] = 2   # {1,1}, {2}

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_k_steps(n: int, k: int) -> int:
    """변형: 최대 k칸씩 오를 수 있을 때.

    dp[i] = dp[i-1] + dp[i-2] + ... + dp[i-k]

    Time:  O(n × k)
    Space: O(n)
    """
    dp = [0] * (n + 1)
    dp[0] = 1   # 0번 계단 = 시작점

    for i in range(1, n + 1):
        for step in range(1, k + 1):
            if i - step >= 0:
                dp[i] += dp[i - step]

    return dp[n]


def climb_no_consecutive_two(n: int) -> int:
    """백준 2579 변형: 연속으로 2칸을 두 번 연속 오를 수 없을 때.

    상태: dp[i][j]
      i = 현재 계단 번호
      j = 0: 이 계단이 연속 첫 번째, j = 1: 이 계단이 연속 두 번째

    실제 2579는 연속 3칸 불가이므로 아래 풀이 참고:

    dp[i][0] = i번 계단을 1번만 연속 (i-2에서 2칸 점프)
    dp[i][1] = i번 계단을 2번 연속 (i-1에서 1칸 점프)
    dp[i][0] = dp[i-2][0] + dp[i-2][1]  (점수 포함)
    dp[i][1] = dp[i-1][0]               (점수 포함)

    Time:  O(n)
    Space: O(n)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    # 단순 계단 수 계산 (점수 없는 버전)
    dp0 = [0] * (n + 1)  # 연속 첫 번째
    dp1 = [0] * (n + 1)  # 연속 두 번째

    dp0[1] = 1
    dp1[1] = 0
    if n >= 2:
        dp0[2] = 1
        dp1[2] = 1

    for i in range(3, n + 1):
        dp0[i] = dp0[i - 2] + dp1[i - 2]
        dp1[i] = dp0[i - 1]

    return dp0[n] + dp1[n]


def climb_ways_space_optimized(n: int) -> int:
    """공간 최적화 계단 오르기.

    Time:  O(n)
    Space: O(1)
    """
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 기본 계단 오르기 (1칸 또는 2칸) ===")
    print(f"{'n':>5} | {'방법 수':>10}")
    print("-" * 20)
    for n in range(1, 11):
        print(f"{n:>5} | {climb_basic(n):>10}")

    print("\n=== 최대 k칸 계단 오르기 ===")
    n = 10
    for k in [1, 2, 3, 4]:
        print(f"  n={n}, k={k}: {climb_k_steps(n, k)}가지")

    print("\n=== 경우 열거 (n=4, 1칸 or 2칸) ===")
    def enumerate_ways(n: int) -> list[list[int]]:
        if n == 0:
            return [[]]
        if n < 0:
            return []
        ways = []
        for step in [1, 2]:
            for rest in enumerate_ways(n - step):
                ways.append([step] + rest)
        return ways

    for n in range(1, 6):
        ways = enumerate_ways(n)
        print(f"  n={n}: {len(ways)}가지 → {ways[:3]}{'...' if len(ways) > 3 else ''}")

    print("\n=== 공간 최적화 ===")
    for n in [5, 10, 20, 50]:
        print(f"  climb({n}) = {climb_ways_space_optimized(n)}")
