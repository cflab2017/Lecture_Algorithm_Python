# 백준 11726 — 2×n 타일링
# https://www.acmicpc.net/problem/11726
# Time: O(n)  Space: O(1)

import sys

input = sys.stdin.readline
MOD = 10_007


def solve() -> None:
    n = int(input())

    if n == 1:
        print(1)
        return

    # dp[i] = 2×i 타일링 방법 수
    # dp[i] = dp[i-1] + dp[i-2]
    # 공간 최적화: 변수 2개만 사용
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, (a + b) % MOD

    print(b)


solve()
