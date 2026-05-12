"""
백준 11659 — 구간 합 구하기 4
https://www.acmicpc.net/problem/11659

난이도 : Silver III
Time  : O(n + m)  n=수 개수, m=쿼리 수
Space : O(n)

풀이:
    1-indexed 1D 구간 합.
    prefix[i] = A[1] + ... + A[i]
    query(l, r) = prefix[r] - prefix[l-1]
"""

import sys

input = sys.stdin.readline


def solve() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    # 1-indexed prefix
    prefix = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix[i] = prefix[i - 1] + A[i - 1]

    result = []
    for _ in range(M):
        l, r = map(int, input().split())
        result.append(prefix[r] - prefix[l - 1])

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    solve()
