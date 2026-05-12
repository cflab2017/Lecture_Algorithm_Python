# 백준 1463 — 1로 만들기
# https://www.acmicpc.net/problem/1463
# Time: O(n)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())

    dp = [0] * (n + 1)
    # dp[i] = i를 1로 만드는 최소 연산 수

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1          # 연산 3: 1 빼기
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[n])


solve()
