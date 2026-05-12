# 백준 11053 — 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
# Time: O(n²)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))

    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


solve()
