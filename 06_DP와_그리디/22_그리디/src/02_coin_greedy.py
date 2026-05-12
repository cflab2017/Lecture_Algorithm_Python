# 주제: 동전 거스름돈 — 그리디 (언제 최적이고 언제 실패하는가)
# Time: O(k) 그리디 — k = 동전 종류 수
# Space: O(1)


def coin_greedy(coins: list[int], amount: int) -> tuple[int, list[int]]:
    """그리디 동전 거스름돈 (큰 동전부터 사용).

    Time:  O(k log k + k) = O(k log k)
    Space: O(k) 결과 저장
    """
    coins_sorted = sorted(coins, reverse=True)
    result: list[int] = []
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    return len(result) if remaining == 0 else -1, result


def coin_dp(coins: list[int], amount: int) -> tuple[int, list[int]]:
    """DP 동전 거스름돈 (최적 보장).

    Time:  O(amount × k)
    Space: O(amount)
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == INF:
        return -1, []

    # 역추적
    result: list[int] = []
    curr = amount
    while curr > 0:
        result.append(parent[curr])
        curr -= parent[curr]

    return int(dp[amount]), sorted(result, reverse=True)


def is_greedy_optimal(coins: list[int], max_amount: int = 1000) -> bool:
    """주어진 동전 집합에서 그리디가 항상 최적인지 확인.

    Time:  O(max_amount × k²)
    Space: O(max_amount)
    """
    for amount in range(1, max_amount + 1):
        g_count, _ = coin_greedy(coins, amount)
        d_count, _ = coin_dp(coins, amount)
        if g_count != d_count and g_count != -1:
            return False
    return True


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 한국 동전 (그리디 최적) ===")
    korean = [500, 100, 50, 10, 5, 1]
    test_amounts = [1260, 730, 999, 376]
    for amt in test_amounts:
        g_cnt, g_coins = coin_greedy(korean, amt)
        d_cnt, d_coins = coin_dp(korean, amt)
        status = "일치 ✓" if g_cnt == d_cnt else "불일치 ✗"
        print(f"  {amt:4d}원: 그리디={g_cnt}개 {g_coins}, DP={d_cnt}개 → {status}")

    print("\n=== 그리디 실패 예시 ===")
    bad_coins = [1, 5, 6, 9]
    for amt in [10, 11, 12]:
        g_cnt, g_coins = coin_greedy(bad_coins, amt)
        d_cnt, d_coins = coin_dp(bad_coins, amt)
        status = "일치 ✓" if g_cnt == d_cnt else "그리디 실패 ✗"
        print(f"  동전={bad_coins}, {amt}원:")
        print(f"    그리디: {g_cnt}개 {g_coins}")
        print(f"    DP:     {d_cnt}개 {d_coins} → {status}")

    print("\n=== 그리디 최적 조건 분석 ===")
    coin_sets = [
        ([1, 5, 10, 50, 100, 500], "한국 동전"),
        ([1, 5, 6, 9], "그리디 실패"),
        ([1, 2, 5, 10, 20, 50, 100, 200], "유로 동전"),
        ([1, 3, 4], "실패 예시 2"),
    ]
    for coins, name in coin_sets:
        optimal = is_greedy_optimal(coins, 100)
        print(f"  {name:15s} {coins}: 그리디 최적? {optimal}")
