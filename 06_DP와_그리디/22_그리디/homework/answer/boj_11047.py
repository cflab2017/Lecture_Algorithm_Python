# 백준 11047 — 동전 0
# https://www.acmicpc.net/problem/11047
# Time: O(n)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    count = 0
    # 큰 동전부터 그리디
    for coin in reversed(coins):
        if coin <= k:
            count += k // coin
            k %= coin
        if k == 0:
            break

    print(count)


solve()
