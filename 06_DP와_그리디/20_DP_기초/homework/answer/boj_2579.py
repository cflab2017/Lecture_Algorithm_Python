# 백준 2579 — 계단 오르기
# https://www.acmicpc.net/problem/2579
# Time: O(n)  Space: O(n)

import sys

input = sys.stdin.readline


def solve() -> None:
    n = int(input())
    score = [0] + [int(input()) for _ in range(n)]

    if n == 1:
        print(score[1])
        return
    if n == 2:
        print(score[1] + score[2])
        return

    # dp[i][0]: i번째 계단을 단독(i-2에서 점프) 밟았을 때 최대 점수
    # dp[i][1]: i번째 계단을 연속으로(i-1에서 왔을 때) 밟았을 때 최대 점수
    dp = [[0, 0] for _ in range(n + 1)]

    dp[1][0] = score[1]
    dp[1][1] = 0          # 1번을 연속으로 밟는 경우는 없음 (시작)
    dp[2][0] = score[2]   # 1번 건너뛰고 2번
    dp[2][1] = score[1] + score[2]   # 1번→2번 연속

    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + score[i]
        dp[i][1] = dp[i - 1][0] + score[i]

    print(max(dp[n][0], dp[n][1]))


solve()
