# 주제: 동전 거스름돈 — 최소 개수 (그리디 실패), 경우의 수
# Time: O(amount × len(coins))
# Space: O(amount)


def min_coins(coins: list[int], amount: int) -> int:
    """최소 동전 개수 (DP).

    dp[i] = i원을 만들기 위한 최소 동전 수
    dp[0] = 0
    dp[i] = min(dp[i - coin] + 1) for coin ≤ i

    Time:  O(amount × len(coins))
    Space: O(amount)
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return int(dp[amount]) if dp[amount] != INF else -1


def greedy_coins(coins: list[int], amount: int) -> int:
    """그리디 동전 거스름돈 (항상 최적은 아님!).

    Time:  O(len(coins) × log(len(coins))) — 정렬 포함
    Space: O(1)
    """
    coins_sorted = sorted(coins, reverse=True)
    count = 0
    remaining = amount
    for coin in coins_sorted:
        count += remaining // coin
        remaining %= coin
    return count if remaining == 0 else -1


def count_ways(coins: list[int], amount: int) -> int:
    """동전으로 amount를 만드는 경우의 수 (순서 무관).

    dp[i] = i원을 만드는 방법 수
    각 동전을 순서대로 처리 → 중복 순열 방지

    Time:  O(amount × len(coins))
    Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1   # 0원: 동전 안 쓰는 1가지

    for coin in coins:           # 외부: 동전 종류
        for i in range(coin, amount + 1):   # 내부: 금액
            dp[i] += dp[i - coin]

    return dp[amount]


def count_permutations(coins: list[int], amount: int) -> int:
    """동전으로 amount를 만드는 순열 수 (순서 고려).

    dp[i] = i원을 만드는 순열 수
    (외부: 금액, 내부: 동전 종류)

    Time:  O(amount × len(coins))
    Space: O(amount)
    """
    dp = [0] * (amount + 1)
    dp[0] = 1

    for i in range(1, amount + 1):   # 외부: 금액
        for coin in coins:            # 내부: 동전 종류
            if coin <= i:
                dp[i] += dp[i - coin]

    return dp[amount]


def reconstruct_coins(coins: list[int], amount: int) -> list[int] | None:
    """최소 동전 조합 복원.

    Time:  O(amount × len(coins))
    Space: O(amount)
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)   # 역추적용

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == INF:
        return None

    # 역추적
    result: list[int] = []
    curr = amount
    while curr > 0:
        coin = parent[curr]
        result.append(coin)
        curr -= coin

    return sorted(result, reverse=True)


# ── 실행 예시 ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== 그리디 실패 예시 ===")
    coins_bad = [1, 5, 6, 9]
    amount = 11
    greedy_ans = greedy_coins(coins_bad, amount)
    dp_ans = min_coins(coins_bad, amount)
    print(f"  동전: {coins_bad}, 금액: {amount}")
    print(f"  그리디: {greedy_ans}개 (9+1+1)")
    print(f"  DP:     {dp_ans}개 (5+6)")

    print("\n=== 한국 동전 (그리디 최적) ===")
    korean_coins = [500, 100, 50, 10, 5, 1]
    for amount in [1260, 730, 999]:
        g = greedy_coins(korean_coins, amount)
        d = min_coins(korean_coins, amount)
        print(f"  {amount}원: 그리디={g}, DP={d}, {'일치' if g == d else '불일치!'}")

    print("\n=== 경우의 수 (조합 vs 순열) ===")
    coins = [1, 2, 3]
    for amt in [3, 4, 5]:
        comb = count_ways(coins, amt)
        perm = count_permutations(coins, amt)
        print(f"  {amt}원: 조합={comb}, 순열={perm}")

    print("\n=== 최소 동전 조합 복원 ===")
    test_cases = [(coins_bad, 11), ([1, 2, 5], 11), ([2], 3)]
    for c, a in test_cases:
        combo = reconstruct_coins(c, a)
        print(f"  동전={c}, 금액={a}: {combo}")
