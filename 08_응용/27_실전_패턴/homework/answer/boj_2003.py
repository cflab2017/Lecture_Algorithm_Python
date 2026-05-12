"""
백준 2003 — 수들의 합 2
https://www.acmicpc.net/problem/2003

난이도 : Silver IV
Time  : O(n)
Space : O(n)

풀이:
    같은 방향 투 포인터.
    모든 A[i] ≥ 1 이므로 합이 M 이상이면 lo를 전진해도 안전.
    합 == M 이면 count++, lo 전진.
"""

import sys

input = sys.stdin.readline


def solve() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    lo = 0
    total = 0
    count = 0

    for hi in range(N):
        total += A[hi]

        # 합이 M 이상이면 lo 전진
        while total >= M and lo <= hi:
            if total == M:
                count += 1
            total -= A[lo]
            lo += 1

    print(count)


if __name__ == "__main__":
    solve()
