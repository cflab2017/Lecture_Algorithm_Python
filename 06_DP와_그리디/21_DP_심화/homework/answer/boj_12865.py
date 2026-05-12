# 백준 12865 — 평범한 배낭
# https://www.acmicpc.net/problem/12865
# Time: O(N × K)  Space: O(K)

import sys

input = sys.stdin.readline


def solve() -> None:
    n, k = map(int, input().split())
    items = [tuple(map(int, input().split())) for _ in range(n)]

    dp = [0] * (k + 1)

    for weight, value in items:
        # 역방향 순회: 0/1 배낭 (같은 물건 중복 방지)
        for w in range(k, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    print(dp[k])


solve()
